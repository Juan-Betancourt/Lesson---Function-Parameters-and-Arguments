# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#   print("Hello")
#   print("How do you do?")
#   print("How is the weather today?")
# greet()

#Functions that allow for input
# def greet_with_name(name):
#   print(f"Hello {name}")
#   print(f"How do you do {name}?")

# greet_with_name("Aldriana")

#Functions that allow more than one input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}")

# greet_with("Tim", "Florida")

greet_with(location = "Florida", name = "Johnny")