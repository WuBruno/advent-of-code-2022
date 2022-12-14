def main():
    values = open("input.txt", "r")

    return sum([score2(*x.strip().split(' ')) for x in values])

"""
X -- rock
Y -- paper
Z -- scissor

A -- rock
B -- paper
C -- scissors
"""
def score2(opponent, strategy):

    if opponent == 'A':
        if strategy == 'X':
            return 3 + result_points(strategy)
        if strategy == 'Y':
            return 1 + result_points(strategy)
        if strategy == 'Z':
            return 2 + result_points(strategy)
            
    if opponent == 'B':
        if strategy == 'X':
            return 1 + result_points(strategy)
        if strategy == 'Y':
            return 2 + result_points(strategy)
        if strategy == 'Z':
            return 3 + result_points(strategy)

    if opponent == 'C': 
        if strategy == 'X':
            return 2 + result_points(strategy)
        if strategy == 'Y':
            return 3 + result_points(strategy)
        if strategy == 'Z':
            return 1 + result_points(strategy)

def score(opponent, strategy):

    if opponent == 'A':
        if mine == 'X':
            return 3 + result_points(mine)
        if mine == 'Y':
            return 6 + result_points(mine)
        if mine == 'Z':
            return presult_oints(mine)
            
    if opponent == 'B':
        if mine == 'Z':
            return 6 + points(mine)
        if mine == 'X':
            return points(mine)
        if mine == 'Y':
            return points(mine) + 3

    if opponent == 'C': 
        if mine == 'X':
            return 6 + points(mine)
        if mine == 'Y':
            return points(mine)
        if mine == 'Z':
            return 3 + points(mine)

"""
X -- lose 0
Y -- draw 3
Z -- win 6
"""
def result_points(x):
    if x == 'X':
        return 0
    if x == 'Y':
        return 3
    if x == 'Z':
        return 6

def points(x):
    if x == 'X':
        return 1
    if x == 'Y':
        return 2
    if x == 'Z':
        return 3

print(main())
