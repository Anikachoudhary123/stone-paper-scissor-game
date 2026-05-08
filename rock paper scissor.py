
# workflow of project
# input from user(rock,paper,scissor)
# computer Choice (computer will chouse randomly not conditionally)
# result print
# A- Rock
# rock-rock = Tie 
# rock-paper = paperwin 
# paper-scissor = scissorwin
# B-paper 
# paper-paper = Tie 
# paper-rock = paperwin
# paper-scissor = scissorwin 
# C- scissor 
# scissor-scissor = Tie 
# scissor-rock = rockwin
# scissor-paper = scissorwin

import random

print("Welcome to Rock, Paper, Scissors Game")

# User input
user_choice = input("Enter Rock, Paper, or Scissor: ").lower()

# Computer random choice
choices = ["rock", "paper", "scissor"]
computer_choice = random.choice(choices)

print("Computer chose:", computer_choice)

# Result conditions
if user_choice == computer_choice:
    print("Tie")

elif user_choice == "rock":
    if computer_choice == "paper":
        print("Paper Wins")
    else:
        print("Rock Wins")

elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper Wins")
    else:
        print("Scissor Wins")

elif user_choice == "scissor":
    if computer_choice == "paper":
        print("Scissor Wins")
    else:
        print("Rock Wins")

else:
    print("Invalid Input")











