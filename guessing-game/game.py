"""A number-guessing game."""

#5.9 Lab: Guess the Number (SFSU-FALL 2021-by Jamie Mancini-10/07/21)

#imports module to generate random integers
import random
#imports module to set delay
import time

#Greet the user
print("Hi friend! I hope that you like guessing games!")

#Build a game in which a user is asked to guess a secret number. 
#The computer first generates a random number between 1 to 100. 
print("Let's play a game!")
time.sleep(2)
print("I'll pick a number between 1 and 100.")
time.sleep(2)
print("You're gonna guess my number.")
time.sleep(1)

#randomly generate a number for the program
computer_number = random.randint(1, 100)
#print(computer_number)

#the user is prompted to guess what number was chosen by the computer
user_number = input("Guess the number:")

#converts the user's number into an integer
user_number=int(user_number)

#Creates a while loop that conitnues 
#UNTIL the user guesses the correct number 
while user_number != computer_number:
  
  #if the user's number is larger than the random number
  if user_number > computer_number and user_number < 101:
    print(f"Sorry, {user_number} is too high :(")
    print()
    user_number = int(input("Guess another number:"))
  
  #if the user's number is smaller than the random number
  elif user_number < computer_number and user_number > 0:
    print(f"Sorry, {user_number} is too low :(")
    print()
    user_number = int(input("Guess another number:"))
  
  #if the user types a number not in the range between 1 and 100
  else:
    print(f"{user_number} is not between 1 and 100 :(")
    user_number = int(input("Guess a number:"))
  
#when the user finally guess the correct answer
print(f"{user_number} is CORRECT!")
print("You've won...")
time.sleep(2)
print("N")
time.sleep(1)
print("A")
time.sleep(1)
print("D")
time.sleep(1)
print("A")
time.sleep(1)
print(":(")
