from linked_list import Node

class Queue:
  def __init__(self):
      self.__size = 0
      self.__head = None
      self.__tail = self.__head
    
  def enqueue(self, item):
    node = Node(item)
        
    if self.is_empty():
        self.__head = node
        self.__tail = self.__head
    else:
      self.__tail.next_node = node
      self.__tail = self.__tail.next_node
            
    self.__size += 1

  def dequeue(self):
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

#---------------------------------------------------------------------
if False:
  collection = [10, 9, 8, 7 , 6]
  test_queue = Queue()
  
  print("ENQUEUE QUEUE")
  for item in collection:
    print(f"-> {item}")
    test_queue.enqueue(item)
  
  print("\nDEQUEUE QUEUE")
  while not test_queue.is_empty():
    item = test_queue.dequeue()
    print(f"-> {item}") 