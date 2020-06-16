class MinHeap:
      def __init__(self):
    self.heap_list = [None]
    self.count = 0

  # define .add() below...
  def add(self, element):
    print("Adding {} to {}".format(element, self.heap_list))
    self.count += 1
    self.heap_list.append(element)
    self.heapify_up()


  # define .heapify_up() below...
  def heapify_up(self):
    print("Restoring the heap property…")
