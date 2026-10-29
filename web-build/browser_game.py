"""Browser presentation adapter; recovered gameplay and timelines stay unchanged."""
import asyncio
import base64
import sys
import time
import types
from pathlib import Path

import js
import pygame
from PIL import Image

def browser_image_load(source, *args):
    # The Pyodide SDL build cannot load Pygame's Python file-like resources.
    # Decode with the bundled Pillow build, then copy pixels to an SDL surface.
    image=Image.open(source).convert('RGBA')
    return pygame.image.frombytes(image.tobytes(),image.size,'RGBA')

pygame.image.load=browser_image_load

def raster_svg(svg_string, **kwargs):
    return bytes(js.rasterSVG(svg_string).to_py())

sys.modules['resvg_py'] = types.SimpleNamespace(svg_to_bytes=raster_svg)

from wd2.resources import read_asset, asset_directory
from wd2.runtime import get
from wd2.setup_menu import SetupMenu
from wd2.iphone_ui import LandscapeUI

class BrowserLandscapeUI(LandscapeUI):
    def font(self, size):
        if size not in self.fonts:
            path=Path('/tmp/wd2-mobile-font.ttf')
            if not path.exists():
                path.write_bytes(read_asset(next(asset_directory('fonts').glob('1_*.ttf*'))))
            self.fonts[size]=self.pg.font.Font(str(path),size)
        return self.fonts[size]

menu = None
ui = None
screen = None
mobile = False


class BrowserAudio:
    def __init__(self, host):
        self.host=host;self.voices={};self.samples={};self.serial=0
        self.paused=False;self.muted=False

    def start(self, sound):
        self.stop(sound);self.serial+=1;voice=self.serial
        key=sound.linkage
        if key not in self.samples:
            self.samples[key]=base64.b64encode(read_asset(sound.host.asset(key))).decode('ascii')
        self.voices[id(sound)]=(voice,sound)
        js.browserAudio.play(voice,key,self.samples[key],sound.volume/100,sound.pan/100,sound.loops)

    def stop(self, sound):
        item=self.voices.pop(id(sound),None)
        if item:js.browserAudio.stop(item[0])

    def volume(self, sound):
        item=self.voices.get(id(sound))
        if item:js.browserAudio.volume(item[0],sound.volume/100,sound.pan/100)

    def poll(self):
        if self.paused:return
        for key,(voice,sound) in list(self.voices.items()):
            if not js.browserAudio.active(voice) and self.voices.get(key)==(voice,sound):
                del self.voices[key];js.browserAudio.stop(voice);sound.host.complete(sound)

    def pause(self, paused):
        self.paused=bool(paused);js.browserAudio.pause(self.paused)

    def set_muted(self, muted):
        self.muted=bool(muted);js.browserAudio.mute(self.muted)


def pointer_down(x,y):
    if ui:ui.down((x,y),time.monotonic())
    elif menu:menu.motion((x,y));menu.click((x,y))

def pointer_move(x,y):
    if ui:ui.motion((x,y),time.monotonic())
    elif menu:menu.motion((x,y))

def pointer_up(x,y):
    if ui:ui.up((x,y),time.monotonic())
    elif menu:menu.release((x,y))

def pointer_wheel(x,y,amount):
    if ui:ui.wheel((x,y),amount)

def key_down(key):
    if not menu:return
    if menu.text_entry.active():
        keys={'Backspace':pygame.K_BACKSPACE,'Delete':pygame.K_DELETE,'ArrowLeft':pygame.K_LEFT,
              'ArrowRight':pygame.K_RIGHT,'Home':pygame.K_HOME,'End':pygame.K_END,'Escape':pygame.K_ESCAPE}
        if key in keys:menu.text_entry.key(keys[key])
        elif len(key)==1:menu.text_entry.insert(key)
    elif key.lower()=='p':
        menu.host.clock.paused=not menu.host.clock.paused;menu.audio.pause(menu.host.clock.paused)

async def run():
    global menu,ui,screen,mobile
    query=js.URLSearchParams.new(js.location.search)
    mode=query.get('mode')
    mobile=mode=='mobile' or (mode!='desktop' and bool(js.window.matchMedia('(pointer: coarse)').matches)
                               and min(js.window.innerWidth,js.window.innerHeight)<700)
    density=min(2,max(1,float(js.window.devicePixelRatio))) if mobile else 1
    size=(round(896*density),round(414*density)) if mobile else (800,600)
    pygame.display.init();pygame.font.init()
    screen=pygame.display.set_mode(size)
    menu=SetupMenu(0);menu.play_battles=True
    menu.audio.connect(BrowserAudio(menu.audio))
    if mobile:ui=BrowserLandscapeUI(menu,size)
    accumulator=0.;previous=time.monotonic()
    while True:
        now=time.monotonic();dt=min(now-previous,.25);previous=now
        accumulator+=dt*24;ticks=int(accumulator);accumulator-=ticks
        pygame.event.pump();menu.audio.poll();menu.step(ticks)
        if ui:ui.step(dt);frame=ui.draw()
        else:frame=menu.surface(pygame)
        screen.blit(frame,(0,0));pygame.display.flip()
        await asyncio.sleep(0)
