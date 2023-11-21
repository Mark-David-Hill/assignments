# Should actually be classes

class DataCollection:
  def __init__(self):
    self.elements = []

  def add(self, item):
    self.elements.append(item)

  def pop(self):
    return None
  
  def size(self):
    return len(self.elements)

class Stack(DataCollection):
  def __init__(self):
    DataCollection.__init__(self)
    
  def pop(self):
    removed_item = self.elements.pop()
    return removed_item

class Queue(DataCollection):
  def __init__(self):
    DataCollection.__init__(self)

  def pop(self):
    removed_item = self.elements.pop(0)
    return removed_item
  
stack = Stack()

stack.add(1)
stack.add(2)
stack.add(3)
print(stack.elements)
print(stack.pop())
print(stack.pop())
print(stack.pop())

queue = Queue()

queue.add('a')
queue.add('b')
queue.add('c')
print(queue.elements)
print(queue.pop())
print(queue.pop())
print(queue.pop())