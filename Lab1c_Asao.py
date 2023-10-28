import networkx as nx
from queue import PriorityQueue

def a_star(graph, start_node, end_node):
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
            neighbor_cost = cost_table[current_node] + edge_data['g'] 
            heuristic_cost = edge_data['h']

            if neighbor_cost + heuristic_cost < cost_table[neighbor] + heuristic_cost:
                cost_table[neighbor] = neighbor_cost#cphi tích lũy mới từ nút xphat -> ke`
                parent_table[neighbor] = current_node# gán nút htai là nút cha của hxom
                queue.put((neighbor_cost + heuristic_cost, neighbor))
                
    if end_node not in parent_table:
        return None, float('inf')

    path = []
    node = end_node
    while node is not None:
        path.insert(0, node)
        node = parent_table[node]

    return path, cost_table[end_node]

# Tạo đồ thị
graph = nx.Graph()
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

path, cost = a_star(graph, start_node, end_node)

if path is None:
    print(f"Không có đường đi từ {start_node} đến {end_node}")
else:
    print(f"Đường đi ngắn nhất từ {start_node} đến {end_node}: {' -> '.join(path)}")
    print(f"Chi phí tương ứng: {cost}")