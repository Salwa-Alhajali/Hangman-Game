# Initialize variables
misses = 0  
count = 0
wrong_attempts = -1

# Get the word to guess
word = input("Enter the word: ").strip()

# Create a list of underscores representing the word
list_word = ["_" for _ in word]  
print(" ".join(list_word))  

# Loop until the word is guessed or attempts are exhausted
while "_" in list_word:  
    # Get the guessed letter
    guess = input("Guess a letter: ").strip()
    
    # Check if the guessed letter is in the word
    if guess in word:   
        for idx, ch in enumerate(word):  
            if ch == guess:
                list_word[idx] = ch  # Replace the underscore with the correct letter
        print(" ".join(list_word))   
    else:
        # Increment the number of wrong attempts
        misses += 1
        
        # Draw the hangman step by step
        if misses == 1:
            print("___________")
        elif misses == 2:
            print("___________\n        |")
        elif misses == 3:
            print("___________\n        |\n        O")
        elif misses == 4:
            print("___________\n        |\n        O\n       /|\\")
        elif misses == 5:
            print("___________\n        |\n        O\n       /|\\\n       / \\")
            print("Hard luck!")
            break

# Check if the word was guessed
if "_" not in list_word:
    print("Congratulations! You've guessed the word completely.")
