class Node:
    __slots__ = '_element', '_color', 'not_changed'
        
    def __init__(self, element):
        # Initialize a node with an element and default color (None)
        self._element = element
        self._color = None
        self.not_changed = True  # Flag to track if the node's color has been changed

    def element(self):
        return self._element

    def get_color(self):
        return self._color

    def set_color(self, c):
        # Set the color of the node
        self._color = c
            
    def __hash__(self):
        return hash(id(self._element))

class Graph:
            
    def __init__(self):
        # Initialize a graph with an empty dictionary to store nodes and their adjacency lists
        self.elements = {}

    def __len__(self):
        return len(self.elements)
    
    def insert_node(self, n):
        # Insert a node into the graph
        node = Node(n)
        self.elements[node] = []

    def insert_nodes(self, nodes):
        # Insert multiple nodes into the graph
        for n in nodes:
            self.insert_node(n)
    
    def add_edge(self, u, v):
        # Add an edge between nodes u and v
        node_u, node_v = None, None
        for node in self.elements:
            if node.element() == u:
                node_u = node
            elif node.element() == v:
                node_v = node
            if node_u and node_v:
                break
        if not (node_u and node_v):
            raise NodeException("Node not found in the graph")
        self.elements[node_u].append(node_v)
        self.elements[node_v].append(node_u)

    def add_edges(self, edges):
        # Add multiple edges to the graph
        for edge in edges:
            u, v = edge
            self.add_edge(u, v)

    def degree(self, node):
        # Return the degree of a node
        return len(self.elements[node])

class NodeException(Exception):
    "Use when the node is not found in the graph"
