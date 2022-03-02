from flask import Flask, request
from flask_cors import cross_origin


class MajSoul(Flask):
    def __init__(self, msg_tunnel):
        super().__init__(__name__)
        self.msg_tunnel = msg_tunnel
        self.add_url_rule('/', 'push_msg', self.receive_msg, methods=['POST'])

    @cross_origin()
    def receive_msg(self):
        self.msg_tunnel.push_msg(request.data)
        return ""

    def run(self):
        super().run('0.0.0.0', 12121, ssl_context='adhoc')
