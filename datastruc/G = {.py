G = {
    "start": {"A": 3, "C": 5, "D": 4},
    "A": {"B": 4},
    "B": {"end": 2},
    "C": {"B": 3, "end": 1},
    "D": {"C": 2, "end": 3}
}

C = {
    "A": 3,
    "B": float("inf"),
    "C": 5,
    "D": 4,
    "end": float("inf")
}

P = {
    "A": "start",
    "B": None,
    "C": "start",
    "D": "start",
    "end": None
}
    
def dijkstra(graph, costs, parents, start, end):
    pass

print(dijkstra(G, C, P, "start", "end"))