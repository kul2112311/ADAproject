from chordal import ChordalGraph

# Test Case 1: Simple chordal graph with obvious trackers
def test_case_1():
    g = ChordalGraph()

    edges = [
        # First triangle (clique)
        ('s', 'a'), ('a', 'b'), ('b', 's'),
        # Second triangle sharing one vertex
        ('b', 'c'), ('c', 'd'), ('d', 'b'),
        # Third triangle sharing one vertex
        ('d', 'e'), ('e', 't'), ('t', 'd'),
        # Additional chordal connections
        ('a', 'd'), ('b', 'e')
    ]

    # Positions for visualization
    fixed_pos = {
        's': (0, 2), 'a': (1, 2), 'b': (1, 1),
        'c': (2, 0), 'd': (2, 1), 'e': (2, 2),
        't': (3, 2)
    }

    for u, v in edges:
        g.add_edge(u, v)

    g.visualize("Original", fixed_pos)
    if g.is_chordal():
        tracking_set = g.find_tracking_set('s', 't')
        print("Tracking set:", tracking_set)
        g.visualize("With Tracking", fixed_pos, highlight_nodes=tracking_set)
    else:
        print("TC1: Graph is not chordal")

# Test Case 2: More complex chordal graph (your sample_chordal_graph1)
def test_case_2():
    g = ChordalGraph()

    edges = [
        # Connections of a
        ('s', 'b'),  # a -> b
        ('s', 't'),  # a -> h
        ('s', 'g'),
        
        # Connections of b
        ('b', 'c'),  # b -> c
        ('b', 'd'),  # b -> d
        ('b', 'g'),
        ('b', 't'),  # b -> h
        
        # Connections of c
        ('c', 'd'),  # c -> d
        
        # Connections of d
        ('d', 'e'),  # d -> e
        ('d', 'g'),  # d -> g
        ('d', 't'),  # d -> h
        
        # Connections of e
        ('e', 'f'),  # e -> f
        ('e', 'g'),  # e -> g
        
        # Connections of f
        ('f', 'g'),  # f -> g
        
        # Connections of g
        ('g', 't'),  # g -> h
    ]

    # Positions for visualization
    fixed_pos = {
        's': (0, 1),  
        'b': (1, 2),
        'c': (2, 2),
        'd': (3, 1),  
        'e': (3, 0),
        'f': (2, -1),
        'g': (1, -1), 
        't': (0, 0),
    }

    for u, v in edges:
        g.add_edge(u, v)

    g.visualize("TC2-Chordal: Original", fixed_pos)
    if g.is_chordal():
        tracking_set = g.find_tracking_set('s', 't')
        print("TC2 Tracking set:", tracking_set)
        g.visualize("TC2-Chordal: With Tracking", fixed_pos, highlight_nodes=tracking_set)
    else:
        print("TC2: Graph is not chordal")

def test_case_3():
    g = ChordalGraph()

    edges = [
        ('s', 'a'),
        ('a', 'b'),
        ('b', 't'),
        ('a', 't')
    ]

    fixed_pos = {
        's': (0, 1),
        'a': (1, 2),
        'b': (2, 1),
        't': (3, 1)
    }

    for u, v in edges:
        g.add_edge(u, v)

    g.visualize("Original", fixed_pos)
    if g.is_chordal():
        tracking_set = g.find_tracking_set('s', 't')
        print("Tracking set:", tracking_set)
        g.visualize("With Tracking", fixed_pos, highlight_nodes=tracking_set)
    else:
        print("Graph is not chordal")

def test_case_4():
    g = ChordalGraph()

    # Edges for the graph
    edges = [
        ('s', 'a'),
        ('a', 'b'),
        ('a', 'c'),
        ('a', 'd'),
        ('b', 'c'),
        ('c', 't'),
        ('a', 't'),
        ('b', 'd'),
        ('d', 't'),
        ('c', 'd')
    ]

    # Positions for visualization
    fixed_pos = {
        's': (0, 2),
        'a': (1, 2),
        'b': (1, 1),
        'c': (2, 1),
        'd': (2, 0),
        't': (3, 1)
    }

    # Add the edges to the graph
    for u, v in edges:
        g.add_edge(u, v)

    g.visualize("Original", fixed_pos)
    
    if g.is_chordal():
        tracking_set = g.find_tracking_set('s', 't')
        print("Tracking set:", tracking_set)
        g.visualize("With Tracking", fixed_pos, highlight_nodes=tracking_set)
    else:
        print("Graph is not chordal")

def test_case_5():
    g = ChordalGraph()

    # Edge list
    edges = [
        # Clique C0 (s,u1,u2,u3)
        ('s','u1'), ('s','u2'), ('s','u3'),
        ('u1','u2'), ('u1','u3'), ('u2','u3'),
        # Clique C1 (v1,v2,v3,t)
        ('v1','v2'), ('v1','v3'), ('v2','v3'),
        ('v1','t'),  ('v2','t'),  ('v3','t'),
        # Articulation a to all u’s and v’s
        ('a','u1'), ('a','u2'), ('a','u3'),
        ('a','v1'), ('a','v2'), ('a','v3'),
    ]

    # Fixed positions for visualization
    fixed_pos = {
        's':  (2, 4),
        'u1': (1, 3),  'u2': (2, 3),  'u3': (3, 3),
        'a':  (2, 2),
        'v1': (1, 1),  'v2': (2, 1),  'v3': (3, 1),
        't':  (2, 0),
    }

    for u, v in edges:
        g.add_edge(u, v)

    g.visualize("Original", fixed_pos)
    if g.is_chordal():
        tracking_set = g.find_tracking_set('s', 't')
        print("Tracking set:", tracking_set)
        g.visualize("With Tracking", fixed_pos, highlight_nodes=tracking_set)
    else:
        print("Graph is not chordal")

def test_case_6():
    g = ChordalGraph()

    edges = [
        ('s','1'),
        ('s', '5'),
        ('1','2'),
        ('2','3'),
        ('3','4'),
        ('4','5'),
        ('5','6'),
        ('5', '1'),
        ('5', '2'),
        ('5', '3'),
        ('6','7'),
        ('7','8'),
        ('8','9'),
        ('9','t'),
    ]

    fixed_pos = {
    's':  (10, 0),
    '1':  (9,  0),
    '2':  (8,  0),
    '3':  (7,  0),
    '4':  (6,  0),
    '5':  (5,  1),
    '6':  (4,  0),
    '7':  (3,  0),
    '8':  (2,  0),
    '9':  (1,  0),
    't':  (0,  0),
    }

    for u, v in edges:
        g.add_edge(u, v)

    g.visualize("Original", fixed_pos)
    if g.is_chordal():
        tracking_set = g.find_tracking_set('s', 't')
        print("Tracking set:", tracking_set)
        g.visualize("With Tracking", fixed_pos, highlight_nodes=tracking_set)
    else:
        print("Graph is not chordal")

def test_case_7():
    g = ChordalGraph()

    edges = [
        ('s','1'),
        ('1','2'),
        ('2','3'),
        ('3','4'),
        ('4','5'),
        ('5','6'),
        ('6','7'),
        ('7','8'),
        ('8','9'),
        ('9','t'),
    ]

    fixed_pos = {
    's':  (10, 0),
    '1':  (9,  0),
    '2':  (8,  0),
    '3':  (7,  0),
    '4':  (6,  0),
    '5':  (5,  0),
    '6':  (4,  0),
    '7':  (3,  0),
    '8':  (2,  0),
    '9':  (1,  0),
    't':  (0,  0),
    }

    for u, v in edges:
        g.add_edge(u, v)

    g.visualize("Original", fixed_pos)
    if g.is_chordal():
        tracking_set = g.find_tracking_set('s', 't')
        print("Tracking set:", tracking_set)
        g.visualize("With Tracking", fixed_pos, highlight_nodes=tracking_set)
    else:
        print("Graph is not chordal")

test_case_7()