#Linked Queue
class Node: 
	def __init__(self, data): 
		self.data = data
		self.next = None
		
class Queue:
  def __init__(self): 
    self.head = None
    self.tail=None

  def enqueue(self, data): 
    if self.tail is None: 
      self.head =Node(data) 
      self.tail =self.head 
    else:
      self.tail.next = Node(data)
      self.tail = self.tail.next

  def dequeue(self): 
    if self.head is None: 
      print("Queue Underflow")  
    else:
        print("Element removed from the queue is ", self.head.data)
        self.head = self.head.next

  def first(self): 
    return self.head.data 

  def size(self): 
    temp=self.head 
    count=0
    while temp is not None: 
      count=count+1
      temp=temp.next
    return count 
	
  def isEmpty(self): 
    if self.head is None: 
      return True
    else: 
      return False
			
  def printqueue(self): 
    print("Queue elements are:") 
    temp=self.head 
    while temp is not None: 
      print(temp.data,end="->") 
      temp=temp.next
	
if __name__=='__main__': 
    queue = Queue() 
    print("Queue operations")
    queue.enqueue(24) 
    queue.enqueue(55) 
    queue.enqueue(68) 
    queue.enqueue(47)
    queue.enqueue(61) 
    queue.enqueue(72) 
    queue.printqueue() 
    print("\nFirst element is ",queue.first()) 
    print("Size of the queue is ",queue.size()) 
    queue.dequeue() 
    queue.dequeue() 
    print("After applying dequeue() two times")
    print("First element is ",queue.first())  
    queue.printqueue() 
    print("\nQueue is empty:",queue.isEmpty()) 
    queue.dequeue() 
    queue.dequeue()
    queue.dequeue() 
    print("After applying dequeue() three times")
    print("Size of the queue is ",queue.size())
    queue.printqueue()
    queue.dequeue()
    print("\nQueue is empty:",queue.isEmpty()) 
    queue.dequeue()
