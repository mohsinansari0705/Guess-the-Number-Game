# Guess the Number Game

This repository contains a simple "Guess the Number" game where the player tries to guess a number chosen by the computer within a specified range.

## Game Rules

- The computer chooses a random number between 1 and 100.
- The player attempts to guess the number within the same range.

## Approach

1. The computer chooses a number between 1 and 100.
2. The player chooses a random number in the range of 1 to 100.
3. Initialize a variable `attempt` to 0 to keep track of the number of attempts.
4. The game logic is as follows:
   - If the player's number (`your_no`) is less than the computer's number (`computer_no`):
     - Print "Greater number please" and increment `attempt` by 1.
   - If the player's number (`your_no`) is greater than the computer's number (`computer_no`):
     - Print "Smaller number please" and increment `attempt` by 1.
   - If the player's number (`your_no`) is equal to the computer's number (`computer_no`):
     - Increment `attempt` by 1 and display the number of attempts to the player.

## Example Code

```python
import random

# Computer chooses a number between 1 and 100
computer_no = random.randint(1, 100)

# Initialize attempt counter
attempt = 0

while True:
    # Player chooses a number
    your_no = int(input("Guess a number between 1 and 100: "))
    
    # Increment attempt counter
    attempt += 1
    
    # Game logic
    if your_no < computer_no:
        print("Greater number please")
    elif your_no > computer_no:
        print("Smaller number please")
    else:
        print(f"Congratulations! You've guessed the number in {attempt} attempts.")
        break