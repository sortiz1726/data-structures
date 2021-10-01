from linked_list import LinkList

class HashTable:
  def __init__(self, number_of_buckets):
    self.__number_of_buckets = number_of_buckets
    self.__table = [None] * self.__number_of_buckets

  def hash(self, value):
    return hash(value) % self.__number_of_buckets

  def set(self, value):
    hash_index = self.hash(value)
    
    bucket_list = None
    
    if self.__table[hash_index] is None:
      bucket_list = LinkList()
      self.__table[hash_index] = bucket_list
      
    else:
      bucket_list = self.__table[hash_index]
    
    bucket_list.add(value)


  def get(self, value):
    hash_index = self.hash(value)
    
    if self.__table[hash_index] is None:
      return None
    else:
      bucket_list = self.__table[hash_index]
      return bucket_list.find(value)

  def has_key(self, value):
    hash_index = self.hash(value)
    
    if self.__table[hash_index] is None:
      return False
    else:
      bucket_list = self.__table[hash_index]
      return bucket_list.does_contain(value)
  
  def print_info(self):
    print(f"Number of bucket: {self.__number_of_buckets}")
    
    bucket_number = 0
    for bucket_list in self.__table:
      
      print(f"\nbucket: {bucket_number}")
      if bucket_list is not None:
        for i in range(bucket_list.size()):
          print(f"\t{bucket_list.get(i)}")
      else:
        print(f"\t{bucket_list}")
        
      bucket_number += 1


def test_bst():
  table = HashTable(17)
  
  collection = ["hda", "add", "substract"]
  
  for item in collection:
    table.set(item)
  
  table.print_info()
  
  print("\n")
  for item in collection:
    print(f"Does contain {item}? {'Yes' if table.has_key(item) else 'No'}")
    
values = [10, 20, 30]
#values = [30, 20, 10]
  
def hash_combine(values):
  print(f"for {values}, the hash is")
  
  hash_value = 1
  for value in values:
    hash_value = 31 * hash_value + value
    print(hash_value)
    
  print("")
  
hash_combine([1, 0, 0])
hash_combine([0, 0, 31 ** 2 * 1])