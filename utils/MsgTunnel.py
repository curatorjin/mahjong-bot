class MsgTunnel(object):
    def __init__(self):
        self._queue = []

    def pop_msg(self):
        if len(self._queue) > 0:
            return self._queue.pop()
        while True:
            if len(self._queue) > 0:
                return self._queue.pop()

    def push_msg(self, msg):
        self._queue.append(msg)
