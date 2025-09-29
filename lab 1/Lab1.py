# - write a program that prints hello world

#print("Hello world")

# 	- application to take a number in binary form from the user, and print it as a decimal

# binary = input("Enter a binary number: ")
# if(set(binary).issubset({"0","1"})):
#     print(int(binary, 2))
# else:
#     print("is not binary")

# 	- write a function that takes a number as an argument and if the number
# 		divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
# 		divisible by both return "FizzBuzz"

# def fizz_buzz(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return "FizzBuzz"
#     elif num % 3 == 0:
#         return "Fizz"
#     elif num % 5 == 0:
#         return "buzz"
#     else:
#         return num

# 	- Ask the user to enter the radius of a circle print its calculated area and circumference

# x= input("Enter R:")
# print("cir : " + str(2*3.14*float(x)))
# print("area: " + str(3.14*float(x)*float(x)))

# 	- Ask the user for his name then confirm that he has entered his name (not an empty string/integers). then proceed to ask him for his email and print all this data
# name = input("Enter name:")
# if name.strip() == "" or name.strip().isdigit():
#     print("input invalid")
# else:
#     email = input("Enter mail:")
#     print(name)
#     print(email)

# 	- Write a program that prints the number of times the substring 'iti' occurs in a string
# text = input("Enter string:")
# print(text.lower().split().count('iti')) 
