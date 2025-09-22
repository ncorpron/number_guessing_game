import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

logo =  __    __  ___   __    __       __  ___________  ____  ________      ___________  __    __    _______      _____  ___   ____  ____  ___      ___  _______    _______   _______  ________   
|"  |/  \|  "| /" |  | "\     /""\("     _   ")))_ ")/"       )    ("     _   ")/" |  | "\  /"     "|    (\"   \|"  \ ("  _||_ " ||"  \    /"  ||   _  "\  /"     "| /"      \("      "\  
|'  /    \:  |(:  (__)  :)   /    \)__/  \\__/(____((:   \___/      )__/  \\__/(:  (__)  :)(: ______)    |.\\   \    ||   (  ) : | \   \  //   |(. |_)  :)(: ______)|:        |\___/   :) 
|: /'        | \/      \/   /' /\  \  \\_ /          \___  \           \\_ /    \/      \/  \/    |      |: \.   \\  |(:  |  | . ) /\\  \/.    ||:     \/  \/    |  |_____/   )  /  ___/  
 \//  /\'    | //  __  \\  //  __'  \ |.  |           __/  \\          |.  |    //  __  \\  // ___)_     |.  \    \. | \\ \__/ // |: \.        |(|  _  \\  // ___)_  //      /  //  \     
 /   /  \\   |(:  (  )  :)/   /  \\  \\:  |          /" \   :)         \:  |   (:  (  )  :)(:      "|    |    \    \ | /\\ __ //\ |.  \    /:  ||: |_)  :)(:      "||:  __   \ ('___/     
|___/    \___| \__|  |__/(___/    \___)\__|         (_______/           \__|    \__|  |__/  \_______)     \___|\____\)(__________)|___|\__/|___|(_______/  \_______)|__|  \___) (___)     
                                                                                                                                                                                          





# Function to check users' guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")
        return turns # The user guessed correctly, no turns are deducted

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100) # Corrected randint call
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer and turns > 0: # Added condition to stop if turns run out
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0 and guess != answer: # Check if turns are 0 and guess is incorrect
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")




game()
