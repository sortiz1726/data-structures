from stack import Stack
from queue import Queue

class BinaryNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
            
  def print_info(self):
    print(f"Data: {self.data}")
    if self.left is not None:
      print(f"left: {str(self.left.data)}")
    if self.right is not None:
      print(f"rigth: {str(self.right.data)}")

class Bst:
  def __init__(self):
    self.__root = None
  
  def insert(self, value):
    if self.__root is None:
      self.__root = BinaryNode(value)
      
    else:
      previous_node = None
      current_node = self.__root
      
      while previous_node is not current_node:
        previous_node = current_node
        
        if value < current_node.data:
          if current_node.left is None:
            current_node.left = BinaryNode(value)
            
          else:
            current_node = current_node.left
            
        else:
          if current_node.right is None:
            current_node.right = BinaryNode(value)
            
          else:
            current_node = current_node.right
                        
  def insert_recursive(self, value):
    self.__root = Bst.insert_recursive_helper(self.__root, value)
  
  @staticmethod
  def insert_recursive_helper(node, value):
    if node is None:
      return BinaryNode(value)
      
    if value < node.data:
      node.left = Bst.insert_recursive_helper(node.left, value)
      
    else:
      node.right = Bst.insert_recursive_helper(node.right, value)
      
    return node
        
  def contains(self, value):
    current_node = self.__root
    
    while current_node is not None and current_node.data != value:
      if value < current_node.data:
        current_node = current_node.left
        
      else:
        current_node = current_node.right
    
    return current_node is not None
  
  def contains_recursive(self, value):
    return self.contains_recursive_helper(self.__root, value)
      
  def contains_recursive_helper(self, node, value):
    if node is None:
      return False
    
    if value == node.data:
      return True
      
    elif value < node.data:
      return self.contains_recursive_helper(node.left, value)
      
    else:
      return self.contains_recursive_helper(node.right, value)  
  
  def remove(self, value):
    parent_node = None
    current_node = self.__root
    
    # Step 1: find the node that contains the value
    while current_node is not None and current_node.data != value:
      parent_node = current_node
      if value < current_node.data:
        current_node = current_node.left
        
      else:
        current_node = current_node.right
    
    # if no node is found then return
    if current_node is None:
      return

    # if current node has at most one child node (only when a node is leaf or has one child)
    if current_node.left is None or current_node.right is None:
      #set new node to be either the left or right of current node
      new_current = current_node.left if current_node.left is not None else current_node.right
      
      if current_node is self.__root:
        self.__root = new_current
        return
          
      #else it is some node in the tree
      if parent_node.left is current_node:
        parent_node.left = new_current
        
      else:
        parent_node.right = new_current
            
    else:
      parent_node = current_node
      min_node = parent_node.right
      
      while min_node.left is not None:
        parent_node = min_node
        min_node = min_node.left
          
      current_node.data = min_node.data
      
      if min_node is parent_node.left:
        parent_node.left = min_node.right
      else:
        parent_node.right = min_node.right 
    
  def remove_recursive(self, value):
    self.__root = Bst.remove_recursive_helper(self.__root, value)
  
  @staticmethod  
  def remove_recursive_helper(node, value):
    if node is None:
      return node
        
    if value < node.data:
      node.left = Bst.remove_recursive_helper(node.left, value)
      
    elif value > node.data:
      node.right = Bst.remove_recursive_helper(node.right, value)
      
    else:
      if node.left is None:
        return node.right
          
      if node.right is None:
        return node.left
          
      temp = node
      node = Bst.get_min(temp.right)
      node.right = Bst.remove_min(temp.right)
      node.left = temp.left
    
    return node
  
  @staticmethod
  def get_min(node):
    if node.left is None:
      return node
    else:
      return Bst.get_min(node.left)
  
  @staticmethod
  def remove_min(node):
    if node.left is None:
      return node.right
    else:
      node.left = Bst.remove_min(node.left)
    
  def print_rows(self):
    if self.__root == None:
      return
    print("----------------------------")
    node_queue = Queue()
    node_queue.enqueue(self.__root)
    
    node_row = []
    row = 0
    current_row_count = 1
    next_row_count = 0
    
    while not node_queue.is_empty():
      node = node_queue.dequeue()
      
      if node.left is not None:
                node_queue.enqueue(node.left)
                if current_row_count > 0:
                    next_row_count += 1
      if node.right is not None:
                node_queue.enqueue(node.right)
                if current_row_count > 0:
                    next_row_count += 1
              
      current_row_count -= 1
      node_row.append(str(node.data))
      
      if current_row_count == 0:
                print(f"row {row}: {' '.join(node_row)}")
                node_row.clear()
                row += 1
                current_row_count = next_row_count
                next_row_count = 0
    
    if len(node_row) > 0:       
      print(f"row {row}: {' '.join(node_row)}")
  
  def print_bfs(self):
    print("------- bfs order -------")
    node_queue = Queue()
    node_queue.enqueue(self.__root)
    
    while not node_queue.is_empty():
            current_node = node_queue.dequeue()
            
            if current_node is not None:
                node_queue.enqueue(current_node.left)
                node_queue.enqueue(current_node.right)
                print(current_node.data)
  
  def print_dfs_preorder(self):
    print("------- dfs predorder -------")
    node_stack = Stack()
    node_stack.push(self.__root)
    
    while not node_stack.is_empty():
            current_node = node_stack.pop()
            
            if current_node is not None:
                print(current_node.data)  
                node_stack.push(current_node.right)
                node_stack.push(current_node.left)
              
  def print_dfs_inorder(self):
    print("------- dfs inorder -------")            
    node_stack = Stack()
    node_stack.push(self.__root)

    while not node_stack.is_empty():
      current_node = node_stack.pop()
            
      # add all left most nodes
      while current_node is not None:
                node_stack.push(current_node)
                current_node = current_node.left

      # if there were left node added then...
      if current_node is None and not node_stack.is_empty():
        # pop it from the stack and print
        current_node = node_stack.pop()
        print(current_node.data)
        # point to the right node to be process later on...
        node_stack.push(current_node.right)
  
  def print_dfs_postorder(self):
    print("------- dfs postorder -------")
    print_stack = Stack()
    helper_stack = Stack()
    
    helper_stack.push(self.__root)
    
    while not helper_stack.is_empty():
      current_node = helper_stack.pop()
      
      if current_node is not None:
                print_stack.push(current_node)
                helper_stack.push(current_node.left)
                helper_stack.push(current_node.right)
            
    while not print_stack.is_empty():
      current_node = print_stack.pop()
      print(current_node.data)
      
  def print_dfs_recursive(self):
    Bst.print_dfs_recursive_helper(self.__root)  
  
  @staticmethod
  def print_dfs_recursive_helper(node):
    if node is not None:
      Bst.print_dfs_recursive_helper(node.left)
      Bst.print_dfs_recursive_helper(node.right)
      print(node.data)

print("PRINT BST")
bst_it = Bst()
bst_recurse = Bst()
collection = [8, 3, 10, 1, 6, 14, 4, 7, 13]
#collection = [8, 3, 10, 1, 6, 14, 4]
for item in collection:
    bst_it.insert(item)
    bst_recurse.insert_recursive(item)

bst_it.print_rows()
bst_recurse.print_rows()

for item in collection: 
    #print(f"Does contain {item}? {'Yes' if bst_it.contains(item) else 'No'}")
    #print(f"Does contain {item}? {'Yes' if bst_recurse.contains_recursive(item) else 'No'}")
    pass
    
for item in collection:
    bst_it.remove(item)
    bst_recurse.remove_recursive(item)
    
bst_it.print_rows()
bst_recurse.print_rows()