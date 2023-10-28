import heapq

def ucs(graph, start):
    visited = set()
    queue = [(0, [start])]
    
    while queue:
        (cost, path) = heapq.heappop(queue)
        node = path[-1]
        
        if node not in visited:
            visited.add(node)
            
            if len(visited) == len(graph):
                # Tất cả các nút đã được duyệt, quay trở về nút ban đầu
                path.append(start)
                return path, cost
            
            for neighbor, neighbor_cost in graph.get(node, {}).items():
                if neighbor not in visited:
                    new_cost = cost + neighbor_cost
                    new_path = path + [neighbor]
                    heapq.heappush(queue, (new_cost, new_path))
    
    return None, float('inf')

def tsp(graph, start):
    # Dùng UCS để tìm đường đi ngắn nhất bắt đầu từ nút start
    path, cost = ucs(graph, start)
    
    if path is None:
        return None, float('inf')
    
    return path, cost

# Biểu diễn đồ thị dưới dạng từ điển
graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

start_node = 'A'
path, cost = tsp(graph, start_node)

if path:
    print("Đường đi TSP:", ' -> '.join(path))
    print("Chi phí:", cost)
else:
    print("Không có đường đi TSP.")