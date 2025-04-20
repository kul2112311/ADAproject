from graph import Graph
import networkx as nx

class TournamentGraph(Graph):
    def __init__(self):
        super().__init__()
        self.directed = True  # Tournament graphs are directed

    def add_edge(self, u, v):
        """Override to ensure no reverse edge is added"""
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].add(v)  # Only add u->v

    def is_tournament(self):
        """Check if the graph is a tournament graph"""
        # Convert to networkx for verification
        nx_graph = nx.DiGraph()
        for u in self.adj:
            for v in self.adj[u]:
                nx_graph.add_edge(u, v)
        return nx.is_tournament(nx_graph)

    def find_tracking_set(self, s, t):
        """Implementation of Algorithm 2 from the paper"""
        # First apply reduction
        reduced = super().reduce_graph(s, t)
        T = set()

        # Convert to networkx for path checking
        nx_graph = nx.DiGraph()
        for u in reduced.adj:
            for v in reduced.adj[u]:
                nx_graph.add_edge(u, v)

        for u in reduced.adj:
            for v in reduced.adj[u]:
                # Find common neighbors (out-neighbors of u and in-neighbors of v)
                out_neighbors = reduced.adj[u]
                in_neighbors = {x for x in reduced.adj if v in reduced.adj[x]}
                common = out_neighbors & in_neighbors - {s, t}

                for x in common:
                    if x in T:
                        continue

                    # Check if edge (u,v) is in some s-t path in G-x
                    G_minus_x = nx_graph.copy()
                    G_minus_x.remove_node(x)
                    if (nx.has_path(G_minus_x, s, u) and 
                        nx.has_path(G_minus_x, v, t) and
                        nx.has_path(G_minus_x, u, v)):
                        T.add(x)

        return T