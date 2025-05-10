import time


class TimeCounter:
    def __init__(self):
        self.H, self.M, self.S = 0, 0, 0
        self.Call()

    def Call(self):
        while True:
            self.Timer()
            time.sleep(1)

    def Timer(self):
        TF = '{:02d}:{:02d}:{:02d}'.format(self.H, self.M, self.S)
        print(TF)
        self.S += 1
        if self.S >= 60:
            self.M += 1
            self.S = 0
        if self.M >= 60:
            self.H += 1
            self.M = 0


cls = TimeCounter()