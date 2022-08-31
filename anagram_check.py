from english_words import english_words_set

anagram = "sueho"
potential_words = []

print(potential_words)

def check_anagram(word, anagram):
    check = True

    for a in word:
        if a not in anagram:
            check = False
    #print("{} : {}".format(word, check))
    if check == True:        
        potential_words.append(word)

for word in english_words_set:
    if len(anagram) == len(word):
        check_anagram(word, anagram)

print(potential_words)