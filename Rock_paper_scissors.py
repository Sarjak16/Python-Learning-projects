import random

user_wins= 0
computer_wins= 0

while True:
    user_input= input("Type rock, paper, scissors or Q to quit.").lower()
    if user_input == "q":
        quit()