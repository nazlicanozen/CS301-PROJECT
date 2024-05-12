class Dsatur:
    def __init__(self, G, lc=None):
        self.graph = G  # Initialize the Dsatur algorithm with a graph G and optional initial color list lc
        # Store the graph
        self.color_list = [i for i in range(len(G))] if lc == None else lc
        # If no initial color list is provided, generate one with indices
        self.sat_degrees = {n: len(self.graph.elements[n]) for n in self.graph.elements.keys()}
        # Initialize saturation degrees for each node in the graph
        self.output = {}  # Output dictionary to store the coloring result
    def colorer(self):
        if len(self.graph) == 0: #in case of empty graph
            return {0: [node.element() for node in self.graph.elements.keys()]}
        else:
            colored = 0
            while colored < len(self.graph): # Loop until all nodes are colored
                # Choose the node with the maximum saturation degree, breaking ties by choosing the one with maximum degree
                node = max(
                    self.sat_degrees,
                    key=lambda n: (
                        self.sat_degrees[n],  # Saturation degree
                        len(self.graph.elements[n])  # Degree of the node
                    )
                )
                # Get colors of neighboring nodes
                neighbor_colors = [n.get_color() for n in self.graph.elements[node]]
                for color in self.color_list:  # Iterate over available colors
                    # If color 'color' is not used by neighbors, assign it to the node
                    if color not in neighbor_colors:
                        node.set_color(color)  # Assign color to the node
                        if color not in self.output.keys():
                            self.output[color] = [node.element()]
                        else:
                            self.output[color].append(node.element())
                        self.sat_degrees[node] = 0  # Saturation degree becomes 0 for the colored node
                        # Update saturation degrees for neighboring nodes
                        for n in self.graph.elements[node]:
                            if n.get_color() == None:  # If the node is not colored
                                if colored == 0 or n.not_changed:  # If it's the first iteration or it wasn't changed previously
                                    self.sat_degrees[n] = 1  # Set its saturation degree to 1
                                else:
                                    self.sat_degrees[n] += 1  # Otherwise, increment its saturation degree
                                if n.not_changed:  # If the node wasn't changed previously
                                    n.not_changed = False  # Set the flag to False indicating it has been changed now
                        break  # Exit the loop after assigning color
                colored += 1  # Increment the colored node count
            return self.output  # Return the coloring result
