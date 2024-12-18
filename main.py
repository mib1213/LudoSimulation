import random

dice = random.randint(0, 5)

colors = [range(4)]

steps, win = [0] * 4

def move_figure(steps, index, dice):
    steps[index] += dice

    modulo = steps[index] % 10
    for figure in steps:
        if figure % 10 == modulo:
            figure = 0

def check_winner(steps):
    maximum_step = max(steps)

    if maximum_step >= 40:
        return steps.index(maximum_step)
    return None
    
while True:
    steps = move_figure(steps)
    
    winner = check_winner(steps)

    if winner:
       break

print(winner)