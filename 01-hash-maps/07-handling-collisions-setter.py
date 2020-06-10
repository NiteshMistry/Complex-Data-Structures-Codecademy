class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    if self.array[array_index] != None:
      current_array_key, current_array_value = self.array[array_index]
      if current_array_key == key:
        self.array[array_index] = [current_array_key, value]
    else:
      self.array[array_index] = [key, value]

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    return self.array[array_index]
