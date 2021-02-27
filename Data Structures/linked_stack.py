#Linked Stack
class Node: 
	def __init__(self, data): 
		self.data = data
		self.next = None

class Stack:
  def __init__(self): 
    self.head = None
  
  def push(self,data):
    if self.head is None:
      self.head = Node(data)
    else:
      newnode = Node(data)
      newnode.next = self.head
      self.head = newnode

  def pop(self):         
        if self.isEmpty():
            print("Stack Underflow")              
        else:
          print("Elemet popped is ",self.head.data)
          self.head = self.head.next

  def isEmpty(self):
    if self.head is None:
      return True
    else:
      return False

  def size(self):
    temp=self.head 
    count=0
    while temp is not None: 
      count=count+1
      temp=temp.next
    return count 

  def top(self):         
        if self.isEmpty():
            return None
        else:
            return self.head.data
     
  def display(self):        
      iternode = self.head
      if self.isEmpty():
          print("Stack Underflow")         
      else:             
          while(iternode != None):                 
              print(iternode.data,"->",end = " ")
              iternode = iternode.next     

stack = Stack()
print("Stack operations")
print("Stack is empty:",stack.isEmpty()) 
stack.push(12)
stack.push(23)
stack.push(34)
stack.push(45)
stack.push(56)
stack.push(67)
stack.display()
print("\nTop element is ",stack.top())
print("Size of the stack is ",stack.size())
stack.pop()
stack.pop()
print("After applying pop() two times")
stack.display()      
print("\nTop element is ",stack.top())
print("Size of the stack is ",stack.size())
print("Stack is empty:",stack.isEmpty())
stack.pop()
stack.pop()
stack.pop()
print("After applying pop() three times")
stack.display()
print("\nTop element is ",stack.top())
stack.pop()
print("Stack is empty:",stack.isEmpty())
