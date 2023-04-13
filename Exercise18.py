import random

def cows_and_bulls():
    # Generate a random 4-digit number
    secret_num = str(random.randint(1000, 9999))

    num_guesses = 0

    # Keep playing until the user guesses the number
    while True:
        # Ask the user to guess a 4-digit number
        user_num = input("Guess a 4-digit number: ")

        # Check if the user's guess is correct
        if user_num == secret_num:
            print("Congratulations, you guessed the number!")
            break

        # Count the number of cows and bulls
        cows = 0
        bulls = 0
        for i in range(4):
            if user_num[i] == secret_num[i]:
                cows += 1
            elif user_num[i] in secret_num:
                bulls += 1

        # Print the number of cows and bulls
        print(f"{cows} cows, {bulls} bulls")

        num_guesses += 1

    # Print the number of guesses the user made
    print(f"You made {num_guesses} guesses.")

if __name__ == "__main__":
    cows_and_bulls()
