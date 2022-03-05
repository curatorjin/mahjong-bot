import json


class MajSoulMessage(object):
    def __init__(self, msg):
        info = json.loads(msg)
        self.account_id = info.get('account_id')
        self.friends = info.get('friends')
        self.record_list = info.get('record_list')
        self.shared_record_base_info = info.get('shared_record_base_info')
        self.current_record_uuid = info.get('current_record_uuid')
        self.record_actions = info.get('record_actions')
        self.record_click_action = info.get('record_click_action')
        self.record_click_action_index = info.get('record_click_action_index')
        self.fast_record_to = info.get('fast_record_to')
        self.live_head = info.get('live_head')
        self.live_fast_action = info.get('live_fast_action')
        self.live_action = info.get('live_action')
        self.change_seat_to = info.get('change_seat_to')
        self.sync_game_actions = info.get('sync_game_actions')
        self.is_game_start = info.get('is_game_start')
        self.seat_list = info.get('seat_list')
        self.ready_id_list = info.get('ready_id_list')
        self.game_config = info.get('game_config')
        self.md5 = info.get('md5')
        self.chang = info.get('chang')
        self.ju = info.get('ju')
        self.ben = info.get('ben')
        self.tiles = info.get('tiles')
        self.dora = info.get('dora')
        self.liqibang = info.get('liqibang')
        self.score = info.get('score')
        self.scores = info.get('scores')
        self.seat = info.get('seat')
        self.tile = info.get('tile')
        self.doras = info.get('doras')
        self.left_tile_count = info.get('left_tile_count')
        self.is_liqi = info.get('is_liqi')
        self.is_wliqi = info.get('is_wliqi')
        self.moqie = info.get('moqie')
        self.operation = info.get('operation')
        self.type = info.get('type')
        self.froms = info.get('froms')
        self.hules = info.get('hules')
        self.liujumanguan = info.get('liujumanguan')
        self.players = info.get('players')
        self.gameend = info.get('gameend')

    def classify_situation(self):
        if self.chang:
            return "ActionNewRound"
        if self.liujumanguan:
            return "BlankEnd"
        if self.hules:
            return "End"
        if self.seat:
            if self.type:
                return "OtherOperation"
            pass
