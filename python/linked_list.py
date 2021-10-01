# ----- Node ------
class Node:
  def __init__(self, data = None):
    self.data = data
    self.next_node = None

class LinkList:
  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__size = 0
    
  def add(self, data):
    node = Node(data)
    
    if self.is_empty():
        self.__head = node
        self.__tail = node
    else:
        self.__tail.next_node = node
        self.__tail = node
        
    self.__size += 1

  def remove(self, data):
    parent_node = None
    current_node = self.__head
    
    while current_node is not None and current_node.data != data:
      parent_node = current_node
      current_node = current_node.next_node
            
    if current_node is not None:
      if current_node is self.__tail:
        self.__tail = parent_node
        
      if current_node is self.__head:
        self.__head = self.__head.next_node
      else:
        parent_node.next_node = current_node.next_node
            
      self.__size -= 1

  def get(self, index):
    current_node = self.__head
    
    while current_node is not None and index > 0:
      current_node = current_node.next_node
      index -= 1
            
    return current_node.data
    
  def find(self, data):
    current_node = self.__head
    
    while current_node is not None and current_node.data != data:
      current_node = current_node.next_node
      
    if current_node is not None:
      return current_node.data
    
  def does_contain(self, data):
    current_node = self.__head
    
    while current_node is not None and current_node.data != data:
      current_node = current_node.next_node
      
    return current_node is not None

  def size(self):
    return self.__size
      
  def is_empty(self):
    return self.__size == 0

if False:
  collection = [5, 4, 8, 18, 2, 4, 4, 4, 1]
  
  my_list = LinkList()
  
  for item in collection:
    my_list.add(item)
    
  for i in range(my_list.size()):
    print(my_list.get(i))
  