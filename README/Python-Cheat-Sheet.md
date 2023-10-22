## Virtual Environments

Python virtual environments are self contained environments for a project. This is done for portability. 

This command makes the environment, replace venv_name with the name of your environment

``` python3 -m venv venv_name``` 

This command will activate the venv

```source venv_name/bin/activate```

This command will install packages needed in the venv

```pip install package_name```

This command will deactivate the environment

```deactivate```

## Classes and Objects

In Python, classes and objects are fundamental concepts that are used to implement object-oriented programming (OOP). Object-oriented programming is a programming paradigm that organizes code into reusable and modular units called classes, which define the structure and behavior of objects. Objects are instances of classes, and they represent specific instances or entities in your program.

### Classes:

A class is a blueprint or template for creating objects.
It defines the attributes (data) and methods (functions) that the objects of the class will have.
Classes are defined using the class keyword followed by the class name, and they are typically named using CamelCase conventions.
Example of a simple class definition:

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!" 
```

In the above example, we defined a Dog class with attributes name and breed, as well as a method bark.

### Objects:

Objects are instances of classes. They are created from a class and inherit the attributes and methods defined in that class.
You can create multiple objects from the same class, each with its own set of attribute values.
Example of creating objects from the Dog class:


```python
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

print(dog1.name)  # Output: Buddy
print(dog2.breed)  # Output: German Shepherd
print(dog1.bark())  # Output: Buddy says Woof!
```

In this example, dog1 and dog2 are two different objects of the Dog class.

Constructor (__init__):

The __init__ method is a special method (also called a constructor) that is called when an object of the class is created.
It is used to initialize the attributes of the object.
The self parameter refers to the instance of the object being created and is used to access and set object attributes.
Methods:

Methods are functions defined within a class, and they operate on the attributes of the class.
They can be called on objects to perform specific actions.
In the Dog class example, bark is a method that returns a string representing the dog's bark.

Python supports various OOP principles such as encapsulation, inheritance, and polymorphism, which allow you to create complex and modular code by organizing data and behavior into classes and objects.

Here's a brief overview of some important OOP concepts in Python:

Inheritance: It allows a class to inherit attributes and methods from another class. This promotes code reusability.

Encapsulation: It refers to restricting access to certain parts of an object and only exposing the necessary interfaces. This is often achieved using private and public attributes and methods.

Polymorphism: It allows objects of different classes to be treated as objects of a common superclass, enabling more flexible and abstract code.

Abstraction: It involves simplifying complex reality by modeling classes based on the essential properties and behaviors, while hiding unnecessary details.

For more see here: https://www.geeksforgeeks.org/python-classes-and-objects/

## Dictionaries


In Python, a dictionary is a built-in data type that is used to store collections of data in key-value pairs. It is also known as a "hash map" or "associative array" in other programming languages. Dictionaries are very versatile and widely used in Python for various tasks due to their efficient lookup and retrieval capabilities.

Here are some key characteristics and concepts related to dictionaries in Python:

### Key-Value Pairs

Each entry in a dictionary consists of a key and its corresponding value. The key is used to uniquely identify the associated value. Keys must be immutable (e.g., strings, numbers, or tuples), while values can be of any data type (including other dictionaries).

### Creating a Dictionary
You can create an empty dictionary using curly braces {} or by using the dict() constructor. Here's an example of both methods:

```python
# Using curly braces
my_dict = {}
```

Using the dict() constructor

```python
another_dict = dict()
```

Initializing with Key-Value Pairs: You can also create a dictionary with initial key-value pairs enclosed in curly braces:

```python
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
```

Accessing Values: You can access the values in a dictionary using square brackets [] and the key:

```python
name = my_dict['name']
```

If the key doesn't exist in the dictionary, it will raise a KeyError. To avoid this, you can use the get() method:

```python
name = my_dict.get('name', 'Default Name')
```

Modifying and Adding Elements: You can change the value associated with a key or add new key-value pairs to a dictionary like this:

```python
my_dict['age'] = 31  # Modifying an existing key
my_dict['country'] = 'USA'  # Adding a new key
```

Removing Elements: You can remove a key-value pair from a dictionary using the del statement or the pop() method:

```python
del my_dict['age']  # Removing a key-value pair by key
country = my_dict.pop('country')  # Removing and getting the value by key 
```

Iterating Through a Dictionary: You can loop through the keys, values, or key-value pairs in a dictionary using various methods like keys(), values(), and items():

```python

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)
```

### Checking for Key Existence

You can use the in keyword to check if a key exists in a dictionary:

```python
if 'name' in my_dict:
    print('Name exists in the dictionary.')
```

Dictionaries are widely used for tasks like storing configuration settings, counting occurrences of elements in a list, and building data structures like JSON objects due to their flexibility and efficiency in retrieving values by key.

For more see here: https://www.geeksforgeeks.org/python-dictionary/

## RegEx in Python

Regular expressions, often referred to as "regex" or "regexp," are a tool for pattern matching and text manipulation in Python. Python provides a built-in module called re for working with regular expressions.

### Import the re module

```python
import re
```

### Creating a Regular Expression Pattern

To use regex, you need to create a pattern that describes the text you want to match. Regular expression patterns are typically written as strings and can include a variety of special characters and metacharacters that have special meanings.

* . (dot): Matches any character except a newline.

* *: Matches zero or more occurrences of the preceding character or group.

* +: Matches one or more occurrences of the preceding character or group.

* ?: Matches zero or one occurrence of the preceding character or group.

* []: Defines a character class, allowing you to specify a set of characters to match.

* |: Acts as a logical OR operator.

* (): Groups characters or subpatterns together.

* ^: Matches the start of a string.

* $: Matches the end of a string.

* \: Escapes a metacharacter to match it literally.

### Using Regular Expressions

Once you have a pattern, you can use various functions from the re module to work with it.

re.search(pattern, string): Searches for the first occurrence of the pattern in the given string and returns a match object if found.

re.match(pattern, string): Matches the pattern only at the beginning of the string.

re.findall(pattern, string): Returns a list of all non-overlapping matches in the string.

re.finditer(pattern, string): Returns an iterator of match objects for all matches in the string.

re.sub(pattern, replacement, string): Replaces all occurrences of the pattern with the specified replacement text.

re.compile(pattern): Compiles a regular expression pattern into a regex object for better performance if you plan to use the same pattern multiple times.

Here's an example of using regex in Python to find and replace email addresses in a text

```python

import re

text = "Contact us at support@example.com or sales@example.net for assistance."

# Define a pattern to match email addresses
pattern = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'

# Find all email addresses in the text
matches = re.findall(pattern, text)

# Print the matched email addresses
for match in matches:
    print(match)
```

For more see here: https://docs.python.org/3/library/re.html
