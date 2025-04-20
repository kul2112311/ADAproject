import networkx as nx
import matplotlib.pyplot as plt

class TournamentTracker:
    def __init__(self, graph=None):
        if graph is None:
            self.graph = nx.DiGraph()
        else:
            self.graph = graph.copy()
    
    def add_edge(self, u, v):
        """Add an edge to the tournament graph"""
        self.graph.add_edge(u, v)
    
    def is_tournament(self):
        """Check if the graph is a tournament"""
        nodes = list(self.graph.nodes())
        for i in range(len(nodes)):
            for j in range(i+1, len(nodes)):
                u, v = nodes[i], nodes[j]
                if not self.graph.has_edge(u, v) and not self.graph.has_edge(v, u):
                    return False
                if self.graph.has_edge(u, v) and self.graph.has_edge(v, u):
                    return False
        return True
    
    def visualize(self, title, pos=None, highlight_nodes=None):
        """Visualize the tournament graph"""
        plt.figure(figsize=(10, 8))
        if pos is None:
            pos = nx.spring_layout(self.graph)
            
        # Draw the graph
        nx.draw_networkx_nodes(self.graph, pos, node_color='lightblue', node_size=500)
        
        # Highlight tracking set nodes if provided
        if highlight_nodes:
            nx.draw_networkx_nodes(self.graph, pos, 
                                  nodelist=highlight_nodes,
                                  node_color='red', 
                                  node_size=500)
            
        nx.draw_networkx_edges(self.graph, pos, arrows=True)
        nx.draw_networkx_labels(self.graph, pos)
        
        plt.title(title)
        plt.axis('off')
        plt.tight_layout()
        plt.show()
        
    def path_contains_edge(self, path, edge):
        """Check if a path contains a specific edge (with debug print)"""
        for i in range(len(path) - 1):
            if (path[i], path[i+1]) == edge:
                return True
        return False
    
    def find_tracking_set(self, s, t):
        """
        Implementation with ALL original print statements preserved.
        Returns the same output as your original code.
        """
        T = set()
        excluded_vertices = {s, t}
        
        print("Starting tracking set algorithm...")
        print(f"Source: {s}, Target: {t}")
        
        for edge in list(self.graph.edges()):
            a, b = edge
            print(f"\nExamining edge ({a}, {b}):")
            
            out_neighbors_of_a = set(self.graph.successors(a))
            in_neighbors_of_b = set(self.graph.predecessors(b))
            common_neighbors = out_neighbors_of_a & in_neighbors_of_b
            common_neighbors -= excluded_vertices
            candidates = common_neighbors - T
            
            if not candidates:
                print(f"  No candidate trackers for edge ({a}, {b})")
                continue
                
            print(f"  Potential trackers for edge ({a}, {b}): {candidates}")
            
            for x in candidates:
                if x in excluded_vertices:
                    print(f"  Skipping vertex {x} as it's either source or target")
                    continue
                    
                print(f"  Checking if vertex {x} needs to be a tracker:")
                G_minus_x = self.graph.copy()
                G_minus_x.remove_node(x)
                path_exists = False
                
                try:
                    if s in G_minus_x.nodes and t in G_minus_x.nodes:
                        all_paths = list(nx.all_simple_paths(G_minus_x, s, t))
                        for path in all_paths:
                            if self.path_contains_edge(path, edge):
                                path_exists = True
                                print(f"    Found path through edge ({a}, {b}) in G-{x}: {path}")
                                break
                    else:
                        all_paths = []
                except nx.NetworkXNoPath:
                    print(f"    No paths from {s} to {t} in G-{x}")
                
                if path_exists:
                    T.add(x)
                    print(f"    Added {x} to tracking set (current T = {T})")
                else:
                    print(f"    No paths through edge ({a}, {b}) in G-{x}, tracker not needed")
        
        T -= excluded_vertices
        print(f"\nAfter removing s and t: T = {T}")
        
        all_paths = list(nx.all_simple_paths(self.graph, s, t))
        paths_by_trackers = {}
        
        for path_idx, path in enumerate(all_paths):
            trackers_in_path = tuple(v for v in path if v in T)
            
            if trackers_in_path in paths_by_trackers:
                print(f"\nFound two paths with the same tracker sequence: {trackers_in_path}")
                print(f"Path 1: {paths_by_trackers[trackers_in_path]}")
                print(f"Path 2: {path}")
                
                for v in path:
                    if (v not in paths_by_trackers[trackers_in_path] and 
                        v not in excluded_vertices and 
                        v not in T):
                        T.add(v)
                        print(f"Added {v} to tracking set to distinguish paths")
                        paths_by_trackers = {trackers_in_path: paths_by_trackers[trackers_in_path]}
                        break
            else:
                paths_by_trackers[trackers_in_path] = path
        
        return T
    
    def verify_tracking_set(self, s, t, T):
        """Verification with original print messages"""
        all_paths = list(nx.all_simple_paths(self.graph, s, t))
        
        print(f"\nVerifying tracking set T = {T}")
        print(f"Found {len(all_paths)} paths from {s} to {t}")
        
        paths_by_trackers = {}
        for i, path in enumerate(all_paths):
            trackers_in_path = tuple(v for v in path if v in T)
            print(f"Path {i+1}: {path}, Trackers: {trackers_in_path}")
            
            if trackers_in_path in paths_by_trackers:
                print(f"PROBLEM: Paths {paths_by_trackers[trackers_in_path]+1} and {i+1} have identical tracker sequences: {trackers_in_path}")
                return False
            paths_by_trackers[trackers_in_path] = i
        
        print("SUCCESS: All paths have unique tracker sequences")
        return True