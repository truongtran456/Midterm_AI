import networkx as nx
from queue import PriorityQueue

def greedy(graph, start_node, end_node):
    queue = PriorityQueue()
    queue.put((0, start_node))

    cost_table = {node: float('inf') for node in graph.nodes}
    cost_table[start_node] = 0

    parent_table = {start_node: None}

    while not queue.empty():
        cost, current_node = queue.get()

        if current_node == end_node:
            break

        for neighbor in graph.neighbors(current_node):
            edge_data = graph.edges[current_node, neighbor]
            parent_table[neighbor] = current_node
            g_cost = edge_data['g']
            h_cost = edge_data['h']
            cost_table[neighbor] = cost_table[current_node] + g_cost 
            queue.put((h_cost, neighbor))

    if end_node not in parent_table:
        return None, float('inf')

    path = []
    node = end_node
    while node != None:
        path.insert(0, node)
        node = parent_table[node]

    return path, cost_table[end_node]

graph = nx.DiGraph()
graph.add_nodes_from(['S', 'A', 'B', 'C', 'D', 'G'])
graph.add_edges_from([
    ('S', 'A', {'g': 3, 'h': 9}),
    ('S', 'B', {'g': 5, 'h': 7}),
    ('S', 'C', {'g': 9, 'h': 8}),
    ('A', 'D', {'g': 1, 'h': 4}),
    ('B', 'D', {'g': 2, 'h': 4}),
    ('C', 'G', {'g': 3, 'h': 0}),
    ('D', 'C', {'g': 2, 'h': 8}),
    ('D', 'G', {'g': 4, 'h': 0}),
])

start_node = 'S'
end_node = 'G'

path, cost = greedy(graph, start_node, end_node)

if cost == 0:
  print(f"Không có đường đi từ {start_node} đến {end_node}")
else:
  print(f"Đường đi ngắn nhất từ {start_node} đến {end_node}: {' -> '.join(path)}")
  print(f"Chi phí tương ứng: {cost}")
  
  