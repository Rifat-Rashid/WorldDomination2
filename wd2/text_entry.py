"""Native keyboard/focus boundary for original editable SWF text fields."""
from .action_entry import visible
from .runtime import get, U


class TextEntry:
    def __init__(self, menu):
        self.menu, self.node = menu, None
        self.caret, self.select_all = 0, False

    def at(self, point):
        for node in reversed(list(self.menu.tree.walk())):
            if not visible(node):
                continue
            if get(self.menu.host.wrap(node), 'onPress') is not U:
                bounds = self.menu.renderer.control_bounds(node)
                if bounds and bounds[0] <= point[0] <= bounds[2] and bounds[1] <= point[1] <= bounds[3]:
                    return None  # Original button overlays intercept fields below them.
            field = self.menu.renderer.fields.get(node.character_id)
            if not field or not field.get('editable'):
                continue
            x0, x1, y0, y1 = field['bounds']
            m = node.world_matrix
            p = [m.point(x,y) for x,y in ((x0,y0),(x1,y0),(x0,y1),(x1,y1))]
            if min(x for x,y in p) <= point[0] <= max(x for x,y in p) and min(y for x,y in p) <= point[1] <= max(y for x,y in p):
                return node
        return None

    def focus(self, node):
        if self.node is not None:
            self.menu.host.wrap(self.node).set('_focused', False)
        self.node = node
        self.select_all = False
        if node is not None:
            target = self.menu.host.wrap(node)
            value = node.as2_text.get('text', '') if hasattr(node, 'as2_text') else self.menu.renderer.fields[node.character_id].get('initial_text', '')
            target.set('text', str(value))
            self.caret = len(str(value))
            target.set('_focused', True)
            target.set('_caret', self.caret)

    def active(self):
        if self.node is not None and (not self.menu.host.attached(self.node) or not visible(self.node)):
            self.focus(None)
        return self.node is not None

    def insert(self, value):
        if not self.active():
            return
        target = self.menu.host.wrap(self.node)
        old = str(get(target, 'text'))
        if self.select_all:
            old, self.caret = '', 0
        limit = self.menu.renderer.fields[self.node.character_id].get('max_length', 0)
        text = old[:self.caret] + value + old[self.caret:]
        if limit:
            text = text[:limit]
        self.caret = min(len(text), self.caret+len(value))
        self.select_all = False
        target.set('text', text); target.set('_caret', self.caret)

    def key(self, key, modifiers=0):
        if not self.active():
            return False
        import pygame
        target = self.menu.host.wrap(self.node)
        text = str(get(target, 'text'))
        if key == pygame.K_ESCAPE:
            self.focus(None)
        elif key == pygame.K_a and modifiers & pygame.KMOD_CTRL:
            self.select_all = True
        elif key in (pygame.K_BACKSPACE, pygame.K_DELETE):
            if self.select_all:
                self.insert('')
            elif key == pygame.K_BACKSPACE and self.caret:
                self.caret -= 1
                target.set('text', text[:self.caret]+text[self.caret+1:])
            elif key == pygame.K_DELETE:
                target.set('text', text[:self.caret]+text[self.caret+1:])
        elif key == pygame.K_LEFT:
            self.caret = max(0, self.caret-1)
        elif key == pygame.K_RIGHT:
            self.caret = min(len(text), self.caret+1)
        elif key == pygame.K_HOME:
            self.caret = 0
        elif key == pygame.K_END:
            self.caret = len(text)
        target.set('_caret', self.caret)
        return True
