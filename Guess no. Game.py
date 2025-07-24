import random
def guess_the_number():
    print("🎉 Welcome to the Guess the Number Game! 🎉")
    print("I'm thinking of a number between 1 and 100. Can you guess it? 🤔")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Get user input
            user_guess = int(input("Enter your guess (1-100): "))
            attempts += 1

            # Check if the guess is correct
            if user_guess < 1 or user_guess > 100:
                print("🚫 Please guess a number between 1 and 100! 🚫")
            elif user_guess < number_to_guess:
                print("📉 Too low! Try again. 📉")
            elif user_guess > number_to_guess:
                print("📈 Too high! Try again. 📈")
            else:
                print(f"🎊 Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts! 🎊")
                break
        except ValueError:
            print("⚠️ Invalid input! Please enter a number. ⚠️")

# Start the game
if __name__ == "__main__":
    guess_the_number()
