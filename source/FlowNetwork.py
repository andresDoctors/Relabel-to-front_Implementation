from Arc import Arc
from Vertex import Vertex

class FlowNetwork:

    def __init__(self):
        self.s = None
        self.t = None
        self.vertexes = {}
        self.arcs = set()

    def set_st(self, stname, st):
        assert((st == 's' and self.s is None) or
               (st == 't' and self.t is None))

        if(stname not in self.vertexes): self.vertexes[stname] = Vertex(stname)
        if  (st == 's'): self.s = self.vertexes[stname]
        elif(st == 't'): self.t = self.vertexes[stname]

    def add_arc(self, xname, yname, cap):

        if xname not in self.vertexes:
            self.vertexes[xname] = Vertex(xname)
        if yname not in self.vertexes:
            self.vertexes[yname] = Vertex(yname)

        x = self.vertexes[xname]
        y = self.vertexes[yname]

        arc = Arc(x, y, cap)
        self.arcs.add(arc)
        if(x != self.t): x.adj_arcs.append(arc)
        if(y != self.s): y.adj_arcs.append(arc)

    def holds_flow_restrictions(self):
        s = self.s
        t = self.t

        res = True
        for x in self.vertexes.values():
            b1 = x.excess == 0 and x != s and x != t
            b2 = x.excess <= 0 and x == s
            b3 = x.excess >= 0 and x == t
            res = res and (b1 or b2 or b3)

        return res

    def pushfront(self, xy):
        x = xy.x
        y = xy.y

        assert(x.excess > 0)
        assert(xy.cap > xy.flow)
        assert(x.label == y.label + 1)
        xy += min(x.excess, xy.cap - xy.flow)

    def pushback(self, xy):
        x = xy.x
        y = xy.y

        assert(y.excess > 0)
        assert(xy.flow > 0)
        assert(y.label == x.label + 1)
        xy -= min(y.excess, xy.flow)

    def relabel(self, u):
        assert(u.excess > 0)

        min_label = float('inf')
        for xy in u.adj_arcs:
            assert(u == xy.x or u == xy.y)

            if(u == xy.x):
                if(xy.cap == xy.flow): continue
                v = xy.y

            elif(u == xy.y):
                if(xy.flow == 0): continue
                v = xy.x

            assert(u.label <= v.label)
            min_label = min(min_label, v.label)

        assert(min_label != float('inf'))
        u.label = min_label + 1

    def discharge(self, u):

        while(u.excess > 0):
            xy = u.current

            if(xy is None):
                self.relabel(u)
                u.head()

            else:

                assert(u == xy.x or u == xy.y)
                v    = xy.y             if u == xy.x else xy.x
                c    = xy.cap - xy.flow if u == xy.x else xy.flow
                push = self.pushfront   if u == xy.x else self.pushback

                if(c > 0 and u.label == v.label + 1): push(xy)
                else: u.next()

    def initialize(self):
        vertexes_values = self.vertexes.values()
        self.s.label = len(vertexes_values)
        for sy in self.s.adj_arcs: sy += sy.cap
        for u in vertexes_values: u.head()
        return [u for u in vertexes_values if u != self.s and u != self.t]

    def relabel_to_front(self):
        assert(self.s is not None)
        assert(self.t is not None)

        idx = 0
        L = self.initialize()
        while(idx < len(L)):
            u = L[idx]

            old_label = u.label
            self.discharge(u)
            if(u.label > old_label):
                L.insert(0, L.pop(idx))
                idx = 0

            else: idx += 1

    def print(self):

        print(f'p max {len(self.vertexes)} {len(self.arcs)}')
        print(f'n {self.s.name} s')
        print(f'n {self.t.name} t')
        for xy in self.arcs:
            print(f'a   {xy.x.name:<4}{xy.y.name:<4}{xy.flow:<4}{xy.cap}')
        print(f'{self.t.excess}')
        print(f'holds restrictions:{self.holds_flow_restrictions()}')
        for u in self.vertexes.values():
            print(f'u {u.name} {u.excess}')
