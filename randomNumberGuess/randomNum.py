import random

def play_round():
    random_number = random.randint(1,100)
    attempts = 0
    max_attempts = 10
    while attempts < max_attempts:
        user_guess = int(input("Guess a number between 1 and 100:"))
        attempts += 1
        if user_guess < random_number:
            print("Hint!, Higher Number")
        elif user_guess > random_number:
            print("Hint!, Lower Number")
        else:
            print("Hurray! You guessed the number in {} attempts".format(attempts))
            return attempts
    print(f"Sorry! You have exhausted all attempts. The number was {random_number}")
    return attempts


def play_game():
    score = 0
    rounds = 0
    while True:
        rounds += 1
        attempts = play_round()
        score += max(0, 10 - attempts)
        while True:
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        if play_again == 'no':
            break
    print(f"Game Over! You played {rounds} rounds and your total score is {score}.")

if __name__ == '__main__':
    play_game()
