class MinStack:
    def __init__(self):
        self.s = []
        self.m = []

    def push(self, v: int) -> None:
        self.s.append(v)
        if self.m:
            v = min(v, self.m[-1])
        self.m.append(v)

    def pop(self) -> None:
        self.s.pop()
        self.m.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.m[-1]
