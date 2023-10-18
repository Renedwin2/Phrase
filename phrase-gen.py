import random

# Open the file called 'list' and read the words into a list
with open('english.txt', 'r') as file:
    words = file.read().split()

# Check if there are at least 12 words in the file
if len(words) >= 12:
    # Randomly select 12 words from the list
    selected_words = random.sample(words, 12)
    
    # Join the selected words into a string separated by space
    result = ' '.join(selected_words)
    
    # Print the result
    print(result)
else:
    print("Not enough words in the file. There should be at least 12 words.")
