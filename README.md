# Learning Python

## Python Variables

A variable is a user-defined name stored in the memory for holding values. or It is a container for storing data values
e.g `x = 5`

- Variables do not need to declared with any particular type and can even change type after they have been set
- If you want to specify the data type of a variable, this can be done with **casting**
  e.g `x = str(3)` # x will be '3' not 3
- Varibale names are case-sensitive `a = 4` and `A = "Sally"` these are two different variables
- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and \_ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
- A variable name cannot be any of [Python reserved keywords](https://www.w3schools.com/python/python_ref_keywords.asp).
- Variable are sometimes declared using variable names in the format **camelCase**, **PascalCase**, **snake_case**
- Python allows you to assign values to multiple variables in one line
e.g 
```python
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
```
- You can assign the same value to multiple variables in one line
e.g
```python
x = y = z = "Orange"
print(x)
print(y)
print(z)

```
- If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. *This is called unpacking*.
```python
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
```
### Getting the type of a variable

You can use `type()` to get the type of a variable
e.g

```python
x = 5
print(type(x)) # This will print int
```

### Global Variables
- Variables that are created outside of a function these are known as global variables which means they can be accessed by everyone
- You can make a variable inside a function globally by the use of **global** keyword
e.g 
```python
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

```

## Python Data Types
Data Types this is the type of a value stored with the variable
There are different types of data which include
- str e.g `x = "Hello World"`
- int, float,complex e.g `x = 20`, `x = 1j`
- list, tuple, range e.g `x = ["apple", "banana", "cherry"]`, `x = ("apple", "banana", "cherry")`, `x = range(6)`
- dict e.g `x = {"name" : "John", "age" : 36}`
- set, frozenset e.g `x = {"apple", "banana", "cherry"}`,` x = frozenset({"apple", "banana", "cherry"})`
- bool e.g `x = True`
- bytes, bytearray, memoryview e.g `x = b"Hello"`, `x = bytearray(5)`, `x = memoryview(bytes(5))`
- NoneType e.g `x = None`

## isinstance 

`isinstance()` is a built-in function in Python that checks whether an object is an instance of a particular class or data type, or any of a tuple of classes and types. It's a versatile tool used for type checking, ensuring that variables or objects adhere to expected types within code, which is crucial for maintaining code reliability and avoiding type-related errors in dynamically typed languages like Python

```python
isinstance(object, classinfo)
```

  - **object**: The variable or object to be checked.
  - **classinfo**: A single class, data type, or a tuple of classes and types to check against the object.
**Returns**
  - True if object is an instance or subclass of classinfo, or if object is one of the types in classinfo when it's a tuple.
  - False otherwise.


## Python Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

### Properties and Methods related to Strings

- Multiline Strings: You can assign a multiline string to a variable by using three quotes:
- Strings are Arrays: This means you can use indexing on string e.g `name = "John"` => `name[0]` would be **J**
- len(): e.g:
```python
a = "Hello, World!"
print(len(a))
```
- Check String: To check if a certain phrase or character is present in a string, we can use the keyword **in**. e.g
```python
txt = "The best things in life are free!"
print("free" in txt)
```
- Check if NOT: To check if a certain phrase or character is NOT present in a string, we can use the keyword **not in**.
- Slicing Strings: You can return a range of characters by using the slice syntax. Specify the start index and the end index, separated by a colon, to return a part of the string.
e.g 
```python
b = "Hello, World!"
print(b[2:5]) # result: llo
```
**Note**: You can as well slice from start by just doing `b[:5]` and also you can slice up to the end by `b[2:]`. **Negative Indexing**, you can use negative indexes to start the slice from the end of the string by `b[-5:-2]`
- Upper case: `str.upper()`
- Lower case: `str.lower()`
- Remove whitespace: `str.strip()`, this method removes any whitespace from the beginning or the end
- Replace string: The `replace()` method replaces a string with another string:
e.g 
```python
a = "Hello, World!"
print(a.replace("H", "J")) # result: Jello, World!
```
- Split string: The `split()` method returns a list where the text between the specified separator becomes the list items. e.g
```python
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
```
- String concatenation: To concatenate, or combine, two strings you can use the **+** operator. e.g
```python
a = "Hello"
b = "World"
c = a + b
print(c) # result: HelloWorld
```
- String formating using **F-Strings**
e.g 

```python
age = 36
txt = f"My name is John, I am {age}"
print(txt)
```
- Placeholders and Modifiers: A placeholder can contain variables, operations, functions, and modifiers to format the value.
**Examples**
1. Add a placeholder for the price variable:
```python
price = 59
txt = f"The price is {price} dollars"
print(txt)
```
A placeholder can include a modifier to format the value.

A modifier is included by adding a colon **:** followed by a legal formatting type, like **.2f** which means fixed point number with *2 decimals*:

e.g 
```python
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
```
A placeholder can contain Python code, like math operations:
```python
txt = f"The price is {20 * 59} dollars"
print(txt)
```
- Escape Characters: 
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash `\` followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

**Summary of All Methods**
1. `capitalize()`: Converts the first character to upper case.
2. `casefold()`: Converts the string into lower case.
3. `center()`: Returns a centered string.
4. `count()`: Returns the number of times a specified value occurs in a string.
5. `encode()`: Returns an encoded version of the string.
6. `endswith()`: Returns true if the string ends with the specified value.
7. `expandtabs()`: Sets the tab size of the string.
8. `find()`: Searches the string for a specified value and returns the position of where it was found.
9. `format()`: Formats specified values in a string.
10. `format_map()`: Formats specified values in a string.
11. `index()`: Searches the string for a specified value and returns the position of where it was found.
12. `isalnum()`: Returns True if all characters in the string are alphanumeric.
13. `isalpha()`: Returns True if all characters in the string are in the alphabet.
14. `isascii()`: Returns True if all characters in the string are ASCII characters.
15. `isdecimal()`: Returns True if all characters in the string are decimals.
16. `isdigit()`: Returns True if all characters in the string are digits.
17. `isidentifier()`: Returns True if the string is an identifier.
18. `islower()`: Returns True if all characters in the string are lower case.
19. `isnumeric()`: Returns True if all characters in the string are numeric.
20. `isprintable()`: Returns True if all characters in the string are printable.
21. `isspace()`: Returns True if all characters in the string are whitespaces.
22. `istitle()`: Returns True if the string follows the rules of a title.
23. `isupper()`: Returns True if all characters in the string are upper case.
24. `join()`: Joins the elements of an iterable to the end of the string.
25. `ljust()`: Returns a left justified version of the string.
26. `lower()`: Converts a string into lower case.
27. `lstrip()`: Returns a left trim version of the string.
28. `maketrans()`: Returns a translation table to be used in translations.
29. `partition()`: Returns a tuple where the string is parted into three parts.
30. `replace()`: Returns a string where a specified value is replaced with a specified value.
31. `rfind()`: Searches the string for a specified value and returns the last position of where it was found.
32. `rindex()`: Searches the string for a specified value and returns the last position of where it was found.
33. `rjust()`: Returns a right justified version of the string.
34. `rpartition()`: Returns a tuple where the string is parted into three parts.
35. `rsplit()`: Splits the string at the specified separator, and returns a list.
36. `rstrip()`: Returns a right trim version of the string.
37. `split()`: Splits the string at the specified separator, and returns a list.
38. `splitlines()`: Splits the string at line breaks and returns a list.
39. `startswith()`: Returns true if the string starts with the specified value.
40. `strip()`: Returns a trimmed version of the string.
41. `swapcase()`: Swaps cases, lower case becomes upper case and vice versa.
42. `title()`: Converts the first character of each word to upper case.
43. `translate()`: Returns a translated string.
44. `upper()`: Converts a string into upper case.
45. `zfill()`: Fills the string with a specified number of 0 values at the beginning.
