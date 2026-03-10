#ROCK PAPER SCISSORS GAME 
"""WORKFLOW OF PROJECT
1- Input from user(Rock,Paper,Scissors)
2- Computer choice(Computer will choose randomly not conditionally)
3- Result print

CASES:
A - Rock
Rock-Rock===Tie
Rock-Paper===Paper Win
Rock-Scissors===Rock Win

B- Paper
Paper-Paper===Tie
Paper-Scissors===Scissors Win
Paper-Rock===Paper Win

C- Scissors
Scissors-Scissors===Tie
Scissors-Rock===Rock Win
Scissors-Paper===Scissors Win 
"""

import random
item_list=["Rock","Paper","Scissors"]
user_choice=input("Enter your move: Rock,Paper,Scissors=")
comp_choice=random.choice(item_list)
print(f"User Choice={user_choice},Computer Choice={comp_choice}")
if(user_choice==comp_choice):
    print("both chooses the same:= MATCH TIE")
elif(user_choice=="Rock"):
    if comp_choice=="Paper":
        print("Paper covers Rock, COMPUTER WIN")
    else:
        print("Rock smashes Scissors, YOU WIN")   #YOU==USER
elif(user_choice=="Paper"):
    if comp_choice=="Scissors":
        print("Scissors cuts Paper, COMPUTER WIN")
    else:
        print("Paper covers Rock, YOU WIN")   #YOU==USER
elif(user_choice=="Scissors"):
    if comp_choice=="Rock":
        print("Rock smashes Scissors, COMPUTER WIN")
    else:
        print("Scissors cuts Paper, YOU WIN")   #YOU==USER
else:
    print("INVALID MOVE. \nEnter the correct move:")


print("-----GAME OVER----")
