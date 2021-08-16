import re

# Read words.txt (words.txt would be a dictionary).
f = open("words.txt", "r")

# Read all the lines from words.txt then splits a the read contents into a list.
words = f.read().splitlines()

# Close the file reader.
f.close()

# Bad letters that cannot be shown on the 8 segment display.
badLetters = "/[gkmqvwxzio]/"

# The last word we looped through.
lastWord = ""

# Temporary list of the longest acceptable words, that will be filtered later for tinier words that came first in the dictionary.
TempAcceptableWords = []

# List of the longest acceptable words.
longestAcceptableWords = []

# Loop through the words in the list of words from the dictionary.
for testWord in words:
    if (len(testWord) < len(lastWord)):
        continue;

    # if the words contains one of the letters in badLetters, dont use that word.
    if (re.match(badLetters, testWord)): continue;

    # This word is longer than the last one so keep it as the longest word we have found so far.
    lastWord = testWord;
    
    # Longest word we have found so far so add it to the temporary list of words.
    TempAcceptableWords.append(testWord);

# Find the longest word in temporary list of longest words.
longestWordLength = len(max(TempAcceptableWords))

# Loop through the words in the list temporary longest words.
for testWord in TempAcceptableWords:
    # If it is as long as the longest word then add it to the list of longest words.
    if (len(testWord) >= longestWordLength):
        longestAcceptableWords.append(testWord)

# Show the list of longest acceptable words.
print(longestAcceptableWords)
