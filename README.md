# Learning Python

## Python Variables

A variable is a user-defined name stored in the memory for holding values or a container for storing data values. For example: `x = 5`

- Variables do not need to be declared with any particular type and can even change type after they have been set.
- If you want to specify the data type of a variable, this can be done with **casting**.
  e.g., `x = str(3)` # x will be '3' not 3
- Variable names are case-sensitive. `a = 4` and `A = "Sally"` are two different variables.
- A variable name must start with a letter or the underscore character.
- A variable name cannot start with a number.
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and `_`).
- Variable names are case-sensitive (age, Age and AGE are three different variables).
- A variable name cannot be any of [Python reserved keywords](https://www.w3schools.com/python/python_ref_keywords.asp).
- Variables are sometimes declared using variable names in the format **camelCase**, **PascalCase**, or **snake_case**.
- Python allows you to assign values to multiple variables in one line.
  e.g., 
  ```python
  x, y, z = "Orange", "Banana", "Cherry"
  print(x)
  print(y)
  print(z)
  ```
- You can assign the same value to multiple variables in one line.
  e.g.,
  ```python
  x = y = z = "Orange"
  print(x)
  print(y)
  print(z)
  ```
- If you have a collection of values in a list, tuple, etc., Python allows you to extract the values into variables. This is called unpacking.
  ```python
  fruits = ["apple", "banana", "cherry"]
  x, y, z = fruits
  print(x)
  print(y)
  print(z)
  ```

### Getting the Type of a Variable

You can use `type()` to get the type of a variable.
e.g.,

```python
x = 5
print(type(x)) # This will print int
```

### Global Variables

- Variables created outside of a function are known as global variables, which means they can be accessed by everyone.
- You can make a variable inside a function globally by using the `global` keyword.
  e.g.,
  ```python
  def myfunc():
    global x
    x = "fantastic"

  myfunc()

  print("Python is " + x)
  ```

## Python Data Types

Data Types refer to the type of a value stored with the variable. There are different types of data, which include:

- `str` e.g., `x = "Hello World"`
- `int`, `float`, `complex` e.g., `x = 20`, `x = 1j`
- `list`, `tuple`, `range` e.g., `x = ["apple", "banana", "cherry"]`, `x = ("apple", "banana", "cherry")`, `x = range(6)`
- `dict` e.g., `x = {"name" : "John", "age" : 36}`
- `set`, `frozenset` e.g., `x = {"apple", "banana", "cherry"}`, `x = frozenset({"apple", "banana", "cherry"})`
- `bool` e.g., `x = True`
- `bytes`, `bytearray`, `memoryview` e.g., `x = b"Hello"`, `x = bytearray(5)`, `x = memoryview(bytes(5))`
- `NoneType` e.g., `x = None`

## isinstance

`isinstance()` is a built-in function in Python that checks whether an object is an instance of a particular class or data type, or any of a tuple of classes and types. It's a versatile tool used for type checking, ensuring that variables or objects adhere to expected types within code, which is crucial for maintaining code reliability and avoiding type-related errors in dynamically typed languages like Python.

```python
isinstance(object, classinfo)
```

- **object**: The variable or object to be checked.
- **classinfo**: A single class, data type, or a tuple of classes and types to check against the object.

**Returns**
- `True` if the object is an instance or subclass of `classinfo`, or if the object is one of the types in `classinfo` when it's a tuple.
- `False` otherwise.

## Python Strings

Strings in Python are surrounded by either single quotation marks or double quotation marks.

### Properties and Methods Related to Strings

- **Multiline Strings**: You can assign a multiline string to a variable by using three quotes.
- **Strings are Arrays**: This means you can use indexing on strings. e.g., `name = "John"` => `name[0]` would be **J**.
- `len()`: e.g.:
  ```python
  a = "Hello, World!"
  print(len(a))
  ```
- **Check String**: To check if a certain phrase or character is present in a string, we can use the keyword `in`. e.g.,
  ```python
  txt = "The best things in life are free!"
  print("free" in txt)
  ```
- **Check if NOT**: To check if a certain phrase or character is NOT present in a string, we can use the keyword `not in`.
- **Slicing Strings**: You can return a range of characters by using the slice syntax. Specify the start index and the end index, separated by a colon, to return a part of the string.
  e.g.,
  ```python
  b = "Hello, World!"
  print(b[2:5]) # result: llo
  ```
  **Note**: You can also slice from the start by just doing `b[:5]` and slice up to the end by `b[2:]`. **Negative Indexing** allows you to use negative indexes to start the slice from the end of the string, like `b[-5:-2]`.
- `str.upper()`: Upper case
- `str.lower()`: Lower case
- `str.strip()`: Removes any whitespace from the beginning or the end
- `str.replace()`: The `replace()` method replaces a string with another string:
  e.g.,
  ```python
  a = "Hello, World!"
  print(a.replace("H", "J")) # result: Jello, World!
  ```
- `str.split()`: The `split()` method returns a list where the text between the specified separator becomes the list items. e.g.,
  ```python
  a = "Hello, World!"
  print(a.split(",")) # returns ['Hello', ' World!']
  ```
- **String Concatenation**: To concatenate, or combine, two strings, you can use the `+` operator. e.g.,
  ```python
  a = "Hello"
  b = "World"
  c = a + b
  print(c) # result: HelloWorld
  ```
- **String Formatting using F-Strings**:
  e.g.,
  ```python
  age = 36
  txt = f"My name is John, I am {age}"
  print(txt)
  ```
- **Placeholders and Modifiers**: A placeholder can contain variables, operations, functions, and modifiers to format the value.
  **Examples**:
  1. Add a placeholder for the price variable:
     ```python
     price = 59
     txt = f"The price is {price} dollars"
     print(txt)
     ```
  2. A placeholder can include a modifier to format the value. A modifier is included by adding a colon `:` followed by a legal formatting type, like `.2f`, which means a fixed-point number with 2 decimals:
     ```python
     price = 59
     txt = f"The price is {price:.2f} dollars"
     print(txt)
     ```
  3. A placeholder can contain Python code, like math operations:
     ```python
     txt = f"The price is {20 * 59} dollars"
     print(txt)
     ```
- **Escape Characters**: To insert characters that are illegal in a string, use an escape character. An escape character is a backslash `\` followed by the character you want to insert. An example of an illegal character is a double quote inside a string that is surrounded by double quotes.

**Summary of All Methods**

Here's the formatted content with markdown syntax for code:

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

## Python Booleans

Booleans represent one of two values: `True` or `False`.
Almost any value is evaluated to `True` if it has some sort of content.
- Any `string` is `True`, except **empty** strings.
- Any `number` is `True`, except **0**.
- Any `list`, `tuple`, `set`, and `dictionary` are `True`, except **empty** ones.

**NOTES:**
- In fact, there are not many values that evaluate to `False`, except empty values, such as `(), [], {}, ""`, the number `0`, and the value `None`. And of course the value `False` evaluates to `False`.
- One more value, or object in this case, evaluates to `False`, and that is if you have an object that is made from a class with a `__len__` function that returns `0` or `False`

## List
`Lists` are used to store multiple items in a single variable.

`Lists` are one of **4 built-in data types** in Python used to store collections of data, the other 3 are `Tuple`, `Set`, and `Dictionary`, all with different qualities and usage.

### Properties & Methods of Lists

**len(list)**: Returns the number of elements in the list.

```python
my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Output: 5
```
**list.append(element)**: Adds an element to the end of the list.

```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
```

**list.insert(index, element)**: Inserts an element at the specified index.

```python
my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)  # Output: [1, 4, 2, 3]
```

**list.remove(element)**: Removes the first occurrence of the specified element from the list.

```python
my_list = [1, 2, 3, 2, 4]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2, 4]
```

**list.pop(index)**: Removes and returns the element at the specified index. If no index is provided, it removes and returns the last element.

```python
my_list = [1, 2, 3, 4]
popped_element = my_list.pop(1)
print(my_list)  # Output: [1, 3, 4]
print(popped_element)  # Output: 2
```

**list.index(element, start, end)**: Returns the index of the first occurrence of the specified element within the optional `start` and `end` range.

```python
my_list = [1, 2, 3, 2, 4]
index = my_list.index(2, 2)
print(index)  # Output: 3
```

**list.count(element)**: Returns the number of occurrences of the specified element in the list.

```python
my_list = [1, 2, 3, 2, 4, 2]
count = my_list.count(2)
print(count)  # Output: 3
```

**list.reverse()**: Reverses the order of elements in the list.

```python
my_list = [1, 2, 3, 4]
my_list.reverse()
print(my_list)  # Output: [4, 3, 2, 1]
```

**list.sort(key=None, reverse=False)**: Sorts the elements of the list in ascending order. The `key` and `reverse` parameters can be used for custom sorting.

```python
my_list = [4, 2, 1, 3]
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4]
```
**list.extend(iterable)**: Extends the list by appending elements from the iterable.

```python
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]
```

**list.clear()**: Removes all elements from the list.

```python
my_list = [1, 2, 3, 4]
my_list.clear()
print(my_list)  # Output: []
```

These are some of the most commonly used properties and methods of lists in Python 3. 

### List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

## Python Operators

Operators are used to perform operations on variables and values. These include
1. Arithmetic Operators
- Addition: `+` (e.g., `x + y`)
- Subtraction: `-` (e.g., `x - y`)
- Multiplication: `*` (e.g., `x * y`)
- Division: `/` (e.g., `x / y`)
- Modulus: `%` (e.g., `x % y`)
- Exponentiation: `**` (e.g., `x ** y`)
- Floor division: `//` (e.g., `x // y`)
2. Assignment Operators
- Assignment: `=` (e.g., `x = 5`)
- Addition assignment: `+=` (e.g., `x += 3` which is equivalent to `x = x + 3`)
- Subtraction assignment: `-=` (e.g., `x -= 3` which is equivalent to `x = x - 3`)
- Multiplication assignment: `*=` (e.g., `x *= 3` which is equivalent to `x = x * 3`)
- Division assignment: `/=` (e.g., `x /= 3` which is equivalent to `x = x / 3`)
- Modulus assignment: `%=` (e.g., `x %= 3` which is equivalent to `x = x % 3`)
- Floor division assignment: `//=` (e.g., `x //= 3` which is equivalent to `x = x // 3`)
- Exponentiation assignment: `**=` (e.g., `x **= 3` which is equivalent to `x = x ** 3`)
- Bitwise AND assignment: `&=` (e.g., `x &= 3` which is equivalent to `x = x & 3`)
- Bitwise OR assignment: `|=` (e.g., `x |= 3` which is equivalent to `x = x | 3`)
- Bitwise XOR assignment: `^=` (e.g., `x ^= 3` which is equivalent to `x = x ^ 3`)
- Right shift assignment: `>>=` (e.g., `x >>= 3` which is equivalent to `x = x >> 3`)
- Left shift assignment: `<<=` (e.g., `x <<= 3` which is equivalent to `x = x << 3`)
- Walrus operator: `:=` (e.g., `print(x := 3)` assigns 3 to x and prints it, then `print(x)` displays the value of x)
3. Comparison Operators
- Equal to: `==` (e.g., `x == y`)
- Not equal to: `!=` (e.g., `x != y`)
- Greater than: `>` (e.g., `x > y`)
- Less than: `<` (e.g., `x < y`)
- Greater than or equal to: `>=` (e.g., `x >= y`)
- Less than or equal to: `<=` (e.g., `x <= y`)
4. Logical Operators
- `and`: Returns True if both statements are true (e.g., `x < 5 and x < 10`)
- `or`: Returns True if one of the statements is true (e.g., `x < 5 or x < 4`)
- `not`: Reverses the result, returns False if the result is true (e.g., `not(x < 5 and x < 10)`)
5. Identity Operators
- `is`: Returns True if both variables are the same object (e.g., `x is y`)
- `is not`: Returns True if both variables are not the same object (e.g., `x is not y`)
6. Membership Operators
- `in`: Returns True if a sequence with the specified value is present in the object (e.g., `x in y`)
- `not in`: Returns True if a sequence with the specified value is not present in the object (e.g., `x not in y`)
7. Bitwise Operators
- `&`: AND - Sets each bit to 1 if both bits are 1 (e.g., `x & y`)
- `|`: OR - Sets each bit to 1 if one of two bits is 1 (e.g., `x | y`)
- `^`: XOR - Sets each bit to 1 if only one of two bits is 1 (e.g., `x ^ y`)
- `~`: NOT - Inverts all the bits (e.g., `~x`)
- `<<`: Zero fill left shift - Shift left by pushing zeros in from the right and let the leftmost bits fall off (e.g., `x << 2`)
- `>>`: Signed right shift - Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off (e.g., `x >> 2`)

**NOTE**: 
Operator precedence describes the order in which operations are performed.

The following list describes the operator precedence in Python, starting from the highest to the lowest:

1. **`()`** - Parentheses
2. **`**`** - Exponentiation
3. **`+x`, `-x`, `~x`** - Unary plus, unary minus, and bitwise NOT
4. **`*`, `/`, `//`, `%`** - Multiplication, division, floor division, and modulus
5. **`+`, `-`** - Addition and subtraction
6. **`<<`, `>>`** - Bitwise left and right shifts
7. **`&`** - Bitwise AND
8. **`^`** - Bitwise XOR
9. **`|`** - Bitwise OR
10. **`==`, `!=`, `>`, `>=`, `<`, `<=`, `is`, `is not`, `in`, `not in`** - Comparisons, identity, and membership operators
11. **`not`** - Logical NOT
12. **`and`** - Logical AND
13. **`or`** - Logical OR

This order defines how expressions containing multiple operators are evaluated in Python. Operators listed earlier have higher precedence and are evaluated before operators lower in the list.


