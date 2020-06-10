class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key):
    self.key = key
    #encode() is a string method that converts a string into its corresponding bytes, a list-like object with the numerical representation of each character in the string.
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code