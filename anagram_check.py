word = "test"
anagram = "sett"
looper = 0
anagram_check = True

for i in word:
    if anagram[looper] in word:
        print('Found')
    else:
        anagram_check = False
    looper += 1

print(anagram_check)
