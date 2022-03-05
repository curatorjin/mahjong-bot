from .MajSoulMessage import MajSoulMessage

CHANG = ['东', '南', '西', '北']
PLAYER = ['自家', '下家', '对家', '上家']


class MajSoulGame(object):
    def __init__(self):
        self.account_id = 14156412
        self.gaming = False
        self.chang = 0
        self.ju = 1
        self.ben = 1
        self.offset = 0
        self.left_tiles_count = 0
        self.doras = []
        self.players = [
            {
                "hands": [],
                "table": [],
                "lu": [],
                "moqie": False,
                "liqi": False,
                "score": 25000,
            },
            {
                "table": [],
                "lu": [],
                "moqie": False,
                "liqi": False,
                "score": 25000,
            },
            {
                "table": [],
                "lu": [],
                "moqie": False,
                "liqi": False,
                "score": 25000,
            },
            {
                "table": [],
                "lu": [],
                "moqie": False,
                "liqi": False,
                "score": 25000,
            }
        ]

    def update_game(self, msg):
        msg = MajSoulMessage(msg)
        if msg.account_id:
            self.account_id = msg.account_id
            return
        if msg.ready_id_list:
            for i in range(0, len(msg.ready_id_list)):
                if msg.ready_id_list[i] == self.account_id:
                    self.offset = i
                    return
        if msg.chang is not None:
            self.gaming = True
            self.chang = msg.chang
            self.ju = msg.ju
            self.ben = msg.ben
            self.left_tiles_count = msg.left_tile_count
            self.players[0]['hands'] = msg.tiles
            self.doras = msg.doras
            return
        if msg.liujumanguan is not None:
            print("流局！")
            self.__handle_end(msg)
            return
        if msg.hules:
            print("胡了！")
            self.__handle_end(msg)
            return
        self.__handle_round(msg)

    def __handle_round(self, msg):
        if msg.seat is None:
            return
        if msg.doras:
            self.doras = msg.doras
        seat = self.__handle_offset(msg.seat)
        if msg.liqibang:
            self.players[seat]['liqi'] = True
            self.players[seat]['score'] = msg.score
            return
        self.__handle_card(msg, self.players[seat])

    def __handle_card(self, msg, player):
        if msg.left_tile_count:
            self.left_tiles_count = msg.left_tile_count
            if msg.tile:
                player['hands'].append(msg.tile)  # 摸牌
        elif msg.type is not None:  # 吃碰杠
            self.__handle_claiming(msg, player)
        elif msg.tile:
            player['table'].append(msg.tile)
            if 'hands' in player.keys():
                player['hands'].remove(msg.tile)

    def __handle_claiming(self, msg, player):
        op_type = msg.type
        if op_type == 0 or op_type == 1:  # 吃
            player['lu'].append(msg.tiles)
            if 'hands' in player.keys():
                for i in range(0, len(msg.froms)):
                    if self.__handle_offset(msg.froms[i]) == 0:
                        player['hands'].remove(msg.tiles[i])
        elif op_type == 2:
            if type(msg.tiles).__name__ == 'list':  # 明杠
                player['lu'].append(msg.tiles)
                if 'hands' in player.keys():
                    for tile in msg.tiles:
                        player['hands'].remove(tile)
            else:  # 加杠
                tile = msg.tiles
                for lu in player['lu']:
                    if lu.count(tile) == 3:
                        lu.append(tile)
                        break
                if 'hands' in player.keys():
                    player['hands'].remove(tile)
        elif op_type == 3:  # 暗杠
            player['lu'].append([msg.tiles, msg.tiles, msg.tiles, msg.tiles])
            if 'hands' in player.keys():
                for i in range(0, 4):
                    player['hands'].remove(msg.tiles)

    def __handle_end(self, msg):
        if msg.hules:
            for i in range(0, len(msg.scores)):
                player_index = self.__handle_offset(i)
                self.players[player_index]['score'] = msg.scores[i]
            for hu in msg.hules:
                seat = self.__handle_offset(hu['seat'])
                print(PLAYER[seat], '手牌:', hu['hand'])
                print('胡：', hu['hu_tile'])
        elif msg.liujumanguan is not None:
            for i in range(0, len(msg.players)):
                player_index = self.__handle_offset(i)
                player = msg.players[i]
                if player['tingpai']:
                    tings = []
                    for ting in player['tings']:
                        tings.append(ting['tile'])
                    print(PLAYER[player_index] + '听牌！', '手牌：' + player['hand'], '听：' + tings)
        for player in self.players:
            player['table'] = []
            player['lu'] = []
            player['moqie'] = False
            player['liqi'] = False
        self.gaming = False

    def __handle_offset(self, msg_index):
        return (msg_index + 4 - self.offset) % 4

    def show(self):
        if not self.gaming:
            return
        print(CHANG[self.chang] + str(self.ju + 1) + "局", str(self.ben + 1) + "本场", "余：" + str(self.left_tiles_count))
        print("上家：", self.players[3]['score'], "已立直" if self.players[3]['liqi'] else "")
        print("\t已出牌：", self.players[3]['table'])
        print("\t副露：", self.players[3]['lu'])
        print("对家：", self.players[2]['score'], "已立直" if self.players[2]['liqi'] else "")
        print("\t已出牌：", self.players[2]['table'])
        print("\t副露：", self.players[2]['lu'])
        print("下家：", self.players[1]['score'], "已立直" if self.players[1]['liqi'] else "")
        print("\t已出牌：", self.players[1]['table'])
        print("\t副露：", self.players[1]['lu'])
        print("本家：", self.players[0]['score'], "已立直" if self.players[0]['liqi'] else "")
        print("\t手牌：", self.players[0]['hands'])
        print("\t已出牌：", self.players[0]['table'])
        print("\t副露：", self.players[0]['lu'])
