import random
#welcome message
def welcome_message():
    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions:")
    print("1. You are going to play against the computer.")
    print("2. Specify the number of rounds you must win to win the match.")
    print("3. In each round, choose Rock (R), Paper (P), or Scissors (S).")
    print("4. Type 'quit' at any time to end the match.")
    print("5. The game will track scores and notify you of the results.\n")


def number_of_rounds(): #number of rounds to win the game
    while True:
        try:
            value = int(input('Enter the number of rounds required to win the game: '))
            if value >= 1:
                return value
            else:
                print('Must enter a value equal to or greater than one to proceed')
        except ValueError:
            print('INVALID ENTRY, Must enter an integer to proceed')


def user_choice():
    while True:
        user = input('Enter ROCK/PAPER/SCISSORS: ').lower()
        if user in ['rock', 'paper', 'scissors']:
            return user
        elif user == 'quit':
            print("Game ended.")
            exit()
        else:
            print('Invalid entry!! Please enter ROCK, PAPER, or SCISSORS.')

def computer_choice():
    option=['rock', 'paper', 'scissors']
    return random.choice(option)

def determine_the_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def match(rounds):
    user_score = 0
    computer_score = 0

    while user_score < rounds and computer_score < rounds:
        user = user_choice()
        computer = computer_choice()
        
        print(f"You chose: {user}")
        print(f"Computer chose: {computer}")

        winner = determine_the_winner(user, computer)
        
        if winner == 'tie':
            print("It's a tie:0")
        elif winner == 'user':
            user_score += 1
            print("You WIN the round!!")
        else:
            computer_score += 1
            print("The COMPUTER wins this round!!")

        print(f"Score - You: {user_score}, Computer: {computer_score}\n")

    if user_score == rounds:
        print('CONGRATULATIONS YOU WON...HURRAYYYY!!!')
    else:
        print('YOU LOST:0 COMPUTER WINS!!!')

# Main program
welcome_message()
rounds = number_of_rounds()
match(rounds)
