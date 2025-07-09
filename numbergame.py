import random
playing = True
number = str(random.randint(1, 50))
print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")
print("DONT RAGEQUIT!(you will problably never gueess it anyway)")
while playing:
    guess = input("Enter your guess: ")
    if guess == number:
        print("Congratulations! You guessed the number!")
        playing = False
    else:
        print("Wrong guess. Try again.")