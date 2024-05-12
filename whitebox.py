import unittest
from graph import Graph
from dsatur import Dsatur  

#STATEMENT COVERAGE
class TestDsaturStatementCoverage(unittest.TestCase):
    def test_initialization(self):
        graph = Graph()
        graph.insert_nodes([0, 1, 2])
        graph.add_edges([(0, 1), (0, 2), (1, 2)])
        dsatur = Dsatur(graph)
        self.assertIsNotNone(dsatur.graph, "Graph is not initialized (non-empty graph)")
        self.assertIsNotNone(dsatur.color_list, "Color list is not initialized (non-empty graph)")
        self.assertIsNotNone(dsatur.sat_degrees, "Saturation degrees are not initialized (non-empty graph)")
        self.assertIsNotNone(dsatur.output, "Output dictionary is not initialized (non-empty graph)")

        graph2 = Graph()
        graph2.insert_nodes([])
        graph2.add_edges([])
        dsatur = Dsatur(graph2)
        self.assertIsNotNone(dsatur.graph, "Graph is not initialized (empty graph)")
        self.assertIsNotNone(dsatur.color_list, "Color list is not initialized (empty graph)")
        self.assertIsNotNone(dsatur.sat_degrees, "Saturation degrees are not initialized (empty graph)")
        self.assertIsNotNone(dsatur.output, "Output dictionary is not initialized (empty graph)")

        graph3 = Graph()
        graph3.insert_nodes([])
        graph3.add_edges([])
        dsatur = Dsatur(graph3)
        self.assertIsNotNone(dsatur.graph, "Graph is not initialized (isolated graph)")
        self.assertIsNotNone(dsatur.color_list, "Color list is not initialized (isolated graph)")
        self.assertIsNotNone(dsatur.sat_degrees, "Saturation degrees are not initialized (isolated graph)")
        self.assertIsNotNone(dsatur.output, "Output dictionary is not initialized (isolated graph)")
    
    def test_coloring_loop(self):
        graph = Graph()
        graph.insert_nodes([0, 1, 2])
        graph.add_edges([(0, 1), (0, 2), (1, 2)])
        dsatur = Dsatur(graph)
        output = dsatur.colorer()
        self.assertGreater(len(output), 0, "Output dictionary is empty for non-empty graph")

        graph2 = Graph()
        graph2.insert_nodes([])
        graph2.add_edges([])
        dsatur = Dsatur(graph2)
        output = dsatur.colorer()
        self.assertGreater(len(output), 0, "Output dictionary is empty for empty graph")

        graph3 = Graph()
        graph3.insert_nodes([0, 1, 2])
        graph3.add_edges([])
        dsatur = Dsatur(graph)
        output = dsatur.colorer()
        self.assertGreater(len(output), 0, "Output dictionary is empty for isolated graph")

if __name__ == '__main__':
    unittest.main()
