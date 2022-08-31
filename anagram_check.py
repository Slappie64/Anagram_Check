import sys
from english_words import english_words_set

# Take an argument from the command line.
# Remove white space and make lowercase.
anagram = sys.argv[1].lower().replace(' ', '')
# Create an empty list for potential solved words.
potential_words = []

# Function
# Takes a word and checks each letter against the anagram.
# If the letter does not exist in both, move on.
# If it does, append the Potential_Words list with the word.
def check_anagram(word, anagram):
    check = True

    for a in word:
        if a not in anagram:
            check = False
    #print("{} : {}".format(word, check))
    if check == True:        
        potential_words.append(word)


# Loop
# For each word in the english_words_list.
# Check whether the word is the same length as the anagram.
# Then run a letter by letter check against the anagram.
for word in english_words_set:
    if len(anagram) == len(word):
        check_anagram(word, anagram)

# Print out the list of potential words
print(potential_words)