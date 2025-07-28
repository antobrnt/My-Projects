import random

def play_game():
    print("Welcome to the Random Number Guessing Game!")
    print("Remember, you can type 'Give up' to quit at any time.")
    min = input ("Enter the minimum number:")
    if not min.isdigit():
        print("Please enter a valid number.")
        return
    max = input ("Enter the maximum number:")
    if not max.isdigit():
        print("Please enter a valid number.")
        return
    min = int(min)
    max = int(max)
    if  min >= max:
        print("The minimum needs to be less than the maximum")
        return
    number = random.randint(min, max)
    guesscounter = 0
    print("Guess the number between", min, "and", max)
    guesses = []
    while True:
        guesscounter +=1
        print(f"This is guess number: {guesscounter}")
        guess = input("Enter your guess: ")
        if guesscounter > 5:
            print("Games over! No more guesses. It was " + str(number))
            break
        if guess.lower() == "give up":
            print("A quitter I see! It was " +str(number))
            break
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        guess = int(guess)
        guesses.append(guess)
        if guess < min or guess > max:
            print("Your guess is out of range. Try again.")
        elif guess == number + 1:
            print("You are very close! The number is just one less than your guess.")
        elif guess == number - 1:
            print("You are very close! The number is just one more than your guess.")
        elif guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number!")
            print("It took you", guesscounter, "guesses.")
            print("Your guesses were:", guesses)
            break

while True:
    play_game()
    again = input("Do you want to play again? (yes/no): ")
    if again.lower() != 'yes':
        print("Thanks for playing!")
        break
    