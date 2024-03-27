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

