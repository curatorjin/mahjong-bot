import json


class Recorder(object):
    def __init__(self, msg_tunnel):
        self.__msg_tunnel = msg_tunnel
        self.__scores = [25000, 25000, 25000, 25000]
        self.__current = []
        self.__table = {"p0": [],
                        "p1": [],
                        "p2": [],
                        "p3": [],
                        "dora": [],
                        "lichi": [False, False, False, False]}

    def listen(self):
        while True:
            msg = self.__msg_tunnel.pop_msg()
            self.__handle(msg)

    def __record(self, info):
        info = json.loads(info)
        if "chang" in info.keys():
            self.__clear()
            self.__current = [info["chang"], info["ju"], info["ben"]]
            self.__table["dora"].extend(info["doras"])
            return
        if "seat" in info.keys():
            op = 'p' + str(info["seat"])
            if "tile" in info.keys():
                self.__table[op].append(info["tile"])

    def __clear(self):
        self.__init__()

    def __show(self):
        print("===" + str(self.__current) + "===")
        print(self.__table)
        print(self.__scores)
        print(8 * "=")

    def __handle(self, msg):
        self.__show()
        # todo 增加对请求的处理
        print(msg)
