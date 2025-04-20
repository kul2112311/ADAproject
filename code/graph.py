import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self):
        self.adj = {}  # adjacency list {vertex: set(neighbors)}
    
    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = set()
    
    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].add(v)
        self.adj[v].add(u)

    # remove vertices not in any s-t path
    def reduce_graph(self, s, t):
        # find all vertices that appear in at least one s-t path
        path_vertices = set()
        
        # using DFS to find all paths from s to t
        def dfs_find_paths(node, visited, current_path):
            visited.add(node)
            current_path.append(node)
            
            if node == t:
                path_vertices.update(current_path)
            else:
                for neighbor in self.adj.get(node, set()):
                    if neighbor not in visited:
                        dfs_find_paths(neighbor, visited.copy(), current_path.copy())
        
        dfs_find_paths(s, set(), [])
        
        # build new graph with only path vertices
        reduced = Graph()
        for u in path_vertices:
            for v in self.adj.get(u, set()):
                if v in path_vertices:
                    reduced.add_edge(u, v)
        
        return reduced
    
    def visualize(self, title="Graph", fixed_pos=None, highlight_nodes=None):
        # using nx here for visualisation only. we've used our own add_edge everywhere else
        nx_graph = nx.Graph()
        for u in self.adj:
            for v in self.adj[u]:
                nx_graph.add_edge(u, v)
        
        plt.figure(figsize=(8, 6))

        if highlight_nodes:
            node_colors = ['red' if node in highlight_nodes else 'skyblue' 
                          for node in nx_graph.nodes()]
        else:
            node_colors = 'skyblue'
        
        nx.draw(nx_graph, fixed_pos, with_labels=True, 
               node_color=node_colors, node_size=1000,
               font_size=12, font_weight='bold')
        plt.title(title, pad=20)
        plt.show()
        return fixed_pos