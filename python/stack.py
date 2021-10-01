from linked_list import Node

class Stack:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack
  def __init__(self):
    self.__size = 0
    self.__head = None
    
  def push(self, item):
    node = Node(item)
    node.next_node = self.__head
    self.__head = node    
    self.__size += 1        

  def pop(self):
    data = None
      
    if not self.is_empty():
      data = self.__head.data
      self.__head = self.__head.next_node
      self.__size -= 1  
        
    return data
        
  def size(self):
    return self.__size
        
  def is_empty(self):
    return self.__size == 0


if False:
  test_stack = Stack()
  collection = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  
  print("PUSING STACK")
  for item in collection:
    print(f"-> {item}")
    test_stack.push(item)
  
  print("\nPOPING STACK")
  while not test_stack.is_empty():
    item = test_stack.pop()
    print(f"-> {item}")