#Circular Queue
class CircularQueue:
  
  class Node:
    def __init__(self, element, next):
      self.element = element
      self.next = next

  def __init__(self):
    self.tail = None
    self.size = 0
  
  def len(self):
    return self.size
  
  def is_empty(self):
    return self.size == 0
  
  def first(self):
    if self.is_empty( ):
      raise Exception("Queue is empty ")
    head = self.tail.next
    return head.element

  def dequeue(self):
    if self.is_empty( ):
      raise Exception("Queue is empty")
    oldhead = self.tail.next
    if self.size == 1:
      self.tail = None 
    else:
      self.tail.next = oldhead.next
    self.size = self.size - 1
    return oldhead.element

  def enqueue(self, e):
    newest = self.Node(e, None)
    if self.is_empty( ):
      newest.next = newest
    else:
      newest.next = self.tail.next
      self.tail.next = newest
    self.tail = newest
    self.size += 1

  def rotate(self):
    if self.size > 0:
      self.tail = self.tail.next

if __name__=='__main__': 
    cqueue = CircularQueue()
    print("Circular Queue operations")
    cqueue.enqueue(24) 
    cqueue.enqueue(55) 
    cqueue.enqueue(68) 
    cqueue.enqueue(47)
    cqueue.enqueue(61) 
    cqueue.enqueue(72) 
    print("First element is ",cqueue.first()) 
    print("Size of the queue is ",cqueue.len()) 
    cqueue.dequeue() 
    cqueue.dequeue() 
    print("After applying dequeue() two times")
    cqueue.rotate()
    print("First element is ",cqueue.first())  
    print("Queue is empty:",cqueue.is_empty()) 
    cqueue.dequeue() 
    cqueue.dequeue()
    cqueue.dequeue() 
    print("After applying dequeue() three times")
    print("Size of the queue is ",cqueue.len())    
    cqueue.dequeue()
    print("Queue is empty:",cqueue.is_empty()) 
    cqueue.dequeue()
