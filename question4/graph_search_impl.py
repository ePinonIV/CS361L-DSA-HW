# Question 4 BFS and DFS Implementation - graph_search_impl.py

import queue
import time
import tracemalloc


# ---------- Graph Class for Adjecency List & Matrix  ----------

class Graph:
    def __init__(self, num_nodes, directed=False, type='list'):
        self.V = num_nodes
        self.E = 0 
        self.directed = directed   # bool to determing if directed or not
        # generalize adj_list to adj to it can be list or matrix
        self.type = type
        if self.type == 'list':
            self.adj = [[] for n in range(num_nodes)]
        elif self.type == 'matrix':
            self.adj = [[0 for n in range(num_nodes)] for n in range(num_nodes)]

    def add_edge(self, v1, v2):
        #
        if self.type == 'list':
            if v2 not in self.adj[v1]:
                self.adj[v1].append(v2)
                if not self.directed:
                    self.adj[v2].append(v1)
        #
        elif self.type == 'matrix':
            if self.adj[v1][v2] == 0:
                self.adj[v1][v2] = 1
                if not self.directed:
                    self.adj[v2][v1] = 1
        self.E += 1

    def explore(self, v):
        if self.type == 'list':
            return self.adj[v]
        elif self.type == 'matrix':
            neighbors = []
            for i in range(self.V):
                if self.adj[v][i] == 1:
                    neighbors.append(i)
            return neighbors


# ---------- Search and Wrapper Functions ----------


# breadth first search with queue taking graph class
def bfs(graph, start, target):
    q = queue.Queue()
    q.put([start])
    
    visited = {start}
    
    while not q.empty():
        path = q.get()
        curr = path[-1] # The last node in the current path
        
        if curr == target:
            return path
            
        for neighbor in graph.explore(curr):
            if neighbor not in visited:
                visited.add(neighbor)
                # Create a new path and add it to the queue
                new_path = list(path)
                new_path.append(neighbor)
                q.put(new_path)
    return None


# depth first search with stack taking graph class
def dfs(graph, start, target):
    stack = [[start]]
    visited = {start}
    
    while stack:
        path = stack.pop()
        curr = path[-1]
        
        if curr == target:
            return path
            
        # don't mark visited until pop usually, but mark during push more efficient and still works fine?
        for neighbor in graph.explore(curr):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
    return None


# wrapper to run with bfs/dfs for a given graph and find the run time and memory
def benchmark(algo, graph, start, target):
    times = []
    mem_usages = []
    
    for i in range(5):
        tracemalloc.start()

        start_time = time.perf_counter()
        path = algo(graph, start, target)
        end_time = time.perf_counter()

        i, peak_mem = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        times.append(end_time - start_time)
        mem_usages.append(peak_mem)
    
    avg_time = sum(times) / 5
    avg_mem = sum(mem_usages) / 5
    return path, avg_time, avg_mem


# ---------- Main Func to make graphs and run benchmarking  ----------


def main():
    print("-----------------------")

    # set up graphs (a) and (b) as adjacency lists and matricies

    a_list = Graph(12, False, "list")
    a_list.add_edge(0,2)
    a_list.add_edge(0,3)
    a_list.add_edge(0,7)
    a_list.add_edge(0,8)
    a_list.add_edge(1,2)
    a_list.add_edge(1,3)
    a_list.add_edge(1,4)
    a_list.add_edge(3,5)
    a_list.add_edge(4,6)
    a_list.add_edge(5,7)
    a_list.add_edge(6,9)
    a_list.add_edge(6,11)
    a_list.add_edge(8,10)
    a_list.add_edge(9,11)
    #print(a_list.adj)

    a_mat = Graph(12, False, "matrix")
    a_mat.add_edge(0,2)
    a_mat.add_edge(0,3)
    a_mat.add_edge(0,7)
    a_mat.add_edge(0,8)
    a_mat.add_edge(1,2)
    a_mat.add_edge(1,3)
    a_mat.add_edge(1,4)
    a_mat.add_edge(3,5)
    a_mat.add_edge(4,6)
    a_mat.add_edge(5,7)
    a_mat.add_edge(6,9)
    a_mat.add_edge(6,11)
    a_mat.add_edge(8,10)
    a_mat.add_edge(9,11)
    #print(a_mat.adj)

    # make map for graph (b) since it has alphabetical vertices
    char_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14}

    b_list = Graph(15, True, "list")
    b_list.add_edge(char_map['A'], char_map['B'])
    b_list.add_edge(char_map['A'], char_map['C'])
    b_list.add_edge(char_map['B'], char_map['D'])
    b_list.add_edge(char_map['B'], char_map['G'])
    b_list.add_edge(char_map['C'], char_map['D'])
    b_list.add_edge(char_map['D'], char_map['E'])
    b_list.add_edge(char_map['E'], char_map['F'])
    b_list.add_edge(char_map['E'], char_map['K'])
    b_list.add_edge(char_map['F'], char_map['G'])
    b_list.add_edge(char_map['F'], char_map['H'])
    b_list.add_edge(char_map['F'], char_map['M'])
    b_list.add_edge(char_map['G'], char_map['H'])
    b_list.add_edge(char_map['G'], char_map['N'])
    b_list.add_edge(char_map['G'], char_map['L'])
    b_list.add_edge(char_map['H'], char_map['I'])
    b_list.add_edge(char_map['I'], char_map['J'])
    b_list.add_edge(char_map['J'], char_map['H'])
    b_list.add_edge(char_map['J'], char_map['D'])
    b_list.add_edge(char_map['K'], char_map['F'])
    b_list.add_edge(char_map['K'], char_map['L'])
    # L doesn't go to anything
    b_list.add_edge(char_map['M'], char_map['O'])
    b_list.add_edge(char_map['N'], char_map['O'])
    # O doesn't go to anything
    #print(b_list.adj)

    b_mat = Graph(15, True, "matrix")
    b_mat.add_edge(char_map['A'], char_map['B'])
    b_mat.add_edge(char_map['A'], char_map['C'])
    b_mat.add_edge(char_map['B'], char_map['D'])
    b_mat.add_edge(char_map['B'], char_map['G'])
    b_mat.add_edge(char_map['C'], char_map['D'])
    b_mat.add_edge(char_map['D'], char_map['E'])
    b_mat.add_edge(char_map['E'], char_map['F'])
    b_mat.add_edge(char_map['E'], char_map['K'])
    b_mat.add_edge(char_map['F'], char_map['G'])
    b_mat.add_edge(char_map['F'], char_map['H'])
    b_mat.add_edge(char_map['F'], char_map['M'])
    b_mat.add_edge(char_map['G'], char_map['H'])
    b_mat.add_edge(char_map['G'], char_map['N'])
    b_mat.add_edge(char_map['G'], char_map['L'])
    b_mat.add_edge(char_map['H'], char_map['I'])
    b_mat.add_edge(char_map['I'], char_map['J'])
    b_mat.add_edge(char_map['J'], char_map['H'])
    b_mat.add_edge(char_map['J'], char_map['D'])
    b_mat.add_edge(char_map['K'], char_map['F'])
    b_mat.add_edge(char_map['K'], char_map['L'])
    # L doesn't go to anything
    b_mat.add_edge(char_map['M'], char_map['O'])
    b_mat.add_edge(char_map['N'], char_map['O'])
    # O doesn't go to anything
    #print(b_mat.adj)


    # benchmarking

    print(" --- Benchmarking graph (a) for path from vertex 0 to 7 --- ")
    # bfs on adj list for a
    path, t, mem = benchmark(bfs, a_list, 0, 7)
    print("BFS List: path = " + str(path) + ", time = " + str(t) + ", memory = " + str(mem) + " bytes")
    # dfs on adj list for a
    path, t, mem = benchmark(dfs, a_list, 0, 7)
    print("DFS List: path = " + str(path) + ", time = " + str(t) + ", memory = " + str(mem) + " bytes")

    # bfs on adj mat for a
    path, t, mem = benchmark(bfs, a_mat, 0, 7)
    print("BFS Matrix: path = " + str(path) + ", time = " + str(t) + ", memory = " + str(mem) + " bytes")
    # dfs on adj mat for a
    path, t, mem = benchmark(dfs, a_mat, 0, 7)
    print("DFS Matrix: path = " + str(path) + ", time = " + str(t) + ", memory = " + str(mem) + " bytes")


    print("\n --- Benchmarking graph (b) for path from vertex A to O --- ")
    # bfs on adj list for b
    path, t, mem = benchmark(bfs, b_list, char_map['A'], char_map['O'])
    print("BFS List: path = " + str(path) + ", time = " + str(t) + ", memory = " + str(mem) + " bytes")
    # dfs on adj list for b
    path, t, mem = benchmark(dfs, b_list, char_map['A'], char_map['O'])
    print("DFS List: path = " + str(path) + ", time = " + str(t) + ", memory = " + str(mem) + " bytes")

    # bfs on adj mat for b
    path, t, mem = benchmark(bfs, b_mat, char_map['A'], char_map['O'])
    print("BFS Matrix: path = " + str(path) + ", time = " + str(t) + ", memory = " + str(mem) + " bytes")
    # dfs on adj mat for b
    path, t, mem = benchmark(dfs, b_mat, char_map['A'], char_map['O'])
    print("DFS Matrix: path = " + str(path) + ", time = " + str(t) + ", memory = " + str(mem) + " bytes")


    print("-----------------------")


if __name__ == "__main__":
    main()