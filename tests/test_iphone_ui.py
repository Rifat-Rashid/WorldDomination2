import os
os.environ.setdefault('SDL_VIDEODRIVER','dummy')
os.environ.setdefault('SDL_AUDIODRIVER','dummy')
import hashlib
from pathlib import Path
import pygame
import pytest
from wd2.iphone_ui import LandscapeUI, ScrollPane
from wd2.setup_menu import SetupMenu
from wd2.runtime import get

@pytest.fixture
def ui():
    pygame.init();pygame.display.set_mode((1,1),pygame.HIDDEN)
    menu=SetupMenu(0);menu.press('splashScreenMC')
    for i in range(1,5):menu.press(f'BTN_allLeaders_screen{i}')
    menu.start_game()
    result=LandscapeUI(menu,(896,414));result.draw()
    yield result
    menu.audio.close();pygame.quit()

def tap(ui,point):
    p=tuple(x*ui.density for x in point)
    ui.down(p,0);ui.up(p,.1)

def test_scrolling_clips_and_reaches_all_nine_actions_without_selecting_on_drag(ui):
    state=ui.menu.game.snapshot()
    ui.down(ui.nav.center,0);ui.motion((ui.nav.centerx,ui.nav.centery-90),.1);ui.up((ui.nav.centerx,ui.nav.centery-90),.2)
    assert ui.navigation.offset>0
    assert ui.menu.game.snapshot()==state
    assert get(ui.menu.model,'userSelectedActionBtn') != 'diplomacy'
    ui.wheel(ui.nav.center,-100);ui.draw()
    assert ui.navigation.offset==ui.navigation.limit
    assert all(ui.nav.contains(r) for r,a in ui.targets if r.colliderect(ui.nav))
    tap(ui,(ui.nav.centerx,ui.nav.y+9*44-ui.navigation.offset-22))
    assert get(ui.menu.model,'userSelectedActionBtn')=='diplomacy'

def test_equipment_scroll_is_independent_and_swipes_do_not_select(ui):
    ui.wheel(ui.stock.center,-5)
    assert ui.equipment.offset>0 and ui.navigation.offset==0
    ui.wheel(ui.nav.center,-2)
    before=ui.equipment.offset
    ui.step(.1)
    assert ui.equipment.offset==before
    ui.draw()
    targets=[r for r,a in ui.targets if r.colliderect(ui.stock)]
    assert targets and all(ui.stock.contains(r) for r in targets)

def test_map_camera_inverse_hits_every_city_and_render_is_pure(ui):
    menu=ui.menu
    state,rng=menu.game.snapshot(),menu.rt.rng.getstate()
    matrices=[n.matrix for n in menu.tree.walk()]
    for size in [(896,414),(844,390),(932,430),(1280,720)]:
        ui.resize(size);ui.draw()
        camera=ui.patches[-1]
        for player in menu.game.players:
            for city in get(player,'cityArr'):
                source=(205+get(city,'xPos')*.46,135+get(city,'yPos')*.46)
                point=camera.project(get(city,'xPos'),get(city,'yPos'),get(player,'playerNum'))
                assert ui.map.collidepoint(point)
                assert ui.stage(point)==pytest.approx(source,abs=1e-6)
        if size[0]/size[1]>2:assert ui.map.w/ui.map.h > 1.5
        assert ui.map.left>=ui.center.left and ui.map.right<=ui.center.right
    assert [n.matrix for n in menu.tree.walk()]==matrices
    assert menu.game.snapshot()==state and menu.rt.rng.getstate()==rng

def test_mobile_actions_use_existing_queue_and_turn_resolution(ui):
    tap(ui,(ui.nav.centerx,ui.nav.y+22));ui.draw()
    assert get(ui.menu.model,'userSelectedActionBtn')=='resources'
    ui.menu.press('btnAccept')
    ui.menu.press('btn4');ui.menu.press('btnAccept');ui.draw()
    tap(ui,ui.targets[-1][0].center)
    assert get(ui.menu.model,'turn')==1
    assert get(ui.menu.game.human,'money')>=100

def test_inertia_clamps():
    pane=ScrollPane(30,1000,100);pane.step(1)
    assert pane.offset==100 and pane.velocity==0
    pane.move(-1000);assert pane.offset==0

def test_safe_area_has_no_hit_targets(ui):
    assert ui.stage((0,100)) is None
    assert ui.content.left>=44 and ui.content.right<=ui.width-44
    assert ui.content.bottom<=ui.height-21

def test_launcher_does_not_depend_on_desktop_entrypoint():
    root=Path(__file__).resolve().parents[1]
    source=(root/'iphone_build.py').read_text(encoding='utf-8-sig')
    assert 'run_game' not in source

def test_real_event_loop_routes_touch_drag_and_wheel_without_ghost_taps(ui, monkeypatch):
    from wd2.iphone_ui import run
    pg=pygame
    cx,cy=ui.stock.center
    groups=iter([
        [pg.event.Event(pg.FINGERDOWN,finger_id=7,x=cx/ui.width,y=cy/ui.height)],
        [pg.event.Event(pg.FINGERMOTION,finger_id=7,x=cx/ui.width,y=(cy-70)/ui.height)],
        [pg.event.Event(pg.FINGERUP,finger_id=7,x=cx/ui.width,y=(cy-70)/ui.height)],
        [pg.event.Event(pg.MOUSEWHEEL,y=-2,precise_y=-2)],
        [pg.event.Event(pg.QUIT)],
    ])
    monkeypatch.setattr(pg.event,'get',lambda:next(groups))
    monkeypatch.setattr(pg.mouse,'get_pos',lambda:ui.nav.center)
    state=ui.menu.game.snapshot();run(ui)
    assert ui.equipment.offset>=60 and ui.navigation.offset>0
    assert ui.menu.game.snapshot()['turn']==state['turn']

def test_simple_action_keeps_map_and_accept_strip_visible(ui):
    from wd2.iphone_map import IslandCamera
    tap(ui,(ui.nav.centerx,ui.nav.y+20));ui.draw()
    assert get(ui.menu.model,'userSelectedActionBtn')=='resources'
    assert not ui.details_open
    assert any(isinstance(p,IslandCamera) for p in ui.patches)
    assert ui.map.h>ui.content.h*.55
    # Source accept callback is exposed in the compact strip, not a screenshot.
    target=next(rect for rect,fn in ui.targets if ui.messages.contains(rect) and rect.centerx>ui.messages.centerx+ui.messages.w*.2)
    tap(ui,target.center)
    assert get(get(ui.menu.game.human,'turnActionArr')[0],'action')=='resources'


def test_filled_tube_cancels_once_without_queuing_skip(ui):
    ui.menu.press('btn1');ui.menu.press('btnAccept');ui.draw()
    tube=ui.targets[-3][0]
    pos=tuple(v*ui.density for v in tube.center)
    ui.down(pos,0)
    assert get(get(ui.menu.game.human,'turnActionArr')[0],'action')=='resources'
    ui.up(pos,.1)
    from wd2.runtime import U
    assert get(get(ui.menu.game.human,'turnActionArr')[0],'action') is U


def test_reflowed_enemy_city_click_uses_original_target_handler(ui):
    from wd2.action_entry import control_path
    from wd2.runtime import U
    menu=ui.menu
    menu.press('btn5')
    button=next(b for b in get(menu.gameplay.hud,'stockBtn_arr') if b is not U and get(b,'relatedWeapon')=='soldier1')
    menu.press(control_path(get(button,'overlayMC').node));ui.draw()
    city=get(menu.game.players[2],'cityArr')[1]
    point=ui.camera.project(get(city,'xPos'),get(city,'yPos'),2)
    tap(ui,point)
    assert get(menu.model,'userSelectedCity') is city


def test_mobile_skin_snapshot_cannot_capture_a_live_resource_modal(ui):
    from wd2.iphone_skin import MobileSkin
    ui.menu.press('btn1')
    before=ui.menu.game.snapshot();matrices=[n.matrix for n in ui.menu.tree.walk()]
    skin=MobileSkin(ui.menu,pygame)
    # This patch must contain blue ocean even when the original center panel is orange.
    patch=skin.crop((358,159,48,50))
    color=patch.get_at((patch.get_width()//2,patch.get_height()//2))
    assert color.b>color.r and color.b>color.g
    assert ui.menu.game.snapshot()==before
    assert [n.matrix for n in ui.menu.tree.walk()]==matrices
