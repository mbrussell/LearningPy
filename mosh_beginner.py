# From Mosh video: Python tutorial - Python full course for beginners
# https://youtu.be/_uQrJ0TkZlc


# print("Matt Russell")
# print("o----")
# print(" ||||")
# print("*" * 10)
# print("<3" * 10)

# price = 10
# rating = 4.9
# name = "Matt"
# is_published = True
# print(price)


# name = "John Smith"
# age = 20
# is_patient = True

# name = input("What is your name? ")
# color = input("What is your favorite color? ")
# print(name, "likes ", color)

# birth_year = input("Birth year: ")
# print(type(birth_year))
# age = 2023 - int(birth_year)
# print(type(age))
# # int()
# # float()
# # bool()
# print(age)

# weight = input("What is your weight? ")
# print(float(weight)*0.4526)

# print("foo")
# # input("My name:" )
# print(45, 47)

# # Strings
# course = 'Python course for "beginners"'
# course = ''' Hi John,
# Here is our email. 
# Thank you, 
# Support Team'''
# course = 'Python  for beginners'
# print(course)
# print(course[0])
# print(course[-2])
# print(course[1:])
# print(course[:5])
# print(course[:])

# name = "Jennifer"
# print(name[1:-1])

# # Formatted strings
# first = "Matt"
# last = "Russell"
# message = first + " [" + last + "] is a coder."
# msg = f"{first} [{last}] is a coder."
# print(msg)

# course = "Python for beginners"
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find("for"))
# print(course.replace("beginners", "absolute beginners"))
# print("Python" in course)

# # Arithmetic operators
# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(10 ** 3)
# x = 10
# x -= 3
# print(x)

# x = (10 + 3) * 2 ** 2
# print(x)

# x = (2 + 3) * 10 - 3
# print(x)

# Math
# x = 2.9
# print(round(x))
# print(abs(-2.9))


# import math

# print(math.ceil(2.9))

# print(math.floor(2.9))

# If statements
# is_hot = False
# is_cold = False

# if is_hot: 
#     print("It's a hot day.")
#     print("Drink water!")
# elif is_cold:
#     print("It's a cold day.")
#     print("Wear warm clothes!")
# else:
#     print("It's a lovely day!")

# print("Enjoy your day!")

# has_good_credit = False
# price = 1000000


# if has_good_credit: 
#     down_payment = 0.10 * price
# else:
#     down_payment = 0.20 * price
# print(f"Down payment: ${down_payment}")    

# Logical operators

# has_high_income = True
# has_good_credit = True
# has_criminal_record = True

# if has_high_income or has_good_credit:
#     print("Eligible for loan")

# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan")

# Comparison operators
# temp = 30

# if temp != 30:
#     print("It's a hot day.")
# else: 
#     print("It's not a hot day.") 

# name = "Matthew"

# if len(name) <3:
#     print("Name must be at least three characters.")
# elif len(name) > 50:
#     print("Name can be a max of 50 characters.")
# else:
#     print("Name looks good!")

## Project: weight converter

# weight = int(input("Weight: "))
# unit = input("(L)bs or (K)g: ")
# if unit.upper() == "L":
#     converted_weight = weight * 0.45
#     print(f"You are {converted_weight} kilos.")
# else:
#     converted_weight = round(weight / 0.45, 3)
#     print(f"You are {converted_weight} pounds.")

# While loops (execute a block of code multiple times)

# i = 1

# while i <= 5:
#     print("*" * i)
#     i = i + 1
# print("DONE")
 
# # Guessing game
# secret_number = 9
# guess_count = 0
# guess_limit = 3

# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("You won!")
#         break
# else: 
#     print("Sorry, you failed.")

## Car game

# car_command = ""
# started = False
# while True:
#     car_command = input("> ").lower()
#     if car_command == "start":
#         if started:
#             print{"Car is already started."}
#         else:
#             started = True    
#             print("You started the car. Vrooom!")
#     elif car_command == "stop":
#         if not started:
#             print("Car is already stopped.")
#         else:
#             started = False    
#             print("You stopped the car. Schreeech!")
#     elif car_command == "help":
#         print("""
# start - to start
# stop - to stop
# quit - to quit
#         """)
#     elif car_command == "quit":
#          break    
#     else:
#         print("Sorry, I don't get that")    

# For loops
# Squared brackets make list
# for item in ["Mosh", "John", "Sarah"]:
#     print(item)

# for item in range(5, 10, 2):
#     print(item) 
# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total = total + price

# print(f"Total: {total}")

## Nested loops
# for x in range(4):
#     for y in range(3):
#           print(f"({x}. {y})")


# ## Challenge
# numbers = [5, 2, 5, 2, 2]
# numbers_L = [2, 2, 2, 2, 5]
# # for x_count in numbers:
# #     print("x" * x_count)

# for x_count in numbers_L:
#     output = ""
#     for count in range(x_count):
#         output = "x" + output
#     print (output)

# # Lists
# names = ["John", "Mary", "Matt"]
# names[2] = "Matthew"
# print(names)
# print(names[1:2])
# print(names[:])

# nums = [12, 11, 15, 9]
# max = nums[0]
# for num in nums:
#     if num > max:
#         max = num
# print(max)
# print(max(nums))

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix[0][1])

# for row in matrix:
#     for item in row:
#         print(item)

# List methods
# numbers = [5, 2, 2, 7, 4]
# numbers.sort()
# numbers.reverse()
# numbers2 = numbers.copy()
# numbers.append(10)
# print(numbers)
# print(numbers2)

# numbers = [2, 2, 4, 6, 3, 4, 6, 1]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)        

# Tuples - cannot be altered like lists can

# numbers = (1, 2, 3)
# numbers[0] = 10
# print(numbers[0])

# Unpacking

# coords = (1, 2, 3)
# #coords[0] * coords[1] * coords[2]
# #x = coords[0]
# #y = coords[1]
# #z = coords[2]

# x, y, z = coords
# print(y)

# Dictionaries

# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True
# }

# print(customer.get("name"))

# print(customer.get("birthdate", "Oct 6, 1983"))
# customer["name"] = "Jack Smith"
# print(customer["name"])

# phone = input("Phone:")

# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }

# output = ""
# for ch in phone:
#     output += digits_mapping.get(ch, "!", " ")

# print(output)

# Emoji converter
# message = input(">")
# words = message.split(" ")
# emojis = {
#     ":)": "happy face",
#     ":(": "sad face"
# }
# ouput = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)    

# # Functions, Parameters, Keyword arguments
# def greet_user(first_name, last_name):
#     print(f"Hi {first_name} {last_name}!")
#     print("Welcome aboard!")


# print("Start")
# greet_user(last_name = "Smith", first_name = "John")
# calc_cost(total = 50, shipping = 5, discount = 0.1)
# print("Finish")   
 
# Return statement
# def square(number): 
#     return number * number


# print(square(3))

# # Exercise
#  message = input(">")
#  words = message.split(" ")
#  emojis = {
#      ":)": "happy face",
#      ":(": "sad face"
#  }
#  ouput = ""
#  for word in words:
#      output += emojis.get(word, word) + " "
#  print(output)    

# def emoji_converter(message):
#     words = message.split(" ")
#     emojis = {
#         ":)": "happy face",
#         ":(": "sad face"
#     }
#     ouput = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output        


# message = input(">") 
# print(emoji_converter(message))       

# # Exceptions
# try: 
#     age = int(input("age: "))
#     income = 20000
#     risk = income/age
#     print(age)
# except ZeroDivisionError:
#     print("Age cannot be zero.")
# except ValueError:
#     print("Invalid value")    

# Comments

# This ignores text
# Use comments to explain whys and hows, not whats.
# print("Mets are a good baseball team.")

# Classes
# Use Pascal naming convention
# class Point:
#      def __init__(self, x, y)
#      def move(self):
#          print("move")

#      def draw(self):
#          print("draw")


# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()

# point2 = Point()
# point2.x = 1
# print(point2.x)

# Constructors

# class Point:
#      def __init__(self, x, y):
#          self.x = x
#          self.y = y
#      def move(self):
#          print("move")

#      def draw(self):
#          print("draw")


# point = Point(10, 20)
# point.x = 11
# print(point.x)

# Exercise
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def talk(self):
#         print(f"Hi! I'm {self.name}")

# bob = Person("Bob Smith") 

# john = Person("John Smith")
# bob.talk()       
# bob = Person("Bob Smith") 

# Inheritance
# DRY: Don't repeat yourself

# class Mammal:
#         def walk(self):
#         print("walk")


# class Dog(Mammal):
#         def bark(self):
#         print("bark")


# class Cat(Mammal):
#        pass

# dog1 = Dog()
# dog1.bark

# Modules
# Modules are like sourcing a file in R
# # Imports all functions of a module
# import converters

# # imports a select function from a module
# from converters import kg_to_lbs

# print(kg_to_lbs(70))
# print(converters.kg_to_lbs(70))

# Exercise
# import utils

# numbers = [120, 37, 4]
# maximum = utils.find_max(numbers)
# print(maximum)
# print(max(numbers)) 

# Packages