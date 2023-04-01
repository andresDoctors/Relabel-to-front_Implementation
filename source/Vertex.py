class Vertex:

    def __init__(self, name):
        self.name = name
        self.excess = 0
        self.label = 0
        self.adj_arcs = []

        self.idx = None
        self.current = None

    def head(self):
        self.idx = 0
        self.current = self.adj_arcs[0]

    def next(self):
        self.idx += 1
        try: self.current = self.adj_arcs[self.idx]
        except Exception: self.current = None
