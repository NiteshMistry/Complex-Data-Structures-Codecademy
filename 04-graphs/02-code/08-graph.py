class Graph:
  def __init__(self, directed = False):
    self.graph_dict = {}
    self.directed = directed

  def add_vertex(self, vertex):
    self.graph_dict[vertex.value] = vertex

  def add_edge(self, from_vertex, to_vertex, weight = 0):
    self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
    if not self.directed:
      self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)
   
  def find_path(self, start_vertex, end_vertex):
    print("Searching from {0} to {1}".format(start_vertex, end_vertex))
    start = [start_vertex]
    while start:
      current_vertex = start.pop(0)
      print("Current Vertex: " + current_vertex)