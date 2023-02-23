import csv
import random

# Define the input file path
input_file = 'AcronymList.csv'

# Open the input file and read its contents
with open(input_file, 'r') as f:
    reader = csv.reader(f)
    # Skip the header row
    next(reader)
    # Create a list of acronym-definition pairs, stripping any newline characters from the end of the definition
    acronyms = [(row[0], row[1].rstrip('\n')) for row in reader]

# Define a function to prompt the user to guess the definition of an acronym
def guess_definition(acronym, definition):
    print('What does the acronym {} stand for?'.format(acronym))
    guess = input().strip().lower()
    if guess == definition.lower():
        print('Congratulations! You are correct.')
        return True
    else:
        print('Sorry, that is incorrect. The correct answer is "{}".'.format(definition))
        return False


# Play the flashcard game until the user chooses to quit
play_again = True
while play_again:
    # Randomly select an acronym and prompt the user to guess its definition
    random_acronym, random_definition = random.choice(acronyms)
    guess_definition(random_acronym, random_definition)
    
    # Prompt the user to play again or quit
    play_again_input = input('Play again? (y/n) ').strip().lower()
    play_again = (play_again_input == 'y')