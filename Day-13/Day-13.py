# Stacks
# A stack is a data structure that can hold many elements, and the last element added is the first one to be removed.

# Like a pile of pancakes, the pancakes are both added and removed from the top. So when removing a pancake, it will always be the last pancake you added. This way of organizing elements is called LIFO: Last In First Out.

# Basic operations we can do on a stack are:

# Push: Adds a new element on the stack.
# Pop: Removes and returns the top element from the stack.
# Peek: Returns the top (last) element on the stack.
# isEmpty: Checks if the stack is empty.
# Size: Finds the number of elements in the stack.
# Stacks can be implemented by using arrays or linked lists.

# Stacks can be used to implement undo mechanisms, to revert to previous states, to create algorithms for depth-first search in graphs, or for backtracking.

# Stacks are often mentioned together with Queues, which is a similar data structure described on the next page.

# Stack Implementation using Python Lists
# For Python lists (and arrays), a stack can look and behave like this:
stack = []
stack.append("A")  # Push A onto the stack
stack.append("B")  # Push B onto the stack  
stack.append("C")  # Push C onto the stack
print(stack)  # Output: ['A', 'B', 'C']

# Pop the top element from the stack
top_element = stack.pop()  # Removes and returns 'C'
print("Pop",top_element)  # Output: C
print(stack)  # Output: ['A', 'B']
stack.append("C")  # Push D onto the stack
stack.append("D")  # Push D onto the stack
print(stack)  # Output: ['A', 'B', 'C', 'D']

# Peek the top element without removing it
top_element = stack[-1]  # Returns 'B' without removing it
print("Peek",top_element)  # Output: B
top_element = stack[-2]  # Returns 'C' without removing it
print("Peek",top_element)  # Output: C

#isEmpty check
isEmpty=not bool(stack)  # Returns True if the stack is empty
print("Is stack empty?", isEmpty)  # Output: False

# Size of the stack
size = len(stack)  # Returns the number of elements in the stack
print("Size of stack:", size)  # Output: 4
# Clear the stack
stack.clear()  # Removes all elements from the stack
print("Stack after clearing:", stack)  # Output: [] 

# While Python lists can be used as stacks, creating a dedicated Stack class provides better encapsulation and 
# additional functionality:
class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

s= Stack()
s.push("A")  # Push A onto the stack
s.push("B")  # Push B onto the stack
s.push("C")  # Push C onto the stack
print(s.items)  # Output: ['A', 'B', 'C']
# Pop the top element from the stack
top_element = s.pop()  # Removes and returns 'C'
print("Pop", top_element)  # Output: C
print(s.items)  # Output: ['A', 'B']
s.push("D")  # Push D onto the stack
s.push("E")  # Push E onto the stack
print(s.items)  # Output: ['A', 'B', 'D', 'E']
# Peek the top element without removing it
top_element = s.peek()  # Returns 'E' without removing it
print("Peek", top_element)  # Output: E
# isEmpty check
isEmpty = s.is_empty()  # Returns False if the stack is not empty
print("Is stack empty?", isEmpty)  # Output: False
# Size of the stack
size = s.size()  # Returns the number of elements in the stack
print("Size of stack:", size)  # Output: 4
# Clear the stack


############################################### Queues ############################################################
# Think of a queue as people standing in line in a supermarket.

# The first person to stand in line is also the first who can pay and leave the supermarket.

# Basic operations we can do on a queue are:

# Enqueue: Adds a new element to the queue.
# Dequeue: Removes and returns the first (front) element from the queue.
# Peek: Returns the first element in the queue.
# isEmpty: Checks if the queue is empty.
# Size: Finds the number of elements in the queue.
# Queues can be implemented by using arrays or linked lists.

# Queues can be used to implement job scheduling for an office printer, order processing for e-tickets, or to create algorithms for breadth-first search in graphs.

# Queues are often mentioned together with Stacks, which is a similar data structure described on the previous page

queue = []
# Enqueue elements to the queue
queue.append("A")  # Enqueue A
queue.append("B")  # Enqueue B
queue.append("C")  # Enqueue C
print(queue)  # Output: ['A', 'B', 'C']
# Peek
frontElement = queue[0]  # Returns 'A' without removing it
print("Peek", frontElement)  # Output: A
# Dequeue the first element from the queue
dequeuedElement = queue.pop(0)  # Removes and returns 'A'
print("Dequeue", dequeuedElement)  # Output: A
# isEmpty
isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

# Size
print("Size: ", len(queue))

#Implementing a Queue Class
class Queue:
  def __init__(self):
    self.queue = []
    
  def enqueue(self, element):
    self.queue.append(element)

  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue.pop(0)

  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue[0]

  def isEmpty(self):
    return len(self.queue) == 0

  def size(self):
    return len(self.queue)

# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue: ", myQueue.queue)
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("Queue after Dequeue: ", myQueue.queue)
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())


















