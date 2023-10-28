def is_safe(graph, v, c, color):
    for i in range(len(graph)):   
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def graph_coloring(graph, m, v, color):
    if v == len(graph):
        return True

    for c in range(1, m + 1):
        if is_safe(graph, v, c, color):
            color[v] = c 
            if graph_coloring(graph, m, v + 1, color):
                return True
            color[v] = 0

    return False

def print_solution(graph, color):
    for i in range(len(graph)):
        print("Khu vực {} được tô màu màu {}.".format(i + 1, color[i]))

def solve_graph_coloring(graph, m):
    n = len(graph) 
    color = [0] * n 
#tức là c lúc này =0, mà nếu màu =0 tức là chưa được tô màu 
    if not graph_coloring(graph, m, 0, color): 
        print("Không tìm thấy lời giải.")
        return False
    print("Lời giải:")
    print_solution(graph, color)
    return True

graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 1, 0]
]

m = 3

solve_graph_coloring(graph, m)