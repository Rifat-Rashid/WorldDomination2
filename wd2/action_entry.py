"""Original action presenters connected to the live host and existing game model.

The recovered presenters own action validation, costs and TurnAction creation.
This boundary supplies pointer dispatch and presentation-only city bindings.
"""
from .runtime import U, get, truth, number, obj, ASFunction


def control_path(node):
    parts = []
    while node.parent:
        parts.append(node.name or f'#{node.depth}')
        node = node.parent
    return '/'.join(reversed(parts))


def visible(node):
    while node:
        if not node.visible:
            return False
        node = node.parent
    return True


class ActionEntry:
    def __init__(self, scene):
        self.scene, self.game = scene, scene.game
        self.rt, self.host = scene.rt, scene.host
        self.model, self.human = self.game.model, self.game.human
        self.presenter, self.hud = scene.presenter, scene.hud
        self.source_update = get(self.presenter, 'updateView')
        self.source_research = get(self.presenter, 'loadResearchFunc')
        self.presenter.set('loadResearchFunc', self.load_research)
        self.source_accept = get(self.presenter, 'btnPressed_accept')
        self.source_tube = get(self.presenter, 'btnPressed_tube')
        self.presenter.set('btnPressed_accept', self.accept)
        self.presenter.set('btnPressed_tube', self.tube)
        self.presenter.set('updateView', self.update)
        # Confirm deliberately retains the synchronous engine's casualty boundary.
        self.presenter.set('btnPressed_turn', scene.resolve)
        interface_model = self.rt.new('Model_interface')
        self.rt.globals.set('model_interface', interface_model)
        self.presenter.set('model_interface', interface_model)
        self.hud.set('model_interface', interface_model)
        self.hovered = None
        self.markers = {}
        self.rt.invoke(self.model, 'resetUserSelections')
        self.model.set('view_leader_MCs_played', 'done')
        get(self.rt.globals, 'view').set('remove_city_popups', lambda: U)

    def accept(self):
        ta = self.rt.invoke(self.human, 'getNextTurnAction')
        funds = number(get(self.human, 'turnMoney'))
        self.rt.call(self.source_accept, self.presenter, [])
        if truth(ta) and truth(get(ta, 'action')):
            ta.set('_entry_cost', funds-number(get(self.human, 'turnMoney')))

    def tube(self, button):
        ta = get(button, 'associatedTA')
        action, cost = get(ta, 'action'), get(ta, '_entry_cost')
        funds = number(get(self.human, 'turnMoney'))
        self.rt.call(self.source_tube, self.presenter, [button])
        if truth(action) and not truth(get(ta, 'action')) and cost is not U:
            # Source production reserves rounded total money but refunds the
            # fractional slider sum. Refund exactly the amount actually reserved.
            self.human.set('turnMoney', funds + number(cost))
            ta.delete('_entry_cost')
            self.update()

    def load_research(self, error=U):
        self.rt.call(self.source_research, self.presenter, [error])
        if truth(error):
            return
        # The recovered loop retains _loc8_ from the previous group when this
        # group is complete. A completed box must never buy that other group.
        center = get(self.scene.interface, 'centerScreen')
        groups = get(self.model, '_userSelectedResearchInvestmentArr')
        for index in range(1, 8):
            box = get(center, f'tech{index}')
            candidate = get(get(box, '_obj'), '_tech')
            if candidate is U or get(candidate, 'desireGroup') != groups[index][2] or truth(get(candidate, 'invented')):
                box.set('_obj', obj({'_tech': U, '_mc': box}))
                self.rt.invoke(box, 'gotoAndStop', 'allInvented')
                text = get(box, 'text1')
                if text is not U:
                    text.set('text', ' -- ')

    def update(self):
        # Source updateCities is the existing headless effect; it must not read
        # City.size_and_frame or replay battle callbacks on presentation ticks.
        self.rt.call(self.source_update, self.presenter, [])
        get(self.scene.interface, 'btn46').set('onPress', self.scene.resolve)
        self.sync_cities()

    def after_turn(self):
        for ta in get(self.human, 'turnActionArr'):
            ta.delete('_entry_cost')
        self.model.set('view_leader_MCs_played', 'done')
        self.presenter.set('blockAllBtns', False)
        self.presenter.set('block_start_btn', False)
        self.rt.invoke(self.presenter, 'removeBioClips')
        self.rt.invoke(self.presenter, 'attachBioClips')
        self.rt.invoke(self.presenter, 'resetBtns')

    def sync_cities(self):
        from .original_gameplay import color_object
        from .generated.View import f_16 as show_population, f_17 as hide_population
        get(self.rt.globals,'view').set('currentViewType','interface')
        for player in self.game.players:
            for city in get(player, 'cityArr'):
                cid = get(city, 'cityID')
                clip = self.scene.city_clips.get(cid)
                if clip is None:
                    continue
                clip.set('onPress', lambda c=city: self.select_city(c))
                self.rt.invoke(get(clip,'mc'),'gotoAndStop',get(get(get(city,'image'),'mc'),'_currentframe'))
                if player is self.human:
                    clip.set('population',get(city,'population'))
                    clip.set('onRollOver',ASFunction(show_population))
                    clip.set('onRollOut',ASFunction(hide_population))
                selection = get(city, 'selectionObj')
                icons = []
                if truth(get(selection, 'attack')):
                    icons.append('soldier')
                if truth(get(selection, 'preAttack')):
                    name = get(selection, 'preAttackWeapon')
                    icons.append('rocket' if str(name).startswith('rocket') else
                                 'plane' if str(name).startswith('plane') else 'special')
                if truth(get(selection, 'propaganda')):
                    icons.append('propaganda')
                icons.extend(['special'] * int(number(get(selection, 'shipCount'))))
                signature = tuple(icons)
                old = self.markers.get(cid)
                if old and old[0] != signature:
                    self.rt.invoke(old[1], 'removeMovieClip')
                    del self.markers[cid]
                if icons and cid not in self.markers:
                    marker = self.rt.invoke(self.scene.battle, 'attachMovie',
                        'map_icon_crosshair', f'crosshair{cid}', get(city, 'image_depth') + 1500)
                    marker.set('_x', get(city, 'xPos'))
                    marker.set('_y', get(city, 'yPos') - 25)
                    marker.set('_xscale', 200)
                    marker.set('_yscale', 200)
                    children = []
                    for index, icon in enumerate(icons):
                        child = self.rt.invoke(marker, 'attachMovie', 'map_icon_' + icon,
                                               f'icon{index}', index + 1)
                        children.append(child)
                        child.set('_y', 25)
                    widths = [number(get(child, '_width')) for child in children]
                    x = -sum(widths)/2
                    for child, width in zip(children, widths):
                        child.set('_x', x)
                        x += width
                    self.markers[cid] = (signature, marker)
                palette = '_default'
                if not icons:
                    if truth(get(city, 'hideForSelection')):
                        palette = 'city_red'
                    elif truth(get(city, 'showForSelection')) and number(get(city, 'population')) > 0:
                        palette = 'city_green'
                self.rt.invoke(color_object(clip), 'setTransform', get(get(self.model, 'wd_colors'), palette))

    def select_city(self, city):
        # Only a chosen, available payload makes a ship's next target selectable.
        if (get(self.model, 'userSelectedActionBtn') == 'preAttack'
                and get(get(self.model, 'userSelectedCarrier'), 'weaponName') == 'ship'
                and (not truth(get(self.model, 'userSelectedWeapon'))
                     or len(get(self.model, 'ship_attack_arr')) >= 3)):
            return
        self.rt.invoke(self.game.presenter, 'citySelect', city)

    def reconcile_reservations(self):
        """Source reset handlers clear inUse; preserve reservations in other slots."""
        stock = get(self.human, 'weaponStock')
        counts = {}
        def reserve(weapon):
            if weapon is not U:
                counts[weapon] = counts.get(weapon, 0) + 1
        for ta in get(self.human, 'turnActionArr'):
            if not truth(get(ta, 'action')):
                continue
            reserve(get(ta, 'attackWeapon'))
            if get(self.human, 'preAttackStatus') != 'ready':
                reserve(get(ta, 'preAttackCarrier'))
            reserve(get(ta, 'preAttackPayload'))
            for assignment in get(ta, 'ship_attack_arr') if get(ta, 'ship_attack_arr') is not U else []:
                reserve(self.rt.invoke(stock, 'getWeaponByID', get(assignment, 'wpn')))
        for assignment in get(self.model, 'ship_attack_arr'):
            reserve(self.rt.invoke(stock, 'getWeaponByID', get(assignment, 'wpn')))
        if not (get(self.model, 'userSelectedActionBtn') == 'preAttack'
                and get(get(self.model, 'userSelectedCarrier'), 'weaponName') == 'ship'):
            reserve(get(self.model, 'userSelectedWeapon'))
        for weapon in get(stock, 'weaponArr'):
            weapon.set('inUse', counts.get(weapon, 0))
        for button in get(self.hud, 'stockBtn_arr'):
            if button is not U:
                weapon = self.rt.invoke(stock, 'getWeaponByName', get(button, 'relatedWeapon'))
                button.set('stockAmount', number(get(weapon, 'inStock'))-number(get(weapon, 'inUse'))
                           if truth(get(weapon, 'active')) else -1)

    def controls(self):
        nodes = []
        # Display order gives nested center controls priority over the HUD and map.
        for root in (self.scene.battle.node, self.scene.interface.node):
            for node in root.walk():
                if visible(node) and any(get(self.host.wrap(node), event) is not U
                                        for event in ('onPress', 'onRollOver')):
                    nodes.append(node)
        return nodes

    def find(self, name):
        nodes = self.controls()
        return next((n for n in reversed(nodes) if control_path(n) == name), None) or next(
            (n for n in reversed(nodes) if n.name == name), None)

    def press(self, name):
        node = self.find(name)
        if node is None or not truth(get(self.human, 'alive')):
            return U
        if truth(get(self.human, 'diplomacyPendingArr')[0]):
            center = get(self.scene.interface, 'centerScreen').node
            if node not in list(center.walk()) and node.name not in ('btn38', 'btn39'):
                return U
        result = self.host.dispatch(node, 'onPress')
        self.reconcile_reservations()
        self.sync_cities()
        return result

    def control_at(self, pos, renderer):
        center = get(self.scene.interface, 'centerScreen').node
        target_frames = {1} | {center.symbol.timeline.labels[name] for name in
                         ('attack1', 'preAttack4', 'propaganda1')}
        for node in reversed(self.controls()):
            if node.parent is self.scene.battle.node and center.frame not in target_frames:
                continue  # An opaque action panel must not click through to cities.
            bounds = renderer.control_bounds(node)
            if bounds and bounds[0] <= pos[0] <= bounds[2] and bounds[1] <= pos[1] <= bounds[3]:
                return control_path(node)
        return None

    def motion(self, pos, renderer):
        self.host.mouse_event('onMouseMove', pos)
        name = self.control_at(pos, renderer)
        node = self.find(name) if name else None
        if node is not self.hovered:
            if self.hovered and self.host.attached(self.hovered):
                self.host.dispatch(self.hovered, 'onRollOut')
            if node:
                self.host.dispatch(node, 'onRollOver')
            self.hovered = node
