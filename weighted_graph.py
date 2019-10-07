import graph


class weighted_graph(graph.graph):
    def __init__(self, w_adj={}):
        if not len(w_adj):
            super().__init__()
        else:
            tmpg = {}
            for e in w_adj:
                tmpl = []
                for e1 in w_adj[e]:
                    tmpl.append(e1[0])
                tmpg[e] = tmpl
            super().__init__(tmpg)
        self.w_adj = w_adj

    def print(self):
        super().print(self.w_adj)

    def dfs(self):
        return super().dfs()

    # def topological_sort(self):


# w = weighted_graph({'a': [('b', 10), ('c', 3)],
#                     'b': [('c', 1), ('d', 2)],
#                     'c': [('d', 8), ('e', 2), ('b', 4)],
#                     'd': [('e', 7)],
#                     'e': [('d', 9)]})
w = weighted_graph({'a': [('c', 1)],
                    'b': [('c', 2)],
                    'c': [],
                    'd': [('a', 1)],
                    'e': [('a', 1)],
                    'f': [('b', 1)],
                    'g': [('b', 1)]})

# w.print()
print(w.topological_sort())
# g.print()
