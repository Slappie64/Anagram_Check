from english_words import english_words_set

def check_anagram(anagram, word):
    looper = 0
    anagram_check = True

    if len(anagram) == len(word):
        for i in word:
            if i not in word:
                anagram_check = False
            looper += 1
            print(i)
        print("{} is {}".format(word, anagram_check))
    else:
        exit
    #return anagram_check

anagram = 'sett'

for i in english_words_set:
    check_anagram(anagram, i)
