import json

def findword(letters, boardLetter, location, wordLength):

# inputs:
# letters - the letters available to you (include repeats)
# boardLetter -  the letter on the board you want to make a word with (can be multiple letters)
# location - the position you want the board letter to be at in the word (eg: 1st position, second position, etc)
# wordLength - the length you want the word to be

# output
# an array of words that can be made based on the inputs
    
    # creating a dictionary to keep track of letters and their repetitions
    letterDict = {}
    for char in letters:
        if char in letterDict:
            letterDict[char] += 1
        else:
            letterDict.update({char:1})
    for char in boardLetter:
        if char in letterDict:
            letterDict[char] += 1
        else:
            letterDict.update({char:1})
         
    # Load the JSON file
    with open('words_dictionary.json', 'r') as file:
        data = json.load(file)

    # Assuming data is a list of words
    filtered_words = [word for word in data 
                      if len(word) > location-1 
                      and word[location-1].lower() == boardLetter[0]
                      and len(word) == wordLength
                      and set(word.lower()).issubset(letters + boardLetter)
                      and boardLetter in word
                      and checkValid(word, letterDict)
    ]

    return filtered_words

# a function that checks the filtered words meet repetition requirements
def checkValid(word, dictionary):
    validWord = True
    for char in dictionary:
        if word.count(char) > dictionary[char]:
            validWord = False
    return validWord

# a test print
print(findword("oiitakf", "in", 4, 5))

#test4