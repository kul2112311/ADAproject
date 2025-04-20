from graph import Graph
import networkx as nx

class ChordalGraph(Graph):
    def __init__(self):
        super().__init__()

    def is_chordal(self):
        # Build a NetworkX graph from adjacency list and check chordality
        G = nx.Graph()
        for u, nbrs in self.adj.items():
            for v in nbrs:
                G.add_edge(u, v)
        return nx.is_chordal(G)

    def find_tracking_set(self, s, t):
        # Pre-reduce the graph using parent class method (removes vertices/edges not on any s-t path)
        reduced = super().reduce_graph(s, t)

        T = set()
        # For each edge (a, b) in reduced graph:
        for a in reduced.adj:
            for b in reduced.adj[a]:
                # common neighbors of a and b
                commons = reduced.adj[a] & reduced.adj[b]
                for x in commons:
                    if x in T:
                        continue
                    # Build H = reduced minus x
                    H = nx.Graph()
                    # add all edges except those incident to x
                    for u, nbrs in reduced.adj.items():
                        if u == x:
                            continue
                        for v in nbrs:
                            if v == x:
                                continue
                            H.add_edge(u, v)
                    # Ensure s and t exist in H, even if isolated
                    H.add_node(s)
                    H.add_node(t)
                    # Check if (a,b) can still be on an s-t path without x
                    # i.e., if we can reach a from s and t from b
                    if nx.has_path(H, s, a) and nx.has_path(H, b, t):
                        T.add(x)
        return T