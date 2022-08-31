from english_words import english_words_set

def check_anagram(anagram, word):

    looper = 0
    anagram_check = True

    for i in word:
        if anagram[looper] in word:
            continue
        else:
            anagram_check = False
        looper += 1
    return anagram_check

word_1 = "test"
anagram_1 = "sett"

word_2 = "random"
anagram_2 = "settah"


print(check_anagram(anagram_1, word_1))
print(check_anagram(anagram_2, word_2))
