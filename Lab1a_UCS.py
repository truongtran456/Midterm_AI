import networkx as nx
from queue import PriorityQueue

def ucs(graph, start_node, end_node):
    queue = PriorityQueue()
    queue.put((0, start_node)) 

    cost_table = {node: float('inf') for node in graph.nodes}
    cost_table[start_node] = 0

    parent_table = {start_node: None}

    while not queue.empty():
        cost, current_node = queue.get()

        if cost > cost_table[current_node]:
            # Nếu có chi phí > chi phí đã có trong O thì bỏ qua
            continue

        if current_node == end_node:
            break

        for neighbor in graph.neighbors(current_node):
            # Tính toán cost tới nút kề
            neighbor_cost = cost + graph.edges[current_node, neighbor]['g']

            if neighbor_cost < cost_table[neighbor]:
                cost_table[neighbor] = neighbor_cost
                parent_table[neighbor] = current_node
                queue.put((neighbor_cost, neighbor))

    return parent_table, cost_table


graph = nx.Graph()
graph.add_nodes_from(['S', 'A', 'B', 'C', 'D', 'G'])
graph.add_edges_from([
    ('S', 'A', {'g': 3}),
    ('S', 'B', {'g': 5}),
    ('S', 'C', {'g': 9}),
    ('A', 'D', {'g': 1}),
    ('B', 'D', {'g': 2}),
    ('C', 'G', {'g': 3}),
    ('D', 'C', {'g': 2}),
    ('D', 'G', {'g': 4}),
])

start_node = 'S'
end_node = 'G'

parent_table, cost_table = ucs(graph, start_node, end_node)

if end_node not in parent_table:
    print(f"Không có đường đi từ {start_node} đến {end_node}")
else:
    path = []
    node = end_node
    while node is not None:
        path.insert(0, node)
        node = parent_table[node]
    print(f"Đường đi ngắn nhất từ {start_node} đến {end_node}: {' -> '.join(path)}")
    print(f"Chi phí tương ứng: {cost_table[end_node]}")