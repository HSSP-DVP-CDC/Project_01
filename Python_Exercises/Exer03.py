#Tuples
#Tuples are immuntable
# coordinates =(4, 5)
# print(coordinates[0])

#How to handle errors that may happen in the code
#Try/Except

#This code works fine, as long as the user inputs a valid integer, but an invalid input will break the code
#number = int(input("Enter a number: "))
#print(number)

#Using a 'try/except' clause, the user will have an input error if they enter an invalid answer
# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except:
#     print("Invalid input")

#You can specify your errors
try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by Zero")
except ValueError:
    print("Invalid input")