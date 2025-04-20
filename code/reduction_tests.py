from graph import Graph

# test case 1: dead end branch
def test_case_1():
    g1 = Graph()
    edges = [('s','a'), ('a','b'), ('b','t'), 
            ('a','c'), ('c','d'), ('d','t'),
            ('b','e'), ('e','f'), ('f','t'),
            ('c','x'), ('x','y')]

    fixed_pos_1 = {
        's': (0, 2), 'a': (1, 2), 'b': (2, 2), 't': (3, 2),
        'c': (1, 1), 'd': (2, 1), 'e': (2, 3), 'f': (3, 3),
        'x': (1, 3), 'y': (0, 3)
    }

    for u, v in edges:
        g1.add_edge(u, v)

    g1.visualize("Original", fixed_pos_1)
    reduced1 = g1.reduce_graph('s', 't')
    reduced1.visualize("Reduced", fixed_pos_1)

# test case 2: disconnected components
def test_case_2():
    g2 = Graph()
    edges = [('s','a'), ('a','b'), ('b','t'),
            ('c','d'), ('d','e'),
            ('x','y'), ('y','z')]

    fixed_pos_2 = {
        's': (0, 2), 'a': (1, 2), 'b': (3, 1), 't': (3, 0),
        'c': (0, 1), 'd': (1, 1), 'e': (2, 1),
        'x': (0, 0), 'y': (1, 0), 'z': (2, 0)
    }

    for u, v in edges:
        g2.add_edge(u, v)

    g2.visualize("Original", fixed_pos_2)
    reduced2 = g2.reduce_graph('s', 't')
    reduced2.visualize("Reduced", fixed_pos_2)

# test case 3: stays entirely
def test_case_3():
    g3 = Graph()
    edges = [('s','a'), ('s','b'), ('a','t'), ('b','t'),
            ('a','b'), ('s','c'), ('c','d'), ('d','t'),
            ('b','d'), ('a','d')]

    fixed_pos_3 = {
        's': (0, 2), 'a': (1, 3), 'b': (1, 1),
        'c': (0.5, 2), 'd': (2, 2), 't': (3, 2)
    }

    for u, v in edges:
        g3.add_edge(u, v)

    g3.visualize("Original", fixed_pos_3)
    reduced3 = g3.reduce_graph('s', 't')
    reduced3.visualize("Reduced", fixed_pos_3)

# test case 4: no s-t path
def test_case_4():
    g4 = Graph()
    edges = [('s','a'), ('a','b'), ('b','c'),
            ('x','y'), ('y','z'), ('z','t')]

    fixed_pos_4 = {
        's': (0, 2), 'a': (1, 2), 'b': (2, 2), 'c': (3, 2),
        'x': (0, 1), 'y': (1, 1), 'z': (2, 1), 't': (3, 1)
    }

    for u, v in edges:
        g4.add_edge(u, v)

    g4.visualize("Original", fixed_pos_4)
    reduced4 = g4.reduce_graph('s', 't')
    reduced4.visualize("TC4-Main: Reduced", fixed_pos_4)

# test case 5: dead end again
def test_case_5():
    g5 = Graph()
    edges = [
        ('s','a1'), ('a1','a2'), ('a2','a3'), ('a3','t'),
        ('s','b1'), ('b1','b2'), ('b2','t'),
        ('a1','c1'), ('c1','c2'), ('c2','t'),
        ('a2','d1'), ('d1','d2'), ('d2','d3'),
        ('b1','e1'), ('e1','e2'),
        ('a3','b2'), ('c1','d1'), ('e1','d2')
    ]

    fixed_pos_5 = {
        's': (0, 2),
        'a1': (1, 2), 'a2': (2, 2), 'a3': (3, 2),
        'b1': (3, 3), 'b2': (4, 3),
        'c1': (1, 1), 'c2': (2, 1),
        'd1': (2, 0), 'd2': (3, 0), 'd3': (4, 0),
        'e1': (2, 3), 'e2': (1, 3),
        't': (4, 2)
    }

    for u, v in edges:
        g5.add_edge(u, v)

    g5.visualize("Original", fixed_pos_5)
    reduced5 = g5.reduce_graph('s', 't')
    reduced5.visualize("Reduced", fixed_pos_5)

# test case 6: stays entirely
def test_case_6():
    g6 = Graph()
    edges = [('s','a'), ('s','b'),
            ('a','c'), ('b','c'),
            ('c','t')]

    fixed_pos_6 = {
        's': (0, 2), 'a': (1, 3), 'b': (1, 1),
        'c': (2, 2), 't': (3, 2)
    }

    for u, v in edges:
        g6.add_edge(u, v)

    g6.visualize("Original", fixed_pos_6)
    reduced6 = g6.reduce_graph('s', 't')
    reduced6.visualize("Reduced", fixed_pos_6)