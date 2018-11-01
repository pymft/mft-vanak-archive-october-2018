import time


class Timer:
    def __init__(self):
        self.start = None
        self.stop = None

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args):
        self.stop = time.time()
        t = self.stop - self.start

        print("start:{}\nstop :{}\nelapsed time : {} sec".format(
            self.start, self.stop, t))


with Timer() as t:
    s = 0.0
    for i in range(100000):
        s+= i

