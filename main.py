import random
import os

p_lst = []

for i in range(2):
    print(f"Player {i+1} is playing...\n")
    com_no = random.randint(1, 100)
    attempt = 0

    your_no = int(input("Choose a number(Between 1-100) : "))
    while(True):
        if(com_no==your_no):
            attempt+=1
            print("You choose correct number.")
            print(f"Total attemps : {attempt}.\n")
            p_lst.append(attempt)
            break
        elif(your_no>com_no):
            print("Lower number, Please!")
            attempt+=1
        else:
            print("Higher number, Please!")
            attempt+=1

        your_no = int(input("\nChoose another number : "))
        os.system('cls')

print(f"Player 1 attempts : {p_lst[0]}\nPlayer 2 attempts : {p_lst[1]}")
if(p_lst[0]==p_lst[1]):
    print("It's a Tie! Play again...")
elif(p_lst[0]<p_lst[1]):
    print("Player 1 Wins.")
else:
    print("Player 2 Wins.")

input("\nPress Enter to END!")