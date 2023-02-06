"""This program will be a little game in Hangman"""
import random
# This function will print the hanging depending on attempts
def print_hangman(attempts):
    print(" _____________")
    print(" |           |")
    listOfPrints = [[" |           O"],[" |           |"," |          \|"," |          \|/"],[" |           |"],[" |          /"," |          / \ "]]
    listofCurrentValues = [' |'] *4
    match attempts:
        case 6:
            listofCurrentValues[0] = listOfPrints[0][0]
        case 5:
            listofCurrentValues[0] = listOfPrints[0][0]
            listofCurrentValues[1] = listOfPrints[1][0]
        case 4:
            listofCurrentValues[0] = listOfPrints[0][0]
            listofCurrentValues[1] = listOfPrints[1][1]
        case 3:
            listofCurrentValues[0] = listOfPrints[0][0]
            listofCurrentValues[1] = listOfPrints[1][2]
        case 2:
            listofCurrentValues[0] = listOfPrints[0][0]
            listofCurrentValues[1] = listOfPrints[1][2]
            listofCurrentValues[2] = listOfPrints[2][0]
        case 1:
            listofCurrentValues[0] = listOfPrints[0][0]
            listofCurrentValues[1] = listOfPrints[1][2]
            listofCurrentValues[2] = listOfPrints[2][0]
            listofCurrentValues[3] = listOfPrints[3][0]
        case 0:
            listofCurrentValues[0] = listOfPrints[0][0]
            listofCurrentValues[1] = listOfPrints[1][2]
            listofCurrentValues[2] = listOfPrints[2][0]
            listofCurrentValues[3] = listOfPrints[3][1]
    for i in listofCurrentValues:
        print(i)
    print(' |')
    if attempts == 0:
        print("You lose the game!")

# From this list will be extract the random word
word_list = ["fasole", "arta", "macaroane", "reflectare", "cucusor", "fraudulos", "cuibarit", "bibliofilm", "solidar", \
    "arici", "prevazator", "perfectionist", "principial", "darnic", "fulgerator", "monoatomic", "obscur", "modernism", \
        "defibrilator", "neocolonialist", "pamfletaresc", "repercutat", "nevalorificat", "perisabil", "prestidigitator"]

attempts = 8
is_game_continue = True
word = random.choice(word_list)
latter_found = 0

#This instruction hide the word from list
choosen_word = [' _ '] * len(word)
print(*choosen_word, sep = "")
while is_game_continue:
    user_latter = input("Please, introduce your letter: ").lower()
    for i in range(0,len(choosen_word)):
        if word[i] == user_latter:
            latter_found += 1
            choosen_word[i] = ' ' + word[i] + ' '
    print(*choosen_word, sep = "")
    if len(user_latter) > 1:
        print("Please introduce just one latter!")
    if latter_found == len(word):
        print("You win!")
        is_game_continue = False
    if user_latter not in word:
        print("Try again!")
        attempts -= 1
    if attempts > 0 and attempts < 8:
        print_hangman(attempts)
    elif attempts == 0:
        print_hangman(attempts)
        is_game_continue = False

