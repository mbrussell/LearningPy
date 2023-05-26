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
