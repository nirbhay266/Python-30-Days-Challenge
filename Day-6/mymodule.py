# # What is a Module?
# # Consider a module to be the same as a code library.

# # A file containing a set of functions you want to include in your application.

#How to  Create a Module
# To create a module just save the code you want in a file with the file extension .py:

def greeting(name):
  print("Hello, " + name)

  #Now we can use the module we just created, by using the import statement:

greeting("Satya")


# Variables in Module
# The module can contain functions, as already described, but also variables of all 
# types (arrays, dictionaries, objects etc):

# Example
# Save this code in the file mymodule.py

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}