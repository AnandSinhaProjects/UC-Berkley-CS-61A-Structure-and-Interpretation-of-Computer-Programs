# Imports Start here ->
from random import randint
# Imports End here -----------------------------------------------

# Boilerplate Code like the defaults and everthing is here.

six_sided = 6
four_sided = 4
score_main = 0
score_opp = 0
pig_tail = lambda x: 2 * abs(int(str(x)[0]) - int(str(x)[1])) + 1
#----------------------------------------------------------------   

# This function is used to start the game in both test and benchmark mode.
print('Follow format def start_game(num_rolls, faces, total_score, outcomes)')
def start_game(num_rolls:int=0, total_score:int=100, faces:int=six_sided,  outcomes:str=''):
    # faces = int(input('Enter the number of faces'))
    # num_rolls = int(input('Number of rolls to play'))
    # outcomes = input()
    if outcomes == 'random':
        outcomes = dice_roll(num_rolls,faces)
    else:
        outcomes = list(map(int, outcomes.split()))
    return outcomes
  
#This function tries to mimic the behavior of of a dice roll with n faces.

def dice(faces):
    assert type(faces)==int and faces>=1, 'Illegal side value for dice'
    return randint(1,faces)

# This functions is used to get the Dice rolls meaning this give 
# the list for total num_rolls say num_rolls = 1 then l will be maybe [4].

def dice_roll(num_rolls,faces=six_sided):
    outcomes = []
    for i in range(num_rolls):
        outcomes.append(dice(faces))
    return outcomes

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
def take_turn(outcomes):
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
