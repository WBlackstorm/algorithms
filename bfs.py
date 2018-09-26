from collections import deque

def bfs(graph, begin, end):
    search_queue = deque()
    search_queue += graph[begin]
    proccessed = [begin]

    while search_queue:
        node = search_queue.popleft()
        if not node in proccessed:
            if node == end:
                proccessed.append(node)
                print(proccessed)
                return
            else:
                search_queue += graph[node]
                proccessed.append(node)    


graph = {}
graph['twin'] = ['a', 'b']
graph['a'] = ['d']
graph['b'] = ['c', 'e']
graph['c'] = ['d']
graph['e'] = ['d']
graph['d'] = ['golden']

bfs(graph, 'twin', 'golden')