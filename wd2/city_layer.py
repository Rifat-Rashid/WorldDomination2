"""Registered raster city presentation; frame/depth decisions belong to City."""
import json
from pathlib import Path

from .runtime import get, number

ROOT = Path(__file__).resolve().parents[1]


class CityLayer:
    def __init__(self, pygame, directory=ROOT / 'assets/cities'):
        self.pg = pygame
        self.manifest = json.loads((directory / 'manifest.json').read_text(encoding='utf-8'))
        self.scale = self.manifest['scale']
        self.frames = {}
        for theme, symbol in self.manifest['symbols'].items():
            for frame, entry in symbol['frames'].items():
                art = pygame.image.load(directory / entry['file'])
                size = tuple(max(1, round(v * self.scale)) for v in art.get_size())
                self.frames[theme, int(frame)] = (
                    pygame.transform.smoothscale(art, size), entry['offset'])

    @staticmethod
    def ordered_cities(game):
        cities = [(i, j, city) for i, player in enumerate(game.players)
                  for j, city in enumerate(get(player, 'cityArr'))]
        return sorted(cities, key=lambda row: number(get(row[2], 'image_depth')))

    def draw(self, surface, city, origin=(0, 0)):
        # Reading size_and_frame here would mutate recovered gameplay state every
        # render. Game synchronizes the clip once at each model update instead.
        frame = int(number(get(get(city, 'image'), '_currentframe')))
        art, offset = self.frames[get(city, 'citySet'), frame]
        position = tuple(round(origin[k] + number(get(city, name)) + offset[k] * self.scale)
                         for k, name in enumerate(('xPos', 'yPos')))
        surface.blit(art, position)
        return self.pg.Rect(position, art.get_size())
