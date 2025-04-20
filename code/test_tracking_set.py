import networkx as nx
import matplotlib.pyplot as plt
from tracking_set import TournamentTracker

def test_case_1():
    """Simple tournament graph"""
    # Create a graph first
    G = nx.DiGraph()
    edges = [
        # Edges from node 0
        (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 2),
        (2, 4),
        (3, 1), (3, 2),
        (4, 1), (4, 3)
    ]
    G.add_edges_from(edges)
    
    # Verify all edges are in the graph
    for u, v in edges:
        if not G.has_edge(u, v):
            print(f"Warning: Edge ({u}, {v}) not added to graph")
    
    # Initialize tracker with the graph
    tracker = TournamentTracker(G)

    fixed_pos = {
        0: (0, 1),
        1: (1, 2),
        2: (2, 1),
        3: (1, 0),
        4: (3, 1)
    }

    # Visualize the original graph
    visualize_graph(G, "TC1-Tournament: Original", fixed_pos, source=0, target=4)
    
    # Check if it's a tournament
    if is_tournament(G):
        print("Graph is a tournament")
        tracking_set = tracker.find_tracking_set(0, 4)
        print("Tracking set:", tracking_set)
        
        # Visualize with tracking set highlighted
        visualize_graph(G, "TC1-Tournament: With Tracking", fixed_pos, highlight_nodes=tracking_set, source=0, target=4)
    else:
        print("TC1: Graph is not a tournament")

def test_case_2():
    """More complex tournament graph"""
    # Create a graph first
    G = nx.DiGraph()
    edges = [
        (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 2), (1, 5),
        (2, 4), (2, 5),
        (1, 3), (2, 3), (5, 3),
        (4, 1), (4, 3), (4, 5),
        (5, 0)
    ]
    G.add_edges_from(edges)
    
    # Initialize tracker with the graph
    tracker = TournamentTracker(G)

    fixed_pos = {
        0: (0, 2),
        1: (1, 3), 2: (1, 1),
        3: (2, 3), 4: (2, 1),
        5: (3, 2)
    }

    # Visualize the original graph
    visualize_graph(G, "TC2-Tournament: Original", fixed_pos)
    
    # Check if it's a tournament
    if is_tournament(G):
        print("Graph is a tournament")
        tracking_set = tracker.find_tracking_set(0, 5)
        print("Tracking set:", tracking_set)
        
        # Visualize with tracking set highlighted
        visualize_graph(G, "TC2-Tournament: With Tracking", fixed_pos, highlight_nodes=tracking_set)
    else:
        print("TC2: Graph is not a tournament")

def is_tournament(G):
    """Check if the graph is a tournament"""
    nodes = list(G.nodes())
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            u, v = nodes[i], nodes[j]
            if not G.has_edge(u, v) and not G.has_edge(v, u):
                return False
            if G.has_edge(u, v) and G.has_edge(v, u):
                return False
    return True

def visualize_graph(G, title, pos=None, highlight_nodes=None, source=None, target=None):
    """Visualize the tournament graph"""
    plt.figure(figsize=(10, 8))
    if pos is None:
        pos = nx.spring_layout(G)
        
    # Draw the graph
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
    
    # Highlight tracking set nodes if provided
    if highlight_nodes:
        nx.draw_networkx_nodes(G, pos, 
                              nodelist=highlight_nodes,
                              node_color='red', 
                              node_size=500)
    
    # Draw most edges as straight lines
    edge_list = list(G.edges())
    if source is not None and target is not None:
        # Remove source-target edge from regular edge list
        if (source, target) in edge_list:
            edge_list.remove((source, target))
        
        # Draw source-target edge as curved
        if G.has_edge(source, target):
            nx.draw_networkx_edges(G, pos, edgelist=[(source, target)], 
                                  arrows=True, arrowsize=20, 
                                  connectionstyle='arc3,rad=0.3', 
                                  width=2, edge_color='blue')
    
    # Draw regular edges
    nx.draw_networkx_edges(G, pos, edgelist=edge_list, arrows=True)
    
    nx.draw_networkx_labels(G, pos)
    
    # Print edge information for debugging
    print(f"\nEdges in the graph:")
    for edge in G.edges():
        print(f"  {edge}")
    
    plt.title(title)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

# Run the test cases
test_case_1()
