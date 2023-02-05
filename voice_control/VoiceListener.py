from speech_recognition import Microphone


class VoiceListener(object):
    def __init__(self):
        self.__mic = Microphone()

    def listen(self):
        with self.__mic as source:
            with open('out.wav', 'wb') as f:
                f.write(source)
