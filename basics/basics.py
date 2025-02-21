# How to write comments in Python

"""
This
is
a
multi-line
comment
"""

# Comparing two numbers
first_number = 2
second_number = 5

# Checking if first_number is greater than second_number
if first_number > second_number:
    print(str(first_number) + " is greater than " + str(second_number))  # Prints when the first number is greater
elif first_number == second_number:
    print(str(first_number) + " is equal to " + str(second_number))  # Prints when both numbers are equal
else:
    print(str(first_number) + " is less than " + str(second_number))  # Prints when the first number is less

# Type conversion examples
a = int(5)  # Converting the number 5 to an integer
b = str(5)  # Converting the number 5 to a string
c = float(5)  # Converting the number 5 to a float

# Printing the values of the variables
print(a)  # Prints the integer value
print(b)  # Prints the string value
print(c)  # Prints the float value

# Printing the data types of the variables
print(type(a))  # Shows the type of 'a' (int)
print(type(b))  # Shows the type of 'b' (str)
print(type(c))  # Shows the type of 'c' (float)

# Assigning values to variables
a = 5  # Integer assignment
A = "Mehedi"  # String assignment

# Printing the values of the variables
print(a)  # Prints the value of 'a' (5)
print(A)  # Prints the value of 'A' ("Mehedi")

# Multiple variable assignment
x, y, z = "Orange", "Banana", "Cherry"  # Assigning multiple values to variables in a single line

# Printing the values of the variables
print(x)  # Prints the value of 'x' ("Orange")
print(y)  # Prints the value of 'y' ("Banana")
print(z)  # Prints the value of 'z' ("Cherry")
