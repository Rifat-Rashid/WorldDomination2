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
    tap(ui,(ui.nav.centerx,ui.nav.y+9*48-ui.navigation.offset-24))
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
                point=(camera.target.x+(source[0]-camera.source.x)*camera.target.w/camera.source.w,
                       camera.target.y+(source[1]-camera.source.y)*camera.target.h/camera.source.h)
                assert ui.map.collidepoint(point)
                assert ui.stage(point)==pytest.approx(source,abs=1e-6)
        assert all(r.w>=44 and r.h>=44 for r,a in ui.targets if r.h>=44)
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
