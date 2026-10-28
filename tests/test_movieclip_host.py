from fractions import Fraction
import math

import pytest

from wd2.display_list import MovieClip, Matrix, Operation, Symbol, Timeline
from wd2.generated import register_all
from wd2.movieclip_host import MovieClipHost
from wd2.presentation_clock import PresentationClock
from wd2.runtime import Runtime, ASFunction, obj, get, ref, Scope, U
from wd2.swf_scene import SWFDocument


def tiny_host():
    symbols = {0: Symbol(0, 0, timeline=Timeline()),
               1: Symbol(1, 39, 'test_clip', Timeline([[], []]))}
    return MovieClipHost(Runtime(12), MovieClip(symbols))


def test_clip_properties_parent_lookup_transform_and_native_calls():
    h = tiny_host()
    clip = h.rt.invoke(h.root, 'attachMovie', 'test_clip', 'child', 5, obj({'_x': 10, '_y': 20}))
    assert get(h.rt.globals, '_root') is h.root and get(h.root, 'child') is clip
    assert get(clip, '_parent') is h.root and get(clip, '_root') is h.root
    clip.set('_rotation', 30); clip.set('_xscale', -50); clip.set('_yscale', 80)
    assert get(clip, '_xscale') == pytest.approx(-50)
    assert get(clip, '_yscale') == pytest.approx(80)
    assert get(clip, '_rotation') == pytest.approx(30)
    assert clip.node.matrix.point(0, 0) == (10, 20)
    assert clip.node.matrix.a == pytest.approx(-.5*math.cos(math.pi/6))
    clip.set('_alpha', 35); clip.set('_visible', False)
    assert get(clip, '_alpha') == 35 and not clip.node.visible
    assert h.rt.invoke(clip, 'getDepth') == 5
    assert h.rt.invoke(h.root, 'getNextHighestDepth') == 6
    assert ref(h.root, 'child').exists()
    assert Scope(h.rt, clip, [], [], []).call('stop', []) is U
    assert not clip.node.playing
    h.rt.invoke(clip, 'removeMovieClip')
    assert get(h.root, 'child') is U and get(clip, '_parent') is U


def test_mouse_coordinates_use_inverse_parent_transform_and_scope_lookup():
    h = tiny_host()
    parent = h.rt.invoke(h.root, 'attachMovie', 'test_clip', 'parent', 1)
    child = h.rt.invoke(parent, 'attachMovie', 'test_clip', 'child', 2)
    parent.node.matrix = Matrix(0, 2, -3, 0, 100, 200)
    child.node.matrix = Matrix(1, .2, .3, 1, 10, 20)
    h.pointer = child.node.world_matrix.point(5, 7)
    assert get(child, '_xmouse') == pytest.approx(5)
    assert get(child, '_ymouse') == pytest.approx(7)
    assert Scope(h.rt, child, [], [], []).get('_xmouse') == pytest.approx(5)


def test_frame_controls_preserve_live_reference_across_inherited_move_and_back_seek():
    h = tiny_host()
    h.tree.symbol.timeline = Timeline([
        [Operation(3, {'character_id': 1, 'name': 'persistent', 'matrix': Matrix(tx=2)})],
        [Operation(3, {'matrix': Matrix(tx=7)}, move=True)]], {'first': 1, 'second': 2})
    h.tree.frame = 0
    h.goto(h.tree, 1, False)
    child = get(h.root, 'persistent'); child.set('marker', 99)
    h.rt.invoke(h.root, 'gotoAndStop', 'second')
    assert get(h.root, 'persistent') is child and get(child, '_x') == 7
    h.rt.invoke(h.root, 'gotoAndStop', 'first')
    assert get(h.root, 'persistent') is child and get(child, 'marker') == 99
    assert get(child, '_x') == 2
    h.rt.invoke(child, 'gotoAndPlay', 1); h.clock.step()
    assert get(child, '_currentframe') == 2 and get(child, '_totalframes') == 2
    h.rt.invoke(child, 'stop'); h.clock.step()
    assert get(child, '_currentframe') == 2
    h.rt.invoke(child, 'gotoAndStop', 1); h.rt.invoke(child, 'nextFrame')
    assert get(child, '_currentframe') == 2 and not child.node.playing
    h.rt.invoke(child, 'prevFrame')
    assert get(child, '_currentframe') == 1 and not child.node.playing


def test_text_and_html_properties_keep_original_hud_messages_in_sync():
    h = tiny_host()
    h.tree.symbols[2] = Symbol(2, 37, 'text_field')
    text = h.rt.invoke(h.root, 'attachMovie', 2, 'message', 5)
    text.set('htmlText', '<b>Welcome</b><br>Funds &amp; stock')
    assert get(text, 'text') == 'Welcome\nFunds & stock'
    text.set('text', 'Turn 1 <ready>')
    text.set('textColor', 0x00FF00)
    assert get(text, 'htmlText') == 'Turn 1 &lt;ready&gt;'
    assert text.node.as2_text['textColor'] == 0x00FF00


def test_timer_order_deadlines_cancellation_pause_resume():
    events = []
    clock = PresentationClock(lambda: events.append('frame'))
    first = clock.set_interval(lambda: events.append('a'), 50)
    second = clock.set_interval(lambda: events.append('b'), 50)
    clock.step(3)
    assert events == ['frame', 'frame', 'a', 'b', 'frame', 'a', 'b']
    assert clock.milliseconds == 125
    clock.clear_interval(first); clock.pause(); clock.step(10)
    assert clock.ticks == 3
    clock.resume(); clock.step()
    assert events[-2:] == ['frame', 'b']
    clock.clear_interval(second)
    clock.step(20)
    assert clock.milliseconds == 1000


def test_runtime_callbacks_receiver_self_cancellation_and_new_timers_deferred():
    h = tiny_host(); events = []
    clip = h.rt.invoke(h.root, 'attachMovie', 'test_clip', 'child', 1)
    clip.set('onEnterFrame', ASFunction(lambda rt, this, args, closure: events.append(this)))
    target = obj({'tick': lambda value: events.append(value)})
    timer_id = h.rt.invoke(h.rt.globals, 'setInterval', target, 'tick', 40, 'timer')
    rng = h.rt.rng.getstate()
    h.clock.step()
    assert events == [clip, 'timer']
    h.rt.invoke(h.rt.globals, 'clearInterval', timer_id)
    clip.delete('onEnterFrame')
    ids = []
    def self_cancel():
        events.append('once')
        h.clock.clear_interval(ids[0])
        h.clock.set_interval(lambda: events.append('new'), 1)
    ids.append(h.clock.set_interval(self_cancel, 1))
    h.clock.step()
    assert events[-1] == 'once'
    h.clock.step()
    assert events[-1] == 'new'
    assert h.rt.rng.getstate() == rng and not h.rt.missing_calls


def test_source_timeline_stop_scripts_execute_through_adapter():
    d = SWFDocument(); rt = Runtime(); register_all(rt)
    node = MovieClip(d.symbols, 4586)
    host = MovieClipHost(rt, node, {4586})
    host.enter(node)
    assert not node.playing
    host.rt.invoke(host.root, 'gotoAndPlay', 1)
    host.clock.step()
    assert node.frame == 2
    assert not rt.missing_calls
