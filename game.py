import functions
import random
from itertools import repeat

#loop counters
b = 1
k = 1

player1turn = 1
player2turn = 0

# game title

def title():
    txt = " Battle of the Sixes (B.O.T.S) "
    print(txt.center(80, "="))

# function that generates the random dice

def randomdice(n):
    n[0] = random.randrange(1, 4)
    n[1] = random.randrange(1, 4)
    n[2] = random.randrange(1, 4)
    n[3] = random.randrange(1, 4)
    n[4] = random.randrange(1, 4)
    return n

# custom dice for re-rolling

custom_dice = [0, 0, 0, 0, 0]


custom_dice_activated = False

def nextturn():
    global player1turn, player2turn
    if player1turn == 1:
        player2turn = 1
        player1turn = 0
    elif player2turn == 1:
        player1turn = 1
        player2turn = 0


def playersscore():
    print("Player 1: " + str(sum(permanent_scores[0])))
    print("Player 2: " + str(sum(permanent_scores[1])) + "\n")

def winner():
    if sum(permanent_scores[0]) > sum(permanent_scores[1]):
        print("Player 1 wins")
    elif sum(permanent_scores[0]) < sum(permanent_scores[1]):
        print("Player 2 wins")
    else:
        print("It's a tie")

def playerturn():
    if player1turn == 1 and player2turn == 0:
        print("Player 1")
    elif player2turn == 1 and player1turn == 0:
        print("Player 2")


# the function that calculates 1s and 2s and 3s and 4s

def like_terms(dice):
    like_terms_list = [0] * 4
    for i in dice:
        if i == 1:
            like_terms_list[0] += i
        elif i == 2:
            like_terms_list[1] += i
        elif i == 3:
            like_terms_list[2] += i
        elif i == 4:
            like_terms_list[3] += i
    return like_terms_list


def trio(dice):
    if dice.count(1) >= 3 or dice.count(2) >= 3 or dice.count(3) >= 3 or dice.count(4) >= 3 or dice.count(5) >= 3:
        return sum(dice)
    else:
        return 0


def quartet(dice):
    if dice.count(1) >= 4 or dice.count(2) >= 4 or dice.count(3) >= 4 or dice.count(4) >= 4 or dice.count(5) >= 4:
        return sum(dice)
    else:
        return 0


def doremi(dice):
    doremi_list = [0] * 5
    for i in dice:
        if i == 1:
            doremi_list[0] += i
        elif i == 2:
            doremi_list[1] += i
        elif i == 3:
            doremi_list[2] += i
        elif i == 4:
            doremi_list[3] += i
        elif i == 5:
            doremi_list[4] += i

        if doremi_list[0] >= 1 and doremi_list[1] >= 1 and doremi_list[2] >= 1 and doremi_list[3] >= 1:
            return 20
        else:
            return 0


def band(dice):
    condition1 = False
    condition2 = False
    if dice.count(1) >= 3 or dice.count(2) >= 3 or dice.count(3) >= 3 or dice.count(4) >= 3 or dice.count(5) >= 3:
        condition1 = True
    if dice.count(1) == 2 or dice.count(2) == 2 or dice.count(3) == 2 or dice.count(4) == 2 or dice.count(5) == 2:
        condition2 = True
    if condition1 == True and condition2 == True:
        return 30
    else:
        return 0


def orchestra(dice):
    f_number = dice[0]
    flag = True
    # Comparing each element with first item
    for item in dice:
        if f_number != item:
            flag = False
            break
    if (flag == True):
        return 40
    else:
        return 0


def currentplayerlist():
    if player1turn == 1:
        return 0
    elif player2turn == 1:
        return 1

# the function that calculates the score for each player in each category

def add_score(category):
    global permanent_scores, scores
    if category.lower() == "1s":
        permanent_scores[currentplayerlist()][0] = scores[currentplayerlist()][0]
    elif category.lower() == "2s":
        permanent_scores[currentplayerlist()][1] = scores[currentplayerlist()][1]
    elif category.lower() == "3s":
        permanent_scores[currentplayerlist()][2] = scores[currentplayerlist()][2]
    elif category.lower() == "4s":
        permanent_scores[currentplayerlist()][3] = scores[currentplayerlist()][3]
    elif category.lower() == "trio":
        permanent_scores[currentplayerlist()][4] = scores[currentplayerlist()][4]
    elif category.lower() == "quartet":
        permanent_scores[currentplayerlist()][5] = scores[currentplayerlist()][5]
    elif category.lower() == "doremi":
        permanent_scores[currentplayerlist()][6] = scores[currentplayerlist()][6]
    elif category.lower() == "band":
        permanent_scores[currentplayerlist()][7] = scores[currentplayerlist()][7]
    elif category.lower() == "orchestra":
        permanent_scores[currentplayerlist()][8] = scores[currentplayerlist()][8]

# check if all of the item items are integers

def checkList(list_input):
    try:
        list_input = [int(i) for i in list_input]
        return all(isinstance(item, int) for item in list_input)
    except:
        return False


# check if the cheat list items have the same number

def check_cheat_numbers(list_num):
    try:
        if checkList(list_num) == True:
            list_input = [int(i) for i in list_num]
            list_input.sort()
            if list_input[-1] <= 4:
                return True
        else:
            return False
    except:
        return False



diceturn = 1

names = ["Player 1", "Player 2"]
categories = ["1S", "2S", "3S", "4S", "Trio", "Quartet", "Band", "Doremi", "Orchestra"]
categories_lowercase = ["1s", "2s", "3s", "4s", "trio", "quartet", "band", "doremi", "orchestra"]

players_categories = {
    0: {"1s": 0, "2s": 0, "3s": 0, "4s": 0, "trio": 0, "quartet": 0, "band": 0, "doremi": 0, "orchestra": 0},
    1: {"1s": 0, "2s": 0, "3s": 0, "4s": 0, "trio": 0, "quartet": 0, "band": 0, "doremi": 0, "orchestra": 0}}

cheat_activated = {0: False, 1: False}

roundnumber = 1

# 1s,2s,3s,4s,trio,quart,doremi,band,orchestra
scores = [[None] * 9, [None] * 9]
permanent_scores = [[None] * 9, [None] * 9]

dice = [0, 0, 0, 0, 0]
title()
functions.ShowTableByList("Scoreboard", names, categories, scores)

scores[0] = [0] * 9
scores[1] = [0] * 9

permanent_scores[0] = [0] * 9
permanent_scores[1] = [0] * 9

playersscore()
playerturn()

print("=" * 8)
input("Press ENTER to roll dice. \n")
outer_loop_breaker = 1

for i in range(1, 19):
    outer_loop_breaker = 1
    if i != 1:
        title()
        functions.ShowTableByList("Scoreboard", names, categories, permanent_scores)

        playersscore()
        playerturn()

        print("=" * 8)
        input("Press ENTER to roll dice. \n")


    for ii in range(1, 4):

        if outer_loop_breaker == 0:
            outer_loop_breaker = 1
            break

        if custom_dice_activated == True:
            dice = custom_dice.copy()
            custom_dice_activated = False
            dice_output = dice
        elif custom_dice_activated == False:
            dice_output = randomdice(dice)

        print("Roll #" + str(ii) + ": " + str(dice_output) + "\n")
        scores[currentplayerlist()][0] = like_terms(dice)[0]
        scores[currentplayerlist()][1] = like_terms(dice)[1]
        scores[currentplayerlist()][2] = like_terms(dice)[2]
        scores[currentplayerlist()][3] = like_terms(dice)[3]
        scores[currentplayerlist()][4] = trio(dice)
        scores[currentplayerlist()][5] = quartet(dice)
        scores[currentplayerlist()][6] = doremi(dice)
        scores[currentplayerlist()][7] = band(dice)
        scores[currentplayerlist()][8] = orchestra(dice)
        # band category
        scores[currentplayerlist()][8] = orchestra(dice)
        functions.ShowTableByList("Category Scores", [], categories, [scores[currentplayerlist()]])


        x = True

        if ii < 3:
            print("Input options:")
            print("SAVE :- Accept these dice.")
            print("ROLL :- Re-roll All dice.")
            print("ROLL d1 :- Re-roll specified dice only. \n")

        while x:
            if ii == 3:
                break
            input_option = input("Input > ")

            # check if the input is valid

            if input_option.lower() == "roll" or input_option.lower() == "save" or input_option.lower().split()[
                0] == "roll" and len(input_option.lower().split()[1:]) <= 5 and checkList(
                    input_option.lower().split()[1:]) == True or input_option.lower().split()[0] == "cheat" and len(
                    input_option.lower().split()[1:]) == 5 and checkList(
                    input_option.lower().split()[1:]) == True and check_cheat_numbers(
                    input_option.lower().split()[1:]) == True and cheat_activated[currentplayerlist()] == False:
                # print(ii)
                break
                # dice_numbers = [int(x) for x in input_option.lower().split()[1:]]
            else:
                print("ERROR: Invalid input.")

        if input_option.lower() == "save" or ii == 3:

            while b == 1:
                desired_category = input("Enter your desired category: ")
                if desired_category.lower() in categories_lowercase:
                    if players_categories[currentplayerlist()][str(desired_category.lower())] == 0:
                        add_score(desired_category.lower())
                        functions.ClearScreen()
                        players_categories[currentplayerlist()][str(desired_category.lower())] = 1
                        nextturn()
                        outer_loop_breaker = 0
                        break
                    else:
                        print("ERROR: Category '" + desired_category.lower() + "' has been used.")
                else:
                    print("ERROR: Category '" + desired_category.lower() + "' does not exist.")

        elif input_option.lower() == "roll":
            ii += 1

			elif input_option.lower().split()[0] == "roll":

				x = list_input = [int(i) for i in input_option.lower().split()[1:]]
				x.sort()
				custom_dice = dice.copy()
				for z in range(len(x)):
					if x[z]:
						custom_dice[z] = random.randrange(1, 4)
				custom_dice_activated = True
				ii += 1

        elif input_option.lower().split()[0] == "cheat":
            x = list_input = [int(i) for i in input_option.lower().split()[1:]]
            x.sort()
            cheat_dice = x
            scores[currentplayerlist()][0] = like_terms(cheat_dice)[0]
            scores[currentplayerlist()][1] = like_terms(cheat_dice)[1]
            scores[currentplayerlist()][2] = like_terms(cheat_dice)[2]
            scores[currentplayerlist()][3] = like_terms(cheat_dice)[3]
            scores[currentplayerlist()][4] = trio(cheat_dice)
            scores[currentplayerlist()][5] = quartet(cheat_dice)
            scores[currentplayerlist()][6] = doremi(cheat_dice)
            scores[currentplayerlist()][7] = band(cheat_dice)
            scores[currentplayerlist()][8] = orchestra(cheat_dice)
            # band category
            functions.ShowTableByList("Category Scores", [], categories, [scores[currentplayerlist()]])
            while k == 1:
                desired_category = input("Enter your desired category: ")
                if desired_category.lower() in categories_lowercase:
                    if players_categories[currentplayerlist()][str(desired_category.lower())] == 0:
                        add_score(desired_category.lower())
                        functions.ClearScreen()
                        players_categories[currentplayerlist()][str(desired_category.lower())] = 1
                        cheat_activated[currentplayerlist()] = True
                        nextturn()
                        outer_loop_breaker = 0
                        break
                    else:
                        print("ERROR: Category '" + desired_category.lower() + "' has been used.")

functions.ClearScreen()
title()
functions.ShowTableByList("Scoreboard", names, categories, permanent_scores)
playersscore()
winner()
print("=" * 8)
input("Press ENTER to exit. \n")
exit()
