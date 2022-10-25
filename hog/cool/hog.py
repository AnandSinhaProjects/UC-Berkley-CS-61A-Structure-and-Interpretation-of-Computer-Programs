# Imports Start here ->
from random import randint
from math import sqrt
from sys import flags
# Imports End here -----------------------------------------------

# Boilerplate Code like the defaults and everthing is here.

six_sided = 6
four_sided = 4
# score_main = 0 # Player 1 Score
# score_opp = 0 # Player 2 Score
# turn_number = 0 # Total number of turns taken in the game.
pig_tail = lambda x: 2 * abs(int(str(x)[0]) - int(str(x)[1])) + 1 #Function followed for pig_tail -> 2 * abs(tens - ones) + 1 points
# faces = int(input('Enter the number of faces -> '))
# num_rolls = int(input('Number of rolls to play -> '))
#total_score = int(input('Total score to play -> '))
#outcomes = input('Either enter the list of outcomes or "random" -> ')
always_roll_5 = 5

#----------------------------------------------------------------   

#This function tries to mimic the behavior of of a dice roll with n faces.

def dice(faces:int=six_sided):
    assert type(faces)==int and faces>=1, 'Illegal side value for dice'
    return randint(1,faces)

# This functions is used to get the Dice rolls meaning this give 
# the list for total num_rolls say num_rolls = 1 then l will be maybe [4].

def dice_roll(num_rolls:int=3,faces:int=six_sided):
    outcomes = []
    for i in range(num_rolls):
        outcomes.append(dice(faces))
    return outcomes

# This function is used to start the game in both test and benchmark mode.
#print('Follow format def start_game(num_rolls, faces, total_score, outcomes)')
def start_game(num_rolls:int=0, faces:int=six_sided,  outcomes:str=''):
    # faces = int(input('Enter the number of faces -> '))
    # num_rolls = int(input('Number of rolls to play -> '))
    # outcomes = input('Either enter the list of outcomes or "random" -> ')
    if outcomes == 'random':
        outcomes = dice_roll(num_rolls,faces)
    else:
        outcomes = list(map(int, outcomes.split()))
    return outcomes

# outcomes = start_game(num_rolls, total_score, faces, outcomes)

# This function checks if the value i is 1 or not.

def sow_sad(i):
    if i == 1:
        return True
    else:
        return False

# This fucntion returns the calc for pig_tail.
# Function followed for pig_tail -> 2 * abs(tens - ones) + 1 points; 
# where tens, ones are the tens and ones digits of the opponent's score

def tail_points(score_opp):
    if score_opp == 0:
        return 0
    else:
        return(pig_tail(score_opp))    

#Calculates the total points perfectly
def take_turn(outcomes,score_opp):
    points_round = 0
    if len(outcomes) == 0:
        return tail_points(score_opp)
    else:
        for i in outcomes:
            if sow_sad(i)==True:
                return 1
            else:
                points_round += i
        return points_round

# This function calculates if the number is a square root.

def perfect_square(score):
    ips = int(sqrt(score))
    if (ips*ips) == score:
        return True,ips
    else:
        return False,0

# This function calculates the next perfect_square(score)

def next_perfect_square(n):
    return (n+1)*(n+1)

# This function calculates the new score depeding on the fact that
# the score is a perfect sqaure or not.

def square_update(score):
    flag,ips = perfect_square(score)
    if flag == False:
        return score
    if flag == True:
        return next_perfect_square(ips)

def play(p1rolls, p2rolls, game_type:str,total_score=100):
    faces = int(input('Enter the number of faces -> '))
    #num_rolls = int(input('Number of rolls to play -> '))
    turn_number = 0
    score_main = 0
    score_opp = 0
    while score_main<total_score and score_opp<total_score:
        print(turn_number)
        outcomes = 'random'#input('Either enter the list of outcomes or "random" -> ')
        round_score = 0
        if game_type == 'square_update':
            if turn_number % 2 == 0:
                num_rolls = p1rolls
                outcomes = start_game(num_rolls, faces, outcomes)
                round_score = take_turn(outcomes, score_opp)
                score_main += round_score
                score_main = square_update(score_main)
                turn_number += 1
                print('Score Player 1 -> ',score_main)
            else:
                num_rolls = p2rolls
                outcomes = start_game(num_rolls, faces, outcomes)
                round_score = take_turn(outcomes, score_main)
                score_opp += round_score
                score_opp = square_update(score_main)
                turn_number += 1
                print('Score Player 2 -> ',score_main)
        else:
            if turn_number % 2 == 0:
                num_rolls = p1rolls
                outcomes = start_game(num_rolls, faces, outcomes)
                round_score = take_turn(outcomes, score_opp)
                score_main += round_score
                turn_number += 1
                print('Score Player 1 -> ',score_main)
            else:
                num_rolls = p2rolls
                outcomes = start_game(num_rolls, faces, outcomes)
                round_score = take_turn(outcomes, score_main)
                score_main += round_score
                turn_number += 1
                print('Score Player 2 -> ',score_main)

    return score_main, score_opp
            
            