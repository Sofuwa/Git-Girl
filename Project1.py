QUESTION
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year 
that they will turn 100 years old. Ask the user for a number. Depending on whether the number is even or odd, print out an 
appropriate message to the user.  How does an even / odd number react differently when divided by 2?

ANSWERS
name = input("What is your name?: ")
age = input("What is your age?: ")
DOB = 2019 - int(age)
year = DOB + 100
print ("You are" + name + " and you will be 100 years old in " + str(age))

number = input("Enter a number: ")
if int(number) % 2 == 0:
  print ("The number you selected is an even number")
else:
  print ("The number you selected is odd")
  
print ("Exiting...")
