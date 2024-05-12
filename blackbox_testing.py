from graph import Graph
from dsatur import Dsatur

print("##################### Test Case 1 ###################") #Test case 1: Empty Graph
g = Graph()
g.insert_nodes([])
g.add_edges([])
print(f"Number of nodes: {len(g)}")
d = {n.element(): len(g.elements[n]) for n in g.elements.keys()} 
ds = Dsatur(g)
out = ds.colorer()
expected_output_colors = 0 
print(f"Number of colors used: {len(out)}")
assert len(out) == expected_output_colors

print("##################### Test Case 2 ###################") #Test case 2: Graph With No Edges
g1 = Graph()
g1.insert_nodes([1, 2, 3, 4])
g1.add_edges([])
print(f"Number of nodes: {len(g1)}")
d1 = {n.element(): len(g1.elements[n]) for n in g1.elements.keys()}
ds1 = Dsatur(g1)
out1 = ds1.colorer()
expected_output_colors = 1
print(f"Number of colors used: {len(out1)}")
assert len(out1) == expected_output_colors

print("##################### Test Case 3 ###################") #Test case 3: Graph With Multiple Nodes And Edges
g2 = Graph()
g2.insert_nodes([0, 1 ,2 ,3 ,4 ,5])
g2.add_edges([(0,1),(0,2),(0,3),(1,3),(1,4),(2,3),(2,5),(3,4),(3,5),(4,5)])
print(f"Number of nodes: {len(g2)}")
d2 = {n.element(): len(g2.elements[n]) for n in g2.elements.keys()}
ds2 = Dsatur(g2)
out2 = ds2.colorer()
expected_output_colors = 4
print(f"Number of colors used: {len(out2)}")
assert len(out2) == expected_output_colors

print("##################### Test Case 4 ###################") #Test case 4: Graph with isolated vertices
g3 = Graph()
g3.insert_nodes([0,1,2,3,4,5]) 
g3.add_edges([(0,1),(0,2),(0,3),(2,3),(2,5)]) 
print(f"Number of nodes: {len(g3)}")
d3 = {n.element(): len(g3.elements[n]) for n in g3.elements.keys()}
ds3 = Dsatur(g3)
out3 = ds3.colorer()
expected_output_colors = 3
print(f"Number of colors used: {len(out3)}")
assert len(out3) == expected_output_colors

print("##################### Test Case 5 ###################") #Test Case 5: Graph With Self-Loop
g4 = Graph()
g4.insert_nodes([1, 2, 3, 4]) 
g4.add_edges([(1,2), (1,3), (2,4), (3,4)]) 
print(f"Number of nodes: {len(g4)}")
d4 = {n.element(): len(g4.elements[n]) for n in g4.elements.keys()}
ds4 = Dsatur(g4)
out4 = ds4.colorer()
expected_output_colors = 2
print(f"Number of colors used: {len(out4)}")
assert len(out4) == expected_output_colors

print("##################### Test Case 6 ###################") #Test Case 6: Bipartite Graph
g5 = Graph()
g5.insert_nodes([1, 2, 3, 4]) 
g5.add_edges([(1,3), (1,4), (2,3), (2,4)]) 
print(f"Number of nodes: {len(g5)}")
d5 = {n.element(): len(g5.elements[n]) for n in g5.elements.keys()}
ds5 = Dsatur(g5)
out5 = ds5.colorer()
expected_output_colors = 2
print(f"Number of colors used: {len(out5)}")
assert len(out5) == expected_output_colors

print("ALL TEST CASES PASSED")
