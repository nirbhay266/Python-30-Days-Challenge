# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the 
# methods __iter__() and __next__().


number=[2,4,6,8,10]
i=iter(number)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

#Even strings are iterable objects, and can return an iterator:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#We can also use a for loop to iterate through an iterable object:
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
    print(x)

# Custom Iterators:
# You can create your own iterator by defining a class that implements the __iter__() and __next__() methods.
class MyIterator:
    def __init__(self, max_value):
        self.current = 0
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max_value:
            self.current += 1
            return self.current
        else:
            raise StopIteration

# Using the custom iterator
my_iter = MyIterator(3)
for value in my_iter:
    print(value)  # Output: 1, 2, 3


# Generators in Python are a special type of iterable, like lists or tuples, but they generate items one at a time 
# and only when required, making them memory-efficient. They are defined using functions and the yield keyword.
# Key Features of Generators:
# Lazy Evaluation: They produce items on demand, which is useful for handling large datasets.
# State Retention: They maintain their state between calls, resuming execution from where they left off.
# Memory Efficiency: Unlike lists, they don’t store all items in memory.
# How to Create a Generator:
# Generators are created using functions with the yield keyword.

def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
for value in gen:
    print(value)

# You can also create generators using a syntax similar to list comprehensions, but with parentheses instead of
#  square brackets.

gen = (x * 2 for x in range(1, 4))
for value in gen:
    print(value)


