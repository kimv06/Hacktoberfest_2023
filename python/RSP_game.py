import random

# List of choices
choices = ["rock", "paper", "scissors"]

while True:
    # Get user choice
    user_choice = input("Choose Rock, Paper, or Scissors (or 'quit' to end): ").lower()

    if user_choice == 'quit':
        break

    if user_choice not in choices:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        continue

    # Generate computer choice
    computer_choice = random.choice(choices)

    # Determine the winner
    if user_choice == computer_choice:
        print(f"It's a tie! You both chose {user_choice}.")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print(f"You win! {user_choice} beats {computer_choice}.")
    else:
        print(f"Computer wins! {computer_choice} beats {user_choice}.")

print("Thanks for playing Rock, Paper, Scissors!")
