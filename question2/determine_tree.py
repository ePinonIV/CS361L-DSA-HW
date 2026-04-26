# Code to implement algorithm finding if a graph is a tree
# Given undirected simple graph G(V,E), determine if its a tree or not

import queue

class Graph:
    def __init__(self, num_nodes):
        self.V = num_nodes
        self.E = 0 
        self.adj_list = [[] for n in range(num_nodes)] 

    def add_edge(self, v1, v2):
        if v2 not in self.adj_list[v1]:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            self.E += 1

       
def is_tree(G):
    # first check if has V-1 edges
    # and edge case for very small graph
    if G.E != G.V - 1 or G.V <= 1:
        return False

    # now do bfs to check for cycle
    visited = set()
    q = queue.Queue()

    q.put((0, -1))
    visited.add(0)

    while not q.empty():
        curr, parent = q.get()

        for neighbor in G.adj_list[curr]:
            if neighbor == parent:
                continue

            if neighbor in visited:
                return False
            
            visited.add(neighbor)
            q.put((neighbor, curr))

    hit_all = False
    if len(visited) == G.V:
        hit_all = True

    return hit_all

    
# -------------------------

# run test cases

# simple tree with root 0 and 4 childen -> valid tree
ex_G1 = Graph(5)
ex_G1.add_edge(0, 1)
ex_G1.add_edge(1, 2)
ex_G1.add_edge(0, 2)
ex_G1.add_edge(0, 3)
ex_G1.add_edge(0, 4)

G1_result = is_tree(ex_G1)
print("Example graph G1 is a tree? " + str(G1_result))

# add cross edge
ex_G2 = Graph(5)
ex_G2.add_edge(0, 1)
ex_G2.add_edge(1, 2)
ex_G2.add_edge(2, 3)
ex_G2.add_edge(3, 4)
ex_G2.add_edge(4, 0)

G2_result = is_tree(ex_G2)
print("Example graph G2 is a tree? " + str(G2_result))