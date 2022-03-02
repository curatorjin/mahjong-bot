from receiver import MajSoul, Recorder
from concurrent.futures import ThreadPoolExecutor
from utils import MsgTunnel


def main():
    executors = ThreadPoolExecutor(max_workers=3)
    tunnel = MsgTunnel()
    app = MajSoul(tunnel)
    recorder = Recorder(tunnel)
    executors.submit(app.run)
    executors.submit(recorder.listen)


if __name__ == '__main__':
    main()
