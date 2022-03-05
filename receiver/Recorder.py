from .MajSoulGame import MajSoulGame


class Recorder(object):
    def __init__(self, msg_tunnel):
        self.__msg_tunnel = msg_tunnel
        self.game = MajSoulGame()

    def listen(self):
        while True:
            msg = self.__msg_tunnel.pop_msg()
            self.game.update_game(str(msg, 'utf-8'))
            self.game.show()
