import random

def play_rock_paper_scissors():
    """
    Plays a game of Rock-Paper-Scissors against the computer.
    """
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors!")

    while True:
        # User Input
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        while user_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        # Computer Selection
        computer_choice = random.choice(choices)
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        # Game Logic and Display Result
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1

        # Score Tracking
        print(f"Score: You {user_score} - Computer {computer_score}")

        # Play Again
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__== "__main__":
    play_rock_paper_scissors()
