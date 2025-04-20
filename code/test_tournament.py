from tournament import TournamentGraph

def test_case_1():
    """Simple tournament graph"""
    g = TournamentGraph()
    edges = [
        (0, 1), (0, 2), (0, 3),
        (1, 2), (1, 3),
        (2, 3), (2, 4),
        (3, 1), (3, 4),
        (4, 0)
    ]

    fixed_pos = {
        0: (0, 1),
        1: (1, 2),
        2: (2, 1),
        3: (1, 0),
        4: (3, 1)
    }

    for u, v in edges:
        g.add_edge(u, v)

    g.visualize("TC1-Tournament: Original", fixed_pos)
    if g.is_tournament():
        print("Graph is a tournament")
        tracking_set = g.find_tracking_set(0, 4)
        print("Tracking set:", tracking_set)
        g.visualize("TC1-Tournament: With Tracking", fixed_pos, highlight_nodes=tracking_set)
    else:
        print("TC1: Graph is not a tournament")

def test_case_2():
    """More complex tournament graph"""
    g = TournamentGraph()
    edges = [
        (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 2), (1, 5),
        (2, 4), (2, 5),
        (3, 1), (3, 2), (3, 5),
        (4, 1), (4, 3), (4, 5),
        (5, 0)
    ]

    fixed_pos = {
        0: (0, 2),
        1: (1, 3), 2: (1, 1),
        3: (2, 3), 4: (2, 1),
        5: (3, 2)
    }

    for u, v in edges:
        g.add_edge(u, v)

    g.visualize("TC2-Tournament: Original", fixed_pos)
    if g.is_tournament():
        print("Graph is a tournament")
        tracking_set = g.find_tracking_set(0, 5)
        print("Tracking set:", tracking_set)
        g.visualize("TC2-Tournament: With Tracking", fixed_pos, highlight_nodes=tracking_set)
    else:
        print("TC2: Graph is not a tournament")

test_case_1()