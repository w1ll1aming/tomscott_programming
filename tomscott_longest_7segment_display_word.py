import re

f = open("words.txt", "r")
words = f.read().splitlines()
f.close()

badLetters = "/[gkmqvwxzio]/"
lastWord = ""
TempAcceptableWords = []
longestAcceptableWords = []

for testWord in words:
    if (len(testWord) < len(lastWord)):
        continue;

    if (re.match(badLetters, testWord)): continue;

    lastWord = testWord;
    TempAcceptableWords.append(testWord);

longestWordLength = len(max(TempAcceptableWords))
for testWord in TempAcceptableWords:
    if (len(testWord) >= longestWordLength):
        longestAcceptableWords.append(testWord)

print(longestAcceptableWords)
