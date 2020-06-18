class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}
    
  def get_edges(self):
    return list(self.edges.keys())

station = Vertex("Cronk")