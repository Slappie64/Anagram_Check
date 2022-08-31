from english_words import english_words_set

word = "test"
anagram = "sett"



def check_anagram(anagram, word):

    looper = 0
    anagram_check = True

    for i in word:
        if anagram[looper] in word:
            print('Found')
        else:
            anagram_check = False
        looper += 1
        
    return anagram_check

print(anagram_check)

for i in english_words_set:
    print(i)
