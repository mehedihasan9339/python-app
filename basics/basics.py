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


x = y = z = "Orange"  # Assigning the same value to multiple variables in a single line
print(x)  # Prints the value of 'x' ("Orange")
print(y)  # Prints the value of 'y' ("Orange")
print(z)  # Prints the value of 'z' ("Orange")

# Global variables
x = "awesome"  # Declaring a global variable
def my_function():  # Defining a function
    print("Python is " + x)  # Accessing the global variable inside the function
my_function()  # Calling the function

# Local variables
def my_function():  # Defining a function
    y = "fantastic"  # Declaring a local variable
    print("Python is " + y)  # Accessing the local variable inside the function
my_function()  # Calling the function

# Global and local variables
x = "awesome"  # Declaring a global
def my_function():  # Defining a function
    x = "fantastic"  # Declaring a local variable with the same name as the global variable
    print("Python is " + x)  # Accessing the local variable inside the function
my_function()  # Calling the function
print("Python is " + x)  # Accessing the global variable

# Using the global keyword
x = "awesome"  # Declaring a global variable
def my_function():  # Defining a function
    global x  # Using the global keyword to access the global variable
    x = "fantastic"  # Changing the value of the global variable
my_function()  # Calling the function
print("Python is " + x)  # Accessing the global variable

# Using the global keyword to change a global variable inside a function
x = "awesome"  # Declaring a global
def my_function():  # Defining a function
    global x  # Using the global keyword to access the global variable
    x = "fantastic"  # Changing the value of the global variable
my_function()  # Calling the function
print("Python is " + x)  # Accessing the global variable

# Unpack a collection
fruits = ["apple", "banana", "cherry"] # Creating a list
x, y, z = fruits # Unpacking the list into three variables
print(x) # Prints the value of 'x' ("apple")
print(y) # Prints the value of 'y' ("banana")
print(z) # Prints the value of 'z' ("cherry")

# Output of multiple variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z) # Prints the values of the variables separated by a space

# Output of multiple variables with a separator
x = "Python"
y = "is"
z = "awesome"
print(x, y, z, sep="-") # Prints the values of the variables separated by a hyphen

# Output of multiple variables with an end parameter
x = "Python"
y = "is"
z = "awesome"
print(x, end=" ") # Prints the value of 'x' followed by a space


# Output of multiple variables with a plus operator
x = "Python "
y = "is "
z = "awesome"
print(x + y + z) # Prints the values of the variables concatenated together

# Output of multiple variables with a plus operator (it works as a math operator)
x = 5
y = 10
print(x + y) # Prints the sum of 'x' and 'y' (15)

# Output of multiple variables seperates with a comma
x = 5
y = "John"
print(x, y) # Prints the values of 'x' and 'y' separated by a comma

# Python data types
# Integers
x = 5
print(type(x)) # Shows the type of 'x' (int)
# Floats
x = 5.5
print(type(x)) # Shows the type of 'x' (float)
# Complex numbers
x = 1j
print(type(x)) # Shows the type of 'x' (complex)
# Strings
x = "Hello, World!"
print(type(x)) # Shows the type of 'x' (str)
# Lists
x = ["apple", "banana", "cherry"]
print(type(x)) # Shows the type of 'x' (list)
# Tuples
x = ("apple", "banana", "cherry")
print(type(x)) # Shows the type of 'x' (tuple)
# Dictionaries
x = {"name" : "John", "age" : 36}
print(type(x)) # Shows the type of 'x' (dict)
# Sets
x = {"apple", "banana", "cherry"}
print(type(x)) # Shows the type of 'x' (set)
# Booleans
x = True
print(type(x)) # Shows the type of 'x' (bool)
# Bytes
x = b"Hello"
print(type(x)) # Shows the type of 'x' (bytes)
# Byte Arrays
x = bytearray(5)
print(type(x)) # Shows the type of 'x' (bytearray)
# Memory Views
x = memoryview(bytes(5))
print(type(x)) # Shows the type of 'x' (memoryview)


# Python Numbers
# Integers
x = 1
print(type(x)) # Shows the type of 'x' (int)
# Floats
x = 1.1
print(type(x)) # Shows the type of 'x' (float)
# Complex numbers
x = 1j
print(type(x)) # Shows the type of 'x' (complex)

# Python Casting
# Integers
x = int(1)
print(type(x)) # Shows the type of 'x' (int)
# Floats
x = float(1)
print(type(x)) # Shows the type of 'x' (float)
# Strings
x = str(1)
print(type(x)) # Shows the type of 'x' (str)

# Python Strings
# Strings
x = "Hello, World!"
print(x) # Prints the string
# Multiline Strings
x = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""
print(x) # Prints the multiline string
# Strings are Arrays
x = "Hello, World!"
print(x[1]) # Prints the second character of the string
# Slicing
x = "Hello, World!"
print(x[2:5]) # Prints the characters from position 2 to 5 (not included)
# Negative Indexing
x = "Hello, World!"
print(x[-1]) # Prints the last character of the string
# String Length
x = "Hello, World!"
print(len(x)) # Prints the length of the string
# String Methods
x = " Hello, World! "
print(x.strip()) # Removes any whitespace from the beginning or the end
print(x.lower()) # Converts a string into lowercase
print(x.upper()) # Converts a string into uppercase
print(x.replace("H", "J")) # Replaces a string with another string
print(x.split(",")) # Splits the string into substrings if it finds instances of the separator
# Check String
x = "Hello, World!"
print("World" in x) # Checks if a certain phrase is present in the string
# String Concatenation
x = "Hello"
y = "World"
z = x + y
print(z) # Prints the concatenated string
# String Format
age = 36
name = "John"
txt = "My name is {} and I am {}"
print(txt.format(name, age)) # Formats the string
# Escape Characters
txt = "We are the so-called \"Vikings\" from the north."
print(txt) # Prints the string with escape characters
# String Methods
a = "Hello, World!"
print(a[1]) # Returns the character at position 1
print(a[2:5]) # Returns the characters from position 2 to 5 (not included)
print(a.strip()) # Removes any whitespace from the beginning or the end
print(a.lower()) # Converts a string into lowercase
print(a.upper()) # Converts a string into uppercase
print(a.replace("H", "J")) # Replaces a string with another string
print(a.split(",")) # Splits the string into substrings if it finds instances of the separator
# Check String
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x) # Returns True if the phrase is present in the string, otherwise False
# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c) # Concatenates two strings

# Python Booleans
# Booleans
print(10 > 9) # Returns True because 10 is greater than 9
print(10 == 9) # Returns False because 10 is not equal to 9
print(10 < 9) # Returns False because 10 is not less than 9
# Evaluate Values and Variables
print(5 > 9) # Returns False because 5 is not greater than 9

# Python Operators
# Arithmetic Operators
x = 5
y = 3
print(x + y) # Addition
print(x - y) # Subtraction
print(x * y) # Multiplication
print(x / y) # Division
print(x % y) # Modulus (Remainder)
print(x ** y) # Exponentiation (Power)
print(x // y) # Floor division
# Assignment Operators
x = 5
y = 10
print(x + y) # Addition
x += 3
print(x) # Addition
x -= 3
print(x) # Subtraction
# Comparison Operators
x = 5
y = 3
print(x == y) # Equal to
print(x != y) # Not equal to
print(x > y) # Greater than
print(x < y) # Less than
print(x >= y) # Greater than or equal to
print(x <= y) # Less than or equal to
# Logical Operators
x = 5
y = 3
print(x > 2 and x < 10) # Returns True because 5 is greater than
print(x > 2 or x < 4) # Returns True because one of the conditions are True
print(not(x > 2 and x < 10)) # Reverse the result, returns False
# Identity Operators
x = 5
y = 5
print(x is y) # Returns True because both variables are the same object
print(x is not y) # Returns False because both variables are the same object
# Membership Operators
x = 5
y = 3
list = [1, 2, 3, 4, 5]
print(x in list) # Returns True because a sequence with the value is present in the list
print(y not in list) # Returns True because a sequence with the value is not present in the list
# Bitwise Operators
x = 5
y = 3
print(x & y) # Bitwise AND
print(x | y) # Bitwise OR
print(x ^ y) # Bitwise XOR
print(~x) # Bitwise NOT
print(x << 2) # Bitwise left shift
print(x >> 2) # Bitwise right shift

# Python Lists
# Lists
thislist = ["apple", "banana", "cherry"]
print(thislist) # Prints the list
# List Indexing
print(thislist[0]) # Prints the first item in the list
# Negative Indexing
print(thislist[-1]) # Prints the last item in the list
# Range of Indexes
print(thislist[1:3]) # Prints the second and third items in the list
# Change Item Value
thislist[1] = "blackcurrant"
print(thislist) # Changes the second item in the list
# Loop Through a List
for x in thislist:
    print(x) # Prints each item in the list
# Check if Item Exists
if "apple" in thislist:
    print("Yes, 'apple' is in the list") # Prints Yes, 'apple'
# List Length
print(len(thislist)) # Prints the number of items in the list
# Add Items
thislist.append("orange")
print(thislist) # Adds an item to the end of the list
# Add Items at a Specific Index
thislist.insert(1, "orange")
print(thislist) # Adds an item at the specified index
# Remove Item
thislist.remove("banana")
print(thislist) # Removes the specified item
# Remove Item by Index
thislist.pop(1)
print(thislist) # Removes the specified index
# Empty the List
thislist.clear()
print(thislist) # Clears the list
# Copy a List
mylist = thislist.copy()
print(mylist) # Copies the list
# Join Two Lists
list1 = ["a", "b", "c"]
list2 = ["d", "e", "f"]
list3 = list1 + list2
print(list3) # Joins two lists
# Append List2 to List1
list1 = ["a", "b", "c"]
list1.extend(list2)
print(list1) # Appends list2 to list1
# List Methods
# List Methods
thislist = ["apple", "banana", "cherry"]
thislist.append("orange") # Adds an item to the end of the list
thislist.insert(1, "orange") # Adds an item at the specified index
thislist.remove("banana") # Removes the specified item
thislist.pop(1) # Removes the specified index
thislist.clear() # Clears the list
mylist = thislist.copy() # Copies the list
list1 = ["a", "b", "c"]
list2 = ["d", "e", "f"]
list1.extend(list2) # Appends list2 to list1
# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) # Returns the fruits containing the letter "a"

# Python Tuples
# Tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple) # Prints the tuple
# Tuple Indexing
print(thistuple[1]) # Prints the second item in the tuple
# Negative Indexing
print(thistuple[-1]) # Prints the last item in the tuple
# Range of Indexes
print(thistuple[1:3]) # Prints the second and third items in the tuple
# Change Tuple Values
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y[1] = "kiwi"
thistuple = tuple(y)
print(thistuple) # Changes the second item in the tuple
# Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x) # Prints each item in the tuple
# Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the tuple") # Prints Yes, 'apple'
# Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) # Prints the number of items in the tuple
# Add Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple) # Adds an item to the end of the tuple
# Remove Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple) # Removes the specified item
# Delete Tuple
thistuple = ("apple", "banana", "cherry")
del thistuple # Deletes the tuple
# Join Two Tuples
tuple1 = ("a", "b", "c")
tuple2 = ("d", "e", "f")
tuple3 = tuple1 + tuple2
print(tuple3) # Joins two tuples
# Tuple Methods
# Tuple Methods
# count()
# index()

# Python Sets
# Sets  (unordered and unindexed)
thisset = {"apple", "banana", "cherry"}
print(thisset) # Prints the set
# Access Items
for x in thisset:
    print(x) # Prints each item in the set
# Check if Item Exists
if "apple" in thisset:
    print("Yes, 'apple' is in the set") # Prints Yes, 'apple'
    # Add Items
thisset.add("orange")
print(thisset) # Adds an item to the set
# Add Multiple Items
thisset.update(["orange", "mango", "grapes"])
print(thisset) # Adds multiple items to the set
# Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset)) # Prints the number of items in the set
# Remove Item
thisset.remove("banana")
print(thisset) # Removes the specified item
# Remove Item with discard()
thisset.discard("banana")
print(thisset) # Removes the specified item
# Remove the Last Item
x = thisset.pop()
print(x) # Removes the last item
# Empty the Set
thisset.clear()
print(thisset) # Removes all items from the set
# Delete the Set
del thisset
# Join Two Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) # Joins two sets
# Join Two Sets with update()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1) # Joins two sets
# Set Methods
# add()
# clear()
# copy()
# discard()
# difference()
# difference_update()
# discard()
# intersection()
# intersection_update()
# isdisjoint()
# issubset()
# issuperset()
# pop()
# remove()
# symmetric_difference()
# symmetric_difference_update()
# union()
# update()

# Python Dictionaries
# Dictionaries
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict) # Prints the dictionary
# Accessing Items
x = thisdict["model"]
print(x) # Accesses the value of the specified key
# Get the Value of the "model" Key
x = thisdict.get("model")
print(x) # Accesses the value of the specified key
# Change Values
thisdict["year"] = 2018
print(thisdict) # Changes the value of the specified key
# Loop Through a Dictionary
for x in thisdict:
    print(x) # Prints all key names in the dictionary
for x in thisdict:
    print(thisdict[x]) # Prints all values in the dictionary
for x in thisdict.values():
    print(x) # Prints all values in the dictionary
for x, y in thisdict.items():
    print(x, y) # Prints all key-value pairs in the dictionary
# Check if Key Exists
if "model" in thisdict:
    print("Yes, 'model' is present in the dictionary") # Checks if the specified key
# Dictionary Length
print(len(thisdict)) # Prints the number of items in the dictionary
# Adding Items
thisdict["color"] = "red"
print(thisdict) # Adds a new key-value pair to the dictionary
# Removing Items
thisdict.pop("model")
print(thisdict) # Removes the specified key
# Copying a Dictionary
thisdict = thisdict.copy()
print(thisdict) # Copies the dictionary
# Nested Dictionaries
thisdict = {
    "name": "John",
    "age": 36,
    "city": {
        "country": "USA",
        "state": "California"
        }
        }
print(thisdict) # Creates a nested dictionary
# Dictionary Methods
# clear()
# copy()
# fromkeys()
# get()
# items()
# keys()
# pop()
# popitem()
# setdefault()
# update()
# values()

# Python If...Else
# If Statement
a = 33
if a > 10:
    print("a is greater than 10") # Checks if the condition is true
# If-Else Statement
a = 33
b = 200
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a") # Checks if the condition is true
# Elif Statement
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
# Else Statement
a = 33
b = 200
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
# Short Hand If
a = 200
b = 33
print("A") if a > b else print("B") # Checks if the condition is
# If-Else Ladder
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
# And
a = 33
b = 33
if a > b and b == a:
    print("Both conditions are True")
# Or
a = 33
b = 33
if a > b or b == a:
    print("At least one condition is True")
# Nested If
a = 33
b = 33
if a > b:
    print("a is greater than b")
    if a == b:
        print("a and b are equal")
# Pass Statement
a = 33
b = 33
if b > a:
    pass # Does nothing
else:
    print("b is not greater than a")

# Python While Loops
# While Loop
i = 1
while i < 6:
    print(i)
    i += 1
# Break Statement
i = 1
while i < 6:
    if i == 3:
        break
    print(i)
    i += 1
# Continue Statement
i = 0
while i < 6:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
# Else Statement
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)
# Pass Statement
for x in [
    "apple",
    "banana",
    "cherry"
]:
    pass

# Python For Loops
# For Loop
# For Loop with Range
for x in range(6):
    print(x)
# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)
# Break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break

# Continue Statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
# Else Statement
for x in range(6):
    print(x)
else:
    print("Finally finished!")
# Pass Statement
for x in [
    "apple",
    "banana",
    "cherry"
]:
    pass

# Python Functions
# Creating a Function
def greet(name):
    print("Hello, " + name)
# Calling a Function
greet("John")
# Arguments
def greet(name):
    print("Hello, " + name)
greet("John")
# Return Values
def greet(name):
    return "Hello, " + name
print(greet("John"))
# Lambda Functions
def greet(name):
    return "Hello, " + name
print(greet("John"))
# Lambda Function
x = lambda a: a + 10

# Python Lambda
# Lambda Function
x = lambda a: a + 10
print(x(5))
# Lambda Function with Multiple Arguments
x = lambda a, b: a + b
print(x(5, 10))
# Lambda Function with Multiple Arguments
x = lambda a, b, c: a + b + c
print(x(5, 10, 15))
# Why Use Lambda Functions?
def myfunc(n):
    return lambda a: a * n
# Lambda Function with Default Argument
x = lambda a, b, c=1: a + b + c
print(x(5, 10))

# Python Classes and Objects
# Creating a Class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print("Woof!")
# Creating an Object
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print("Woof!")

# Python Inheritance
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print("Woof!")
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def bark(self):
        print("Woof!")

# Python Iterators
# Creating an Iterator
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
        def __iter__(self):
            return self
        def __next__(self):
            if self.index < len(self.data):
                result = self.data[self.index]
                self.index += 1
                return result
            else:
                raise StopIteration()
# Using the Iterator
data = ["apple", "banana", "cherry"]
my_iterator = MyIterator(data)
for item in my_iterator:
    print(item)

# Python Modules
# Importing a Module
import math
print(math.pi)
# Using the Module
# Creating a Module
def greet(name):
    print("Hello, " + name)
    
# Python Dates
# Importing the datetime Module
import datetime
x = datetime.datetime.now()
print(x)

# Python Math
# Importing the math Module
import math
print(math.pi)
# Math Functions
# abs() - Returns the absolute value of a number
# ceil() - Returns the smallest integer not less than the given number
# floor() - Returns the largest integer not greater than the given number
# log() - Returns the natural logarithm of a number
# max() - Returns the largest number in a list
# min() - Returns the smallest number in a list
# pow() - Returns the value of x to the power of y

# Python JSON
# Importing the json Module
import json
# JSON Data
data = {'name': 'John', 'age': 30, 'city': 'New York' }
# Converting Python to JSON
json_data = json.dumps(data)
print(json_data)
# Converting JSON to Python
python_data = json.loads(json_data)
print(python_data)

# Python RegEx
# Importing the re Module
import re
# RegEx Pattern
# ^ matches the start of a string
# $ matches the end of a string
# . matches any character
# \d matches any digit
# \D matches any non-digit
# \s matches any whitespace
# \S matches any non-whitespace
# \w matches any alphanumeric character
# \W matches any non-alphanumeric character
# [abc] matches 'a' or 'b' or 'c'
# [a-z] matches any lowercase letter
# [A-Z] matches any uppercase letter
# [a-zA-Z] matches any letter
# [0-9] matches any digit
# [^abc] matches any character except 'a' or 'b' or 'c'

# Python XML
# Importing the xml.etree.ElementTree Module
import xml.etree.ElementTree as ET
# Parsing an XML File
# root = ET.parse('example.xml').getroot()
# root = ET.fromstring(xml_string)
# root = ET.ElementTree(xml_string)
# root = ET.fromstring(xml_string)

# Python PIP
# Installing a Package
# pip install package_name
# Uninstalling a Package
# pip uninstall package_name
# Listing Installed Packages
# pip list
# Using a Requirements File
# pip install -r requirements.txt
# Creating a Requirements File
# pip freeze > requirements.txt

# Python Try...Except
try:
    # Code to be executed
    print(x)
except:
    # Code to be executed if an error occurs
    print("An exception occurred")

# Python User Input
username = input("Enter username:")
print("Username is: " + username)

# Python String Formatting
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
# Output: The price is 49 dollars

# Python File Handling
# Opening a File
f = open("demofile.txt", "r")
print(f.read())
# Closing a File
f.close()

# Python Read Files
# Reading a File
f = open("demofile.txt", "r")
print(f.read())
# Reading Only Parts of a File
f = open("demofile.txt", "r")
print(f.read(5))
# Reading Lines
f = open("demofile.txt", "r")
print(f.readline())
# Reading Multiple Lines
f = open("demofile.txt", "r")
print(f.readline())

# Python Write/Create Files
# Writing to an Existing File
f = open("demofile.txt", "a")
f.write("Now the file has more content!")
# Closing the File
f.close()

# Python Delete Files
# Deleting a File
import os
# Delete a file
os.remove("demofile.txt")
# Check if file exists
try:
    os.remove("demofile.txt")
except:
    print("The file does not exist")


