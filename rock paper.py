import random

while True:
    # Get user input and validate it
    while True:
        try:
            a = int(input("Enter the number between 1 to 3 (1: Rock, 2: Paper, 3: Scissors): "))
            if a in [1, 2, 3]:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Generate computer's choice
    b = random.randint(1, 3)

    # Determine the result
    if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
        print("You lose")
    elif (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
        print("You win")
    else:
        print("Draw")
    
    print("Computer choice is:", b)

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        break