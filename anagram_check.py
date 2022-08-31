from english_words import english_words_set

test_word = 'says'
anagram = "etst"
check = True

potential_words = []


for i in english_words_set:
    if len(anagram) == len(i):
        for a in i:
            if a not in anagram:
                check = False
        print("{} : {}".format(i, check))

"""
for a in test_word:
    if a not in anagram:
        check = False
print("{} : {}".format(test_word, check))
"""