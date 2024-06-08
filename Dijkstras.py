from typing import List
import heapq

def createEmptyGraph(node_nbr):
    graph = []
    #graph = [] * node_nbr  # is disastrous because [] referes to the same object which will mess things up later when we try to add edges
    for e in range(node_nbr):
        graph.append([])
    return graph

def addEdge(adj: [], src: int, dest: int, weight: int):
    adj[src].append([weight, dest])

def dijkstra(adj: [[[]]], n: int): # adj: [[[]]]  ex [[[1, 0], [2, 1]]] where first element in 2-pair is the weight and the second element is the element. Returns a list with all number of steps. Unlike the previous one this also returns a dictionary with previous
    result = [100000] * len(adj)       #arbitrarily big, don't know how to represent infinity
    pred = dict()
    visited = [False] * len(adj)
    #q.remove(n)
    heap = []
    heapq.heappush(heap, [0, n, n])
    while heap:
        v = heapq.heappop(heap)
        n_nbr = v[1]
        prev_node = v[2]
        w = v[0]    #w for weight
        if not visited[n_nbr]:
            result[n_nbr] = w
            pred[n_nbr] = prev_node
            visited[n_nbr] = True
            for neighbor in adj[n_nbr]:        # Kolla om man kan göra detta snyggare med _ eller nåt.
                if not visited[neighbor[1]] and result[neighbor[1]] > result[n_nbr] + neighbor[0]:
                    heapq.heappush(heap, [result[n_nbr] + neighbor[0], neighbor[1], n_nbr])
    return result, pred

def dijkstra2(adj: [[[]]], n: int): # adj: [[[]]]  ex [[[1, 0], [2, 1]]], returns a list with all number of steps
    result = [100000] * len(adj)       #arbitrarily big, don't know how to represent infinity
    #q = [v for v in range(len(adj))]  # Saves all the vertices in Q
    #ska lägga till pred eller ändra result till att även ha med pred
    visited = [False] * len(adj)
    #q.remove(n)
    heap = []
    heapq.heappush(heap, [0, n])
    while heap:
        v = heapq.heappop(heap)
        n_nbr = v[1]
        w = v[0]
        if not visited[v[1]]:
            result[n_nbr] = w
            visited[n_nbr] = True
            for neighbor in adj[n_nbr]:        # Kolla om man kan göra detta snyggare med _ eller nåt.
                if not visited[neighbor[1]] and result[neighbor[1]] > result[n_nbr] + neighbor[0]:
                    heapq.heappush(heap, [result[n_nbr] + neighbor[0], neighbor[1]])
    return result

def main():
    graph = createEmptyGraph(9)
    addEdge(graph, 0, 1, 4)
    addEdge(graph, 0, 7, 8)
    addEdge(graph, 1, 2, 8)
    addEdge(graph, 1, 7, 11)
    addEdge(graph, 2, 3, 7)
    addEdge(graph, 2, 8, 2)
    addEdge(graph, 2, 5, 4)
    addEdge(graph, 3, 4, 9)
    addEdge(graph, 3, 5, 14)
    addEdge(graph, 4, 5, 10)
    addEdge(graph, 5, 6, 2)
    addEdge(graph, 6, 7, 1)
    addEdge(graph, 6, 8, 6)
    addEdge(graph, 7, 8, 7)
    result = dijkstra(graph, 0)
    print(result)

main()



