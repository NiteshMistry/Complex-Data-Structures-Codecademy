# implement separate chaining
from linked_list import Node, LinkedList
# add flower definitions
from blossom_lib import flower_definitions 

class HashMap:
  def __init__(self, size):
    self.array_size = size
    #self.array = [None for i in range(size)]
    #self.array = [None] * size
    #self.array = [LinkedList() for i in range(size)]
    self.array = [LinkedList()] * size

  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code

  def compress(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    is_key_found = False
    for stored_key, stored_value in list_at_array:
      if stored_key == key:
        is_key_found = True
        stored_value = value
    if not is_key_found:
      list_at_array.insert(payload)

  def retrieve(self, key):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    list_at_index = self.array[array_index]
    for stored_key, stored_value in list_at_index:
      if stored_key == key:
        return stored_value
    return None
  
blossom = HashMap(len(flower_definitions))
for flower, meaning in flower_definitions:
  blossom.assign(flower, meaning)

#print(flower_definitions)
print(blossom.retrieve('daisy'))