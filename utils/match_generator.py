import random

DRAWS = []


def init():
    for k in ['p', 's', 'm']:
        for i in range(9):
            for x in range(4):
                DRAWS.append(str(i) + k)
    for i in range(7):
        for x in range(4):
            DRAWS.append(str(i) + 'z')
    random.shuffle(DRAWS)
