#- Implement a stack with push, pop, and peek
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if self.is_empty():
            return "Stack is empty. Cannot pop."
        return f"Popped: {self.items.pop()}"

    def peek(self):
        if self.is_empty():
            return "Stack is empty. Nothing to peek."
        return f"Top Element: {self.items[-1]}"

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack from bottom to top:", self.items)

#Testing the Stack
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.peek())      # Should print top element (30)
print(s.pop())       # Should remove and return 30
print(s.peek())      # Should now be 20
s.display()
