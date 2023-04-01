class Arc:

    def __init__(self, x, y, cap):
        self.x = x
        self.y = y
        self.cap = cap
        self.flow = 0

    def __iadd__(self, quantity):
        self.flow += quantity
        assert(0 <= self.flow and self.flow <= self.cap)
        self.y.excess += quantity
        self.x.excess -= quantity

    def __isub__(self, quantity):
        self.flow -= quantity
        assert(0 <= self.flow and self.flow <= self.cap)
        self.y.excess -= quantity
        self.x.excess += quantity
