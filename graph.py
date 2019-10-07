# directed acyclic graph
class graph:
    def __init__(self, adj={}):
        self.adj = adj

    def setgraph(self, adj):
        self.adj = adj

    def addnode(self, node, adjlist):
        self.adj[node] = adjlist
        for e in adjlist:
            if e not in self.adj.keys():
                self.addnode(e, [])

    def addedge(self, node1, node2):
        if node1 not in self.adj.keys():
            self.adj[node1] = [node2]
        else:
            self.adj[node1].append(node2)
            if node2 not in self.adj.keys():
                self.adj[node2] = []

    def print(self, adj=None):
        if adj is None:
            print(self.adj)
        else:
            print(adj)
        # for n in self.adj.keys():
        #     print(n, self.adj[n])
        # pass

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
        if start not in self.adj.keys():
            return None
        for n in self.adj[start]:
            if n not in path:
                tmp = self.find_path(n, end, path)
                if tmp is not None:
                    return tmp
        return None

    def dfs_r(self, S, time, count):
        if S not in time:
            for u in self.adj[S]:
                if u not in time:
                    self.dfs_r(u, time, count)
            count[0] += 1
            # print("  ", S, count[0])
            time[S] = count[0]

    # TODO: return parents
    def dfs(self):
        time = {}
        count = [0]
        for v in list(self.adj.keys()):
            # print(v)
            self.dfs_r(v, time, count)
        return time

    def topological_sort(self):
        return sorted(self.dfs().items(), key=lambda x: x[1], reverse=True)
