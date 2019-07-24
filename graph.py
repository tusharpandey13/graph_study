# directed graph
class graph:
    def __init__(self):
        self._graph = {}

    def addnode(self, node, adjlist):
        self._graph[node] = adjlist

    def addedge(self, node1, node2):
        if node1 not in self._graph.keys():
            self._graph[node1] = [node2]
        else:
            self._graph[node1].append(node2)
            if node2 not in self._graph.keys():
                self._graph[node2] = []

    def print(self):
        for n in self._graph.keys():
            print(n, self._graph[n])
        pass

    def find_path(self, start, end, path=[]):
        path.append(start)
        # path = path + [start]
        # path += [start]
        # these modify the original path var
        # print(id(path), path) gives same id of path for all the recursions
        # makes you appreciate immutables
        if start == end:
            # path += [end]
            return path
        if start not in self._graph.keys():
            return None
        for n in self._graph[start]:
            if n not in path:
                tmp = self.find_path(n, end, path)
                if tmp is not None:
                    return tmp
        return None


g = graph()
g.addnode('a', [])
g.addedge('a', 'b0')
g.addedge('b0', 'c0')
g.addedge('c0', 'd0')
g.addedge('a', 'b1')
# g.addedge('a', 'c')
g.addedge('b1', 'c')
g.addedge('c', 'd')
g.addedge('d', 'e')

# g.print()
print(g.find_path('a', 'e'))
