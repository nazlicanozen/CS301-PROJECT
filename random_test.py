#IMPLEMENTED BY GROUP-69 (07.05.2024)
import random
from graph import Graph
from dsatur import Dsatur
import networkx as nx
import matplotlib.pyplot as plt
#####GRAPH GENERATOR AND COLORER######
print("##################### Random Test ###################")
num_nodes = random.randint(1, 35) #generate a random node amount
g = Graph() #implement the graph
nodes = list(range(num_nodes)) #insert all nodes
g.insert_nodes(nodes)
edges = [] #make edge connections
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        if random.random() < 0.5: 
            edges.append((nodes[i], nodes[j]))
g.add_edges(edges)
print(f"Number of nodes: {len(g)}")
d = {n.element(): len(g.elements[n]) for n in g.elements.keys()}
print(f"Nodes and degrees: {d}")
nodes_human_readable = [[node.element() for node in g.elements[n]] for n in g.elements.keys()]

dsatur = Dsatur(g) #color the generated graph using DSATUR algorithm
colors = dsatur.colorer()
print("The graph is colored using", len(colors), "colors with DSATUR algorithm")
#####GRAPH VISUALIZER######
G = nx.Graph()
for node in g.elements.keys():
    G.add_node(node.element())
for u, v in edges:
    G.add_edge(u, v)
node_colors = [] #visualize the colors such that no adjacent colors are the same
for node in G.nodes():
    for color, colored_nodes in colors.items():
        if node in colored_nodes:
            node_colors.append(color)
            break
plt.figure(figsize=(5, 3)) #adjust the figure size
nx.draw(G, with_labels=True, node_color=node_colors, cmap=plt.cm.rainbow, node_size=500)
plt.title(f"Random Graph with {num_nodes} Nodes and {len(colors)} Colors")
output_file = f"graph_{num_nodes}_nodes_{len(colors)}_colors.png" #save & show
plt.savefig(output_file)
plt.show()
