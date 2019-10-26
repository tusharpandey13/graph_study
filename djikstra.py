from pqdict import PQDict

graph = {'a': {'b': 1},
         'b': {'c': 2, 'b': 5},
         'c': {'d': 1},
         'd': {}}

# 1 level in gives dict of neighbours
# 2 levels in gives distance always

# For any directed edge `v -> w`, `G[v][w]`
# is the length of the edge from `v` to `w`.


def dijkstra(G, src, dst=None):
    inf = float('inf')
    D = {src: 0}                                # distance
    Q = PQDict(D)                               # priority queue
    P = {}                                      # predecessor
    U = set(G.keys())                           # unexplored nodes

    while U:                                    # still have unexplored
        (v, d) = Q.popitem()                    # get node with least d
        D[v] = d                                # add to D dict
        U.remove(v)                             # node now explored
        if v == dst:                            # reached destination
            break

        # now edges FROM v
        for w in G[v]:
            if w in U:                          # unvisited neighbour
                tmpd = D[v] + G[v][w]
                if tmpd < Q.get(w, inf):        # return inf if not found
                    Q[w] = tmpd                 # update distance
                    P[w] = v                    # set predecessor as current
    return D, P


print(dijkstra(graph, 'a'))


def shortest_path(graph, src, dest):
    _, P = dijkstra(graph, src, dest)
    tmpl = [dest]
    tmp = dest
    while (tmp != src):
        tmp = P[tmp]
        tmpl.append(tmp)
    return list(reversed(tmpl))


print(shortest_path(graph, 'a', 'd'))
