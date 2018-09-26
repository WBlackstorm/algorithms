def dijkstra(graph, costs, parents, begin, end):
    proccessed = []
    node = get_cheapest_node(costs, proccessed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        proccessed.append(node)
        node = get_cheapest_node(costs, proccessed)

def get_cheapest_node(costs, proccessed):
    lowest_cost = float("inf")
    cheapest_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in proccessed:
            lowest_cost = cost
            cheapest_node = node
    return cheapest_node