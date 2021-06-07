
import heapq as hq
import random

graph = {
    'A': {'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0},
    'B': {'A': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0},
    'C': {'A': 0, 'B': 0, 'D': 0, 'E': 0, 'F': 0},
    'D': {'A': 0, 'B': 0, 'C': 0, 'E': 0, 'F': 0},
    'E': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0},
    'F': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
}

for i in graph:
    for v in graph[i]:
        graph[i][v] = random.randint(0, 10)

def dijkstra(G, src, dest):
    dist = {} # initializing our distances dict

    for v in G:
        dist[v] = float('inf') # for every vertex within the G(raph) parameter, set vertex value to infinity
        
    dist[src] = 0 # setting the source point to 0
    Q = [(0,src)] # so here i am creating the queue array and adding the first item, or the starting node, to the queue

    while len(Q) > 0:
        u, curr = hq.heappop(Q) # setting current and minimum disance (u) / corresponding current vertex (curr)

        if u > dist[curr]: # if current distance is greater than the value we have for dist[current_vertex] then just continue
            continue
        for v, w in G[curr].items():
            d = u + w # (d) is equal to the current distance plus the weight of the current item in G that we are iterating over

            if d < dist[v]: # if d (cirrent distance + weight) is less than the dist[v of G[curr]]), assign dist[v] value to d and push d/v to the queue
                dist[v] = d
                hq.heappush(Q, (d, v))
    return 'Distance from {} to {} is {}'.format(src, dest, dist[dest])

print(graph)

start_point = input('Enter source point (A-F):  ')
end_point = input('Enter destination point (A-F):   ')

print(dijkstra(graph, start_point, end_point))