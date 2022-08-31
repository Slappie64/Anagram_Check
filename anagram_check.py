word = "Test"
anagram = "SETT"
looper = 0

for i in word:
    if anagram[looper] in word:
        continue
    else:
        print("Nope")
    print("Yup")