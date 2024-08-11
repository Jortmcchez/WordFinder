import json

def checkValid(word, dictionary):
    validWord = True
    for char in dictionary:
        if word.count(char) > dictionary[char]:
            validWord = False
    return validWord


def findword(letters, boardLetter, spaceLeft, spaceRight):
    
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

    with open('words_dictionary.json', 'r') as file:
        data = json.load(file)

    filtered_words = [word for word in data 
                if boardLetter in word
                and set(word.lower()).issubset(letters + boardLetter)
                and checkValid(word, letterDict)
                and spaceLeft - word.rfind(boardLetter) >= 0
                and spaceRight - (len(word) - (word.rfind(boardLetter) + 1)) >= 0
    ]
    
    return filtered_words            


#print(findword("viclohe", "k", 2, 2))

def checkRight(row, col):
    right_limit = 0
    col = col + 1
    if col == 14:
        return 0
    while col <= 14:
        if arr[row][col] != " ":
            break
        else:
            col = col + 1
            right_limit = right_limit + 1
    return right_limit
def checkLeft(row, col):
    left_limit = 0
    col = col - 1
    if col == 0:
        return 0
    while col >= 0:
        if arr[row][col] != " ":
            break
        else:
            col = col + 1
            left_limit = left_limit + 1
    return left_limit
def checkAbove(row, col):
    upper_limit = 0
    row = row - 1
    if row == 0:
        return 0
    while row > 0:
        if arr[row][col] != " ":
            break
        else:
            row = row - 1
            upper_limit = upper_limit + 1
    return upper_limit
def checkBelow(row, col):
    lower_limit = 0
    row = row + 1
    if row == 14:
        return 0
    while row <= 14:
        if arr[row][col] != " ":
            break
        else:
            row = row + 1
            lower_limit = lower_limit + 1
    return lower_limit

rows, cols = (15, 15)
arr = [[" " for i in range(cols)] for j in range(rows)]
arr[6][5] = "t"
arr[7][5] = "a"
arr[8][5] = "i"
arr[9][5] = "k"
arr[10][5] = "o"
arr[7][3] = "s"
arr[7][4] = "p"
arr[7][5] = "a"
arr[7][6] = "y"
arr[7][7] = "e"
arr[7][8] = "d"
arr[0][3] = "f"
arr[0][4] = "r"
arr[0][5] = "a"
arr[0][6] = "t"
arr[0][8] = "m"
arr[0][9] = "a"
arr[0][10] = "d"
arr[0][11] = "l"
arr[0][12] = "y"
arr[1][5] = "r"
arr[1][6] = "e"
arr[1][7] = "v"
arr[1][8] = "e"
arr[1][9] = "t"
arr[2][7] = "e"
arr[3][7] = "h"
arr[4][7] = "i"
arr[5][7] = "c"
arr[6][7] = "l"
letters = "oaanhws"

for row in arr:
    print(row)

row_counter = -1
col_counter = -1
possible_words = []
for row in arr:
    row_counter = row_counter + 1
    col_counter = -1
    for item in row:
        col_counter = col_counter + 1
        if item != " ":
            right = checkRight(row_counter, col_counter)
            left = checkLeft(row_counter, col_counter)
            up = checkAbove(row_counter, col_counter)
            below = checkBelow(row_counter, col_counter)

            #print(checkBelow(row_counter, col_counter))

            #print(right)
            #print(letters)
            if right > 0 or left > 0:
                print(item)
                print("[" + str(col_counter) + "][" + str(row_counter) + "]")
                print(findword(letters, item, left, right))
                print(" ")
            if up > 0 or below > 0:
                print(item)
                print("[" + str(col_counter) + "][" + str(row_counter) + "]")
                print(findword(letters, item, up, below))
                print(" ") 




            

