# # string
# first_name = "John"
# print(first_name, "is a string")
# # numbers
# num = 1
# print(num, "is a number")

# # multiline comments

# """This is a multiline
# comment, you can see when you print the scripts 
# it won't show
# """

# """
# String are like arrays
# Therefore, you can get each item in respective of its
# index
# """
# last_name = "Niyontwali"
# print(last_name[1])

# # getting the length of a string
# best_car = "Bentley"
# print(len(best_car))

# # in and not in
# best_car = "Bentley"
# print("b" in best_car) # python is case sensitive b == B

# print("B" in best_car)

# print("e" not in best_car) # this has to be false since e is among the letters of our best_car variable

# # Slicing Strings
# first_name = "John"
# print(first_name[1:3])

# print(first_name[1:]) # slices up to the last index
# print(first_name[:3]) # slices from the first index

# # negative indexes slicing
# first_name = "Peter"
# print(first_name[-3: -2])
# print(first_name[-5: -1])

# # upercase and lowercase
# first_name = "Amber"
# print(first_name.lower())
# print(first_name.upper())

# # removing the white space
# first_name = " Amber "
# print(first_name) # without stripping the white space
# print(first_name.strip()) # white space stripped

# # replace a string
# text = "This boy is beautiful"
# modified_text = text.replace("boy", "girl")
# print(modified_text)

# # splitting
# text = "sweet love"
# print(text.split(" ")) # splitting by space separator

# # concatenation
# first_name = "John " # note the space after John
# last_name = "Niyontwali"
# print(first_name + last_name)

# # format method
# age = 28
# year = 1994
# text = "I was born in {}, therefore I am turning {} years soon"
# print(text.format(year, age)) # order matters

# # format method using the short hard
# age = 28
# year = 1994
# text = f"I was born in {year}, therefore I am turning {age} years soon"
# print(text)

# # Escape character
# text = "God said, \"Blessed are those who seek the Kingdom of God\""
# print(text)

# # reading keyboard input
# question = "What is your name: "
# print(question)
# answer = input()
# print("You wrote your name is: ", answer)

# # python lists
# cars = ["Benz", "Bentley", "Volvo"]
# print(cars)  # this is a list of cars
# even_numbers = [0, 2, 4, 6, 8]
# print(even_numbers)

# # length of a list
# even_numbers = [0, 2, 4, 6, 8]
# print(len(even_numbers))

# # type list
# even_numbers = [0, 2, 4, 6, 8]
# print(type(even_numbers))

# # accessing list items
# even_numbers = [0, 2, 4, 6, 8]
# print(even_numbers[3]) # The output has to be 6

# # print a range of list items
# even_numbers = [0, 2, 4, 6, 8]
# print(even_numbers[1:3]) # notice that the 3rd item is not included

# # append and insert
# fruits_list = ["Banana", "Pineaple"]
# fruits_list.append("Apple")
# print(fruits_list)

# fruits = ["Banana", "Pineaple"]
# fruits.insert(1, "Apple")
# print(fruits)

# # extend list
# suv1 = ["Bently", "BMW"]
# suv2 = ["Benz", "VW", "Lamborgin"]
# suv2.extend(suv1)
# print(suv2)

# # removing a list item
# fruits = ["Mango", "Banana", "Apple"]
# fruits.remove("Banana")
# print(fruits)

# # pop and del
# fruits = ["apple", "banana", "cherry"]
# fruits.pop(2)
# print(fruits)

# stacks = ["JavaScript", "Python", "Java"]
# del stacks[2]
# print(stacks)

# reverse
# stacks = ["JavaScript", "Python", "Java"]
# stacks.reverse()
# print(stacks)

# # sorting
# cars = ['Ford', 'BMW', 'Volvo']
# cars.sort()
# print(cars)

# # count
# cars = ["Ford", "BMW", "Ford"]
# print(cars.count("Ford"))

# # List comprehension
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist)

# # short hand for the above
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# new_list = [x for x in fruits if "a" in x]
# print(newlist)

# # looping
# i = 1
# while i < 6:
#   print(i)
#   i += 1

# # for loop
# last_name = "Niyontwali"
# for x in last_name: 
#   print(x)
# the range function
for x in range(6):
  print(x)