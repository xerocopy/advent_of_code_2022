#Day 9: Rope Bridge
import numpy as np

def openfile():
    with open('test.txt', mode = 'r') as f:
        file = f.readlines()
        return file

def move(head, tail, line, trail): # Part 1
    '''
    give the new h_ position
    '''
    direction = line[0]
    step = int(line[-1])
    for _ in range(step):
        if direction == 'U':
            head = (head[0], head[1] + 1)
        elif direction == 'D':
            head = (head[0], head[1] - 1)
        elif direction == 'R':
            head = (head[0] + 1, head[1])
        elif direction == 'L':
            head = (head[0] - 1, head[1])
        x = head[0] - tail[0]
        y = head[1] - tail[1]
        if abs(x) > 1 or abs(y) > 1:
            tail = (tail[0] + np.sign(x), tail[1] + np.sign(y))
            trail.add(tail)
            #print(head, tail, trail)
    return head, tail, trail


def move2(head, tail, line, trail): # Part 2
    '''
    give the new h_ position
    '''

    direction = line[0]
    step = int(line[-1])
    for _ in range(step): # the head moves one step
        for knot in range(9): # each knot follows
            if direction == 'U':
                head = (head[0], head[1] + 1)
            elif direction == 'D':
                head = (head[0], head[1] - 1)
            elif direction == 'R':
                head = (head[0] + 1, head[1])
            elif direction == 'L':
                head = (head[0] - 1, head[1])
            x = head[0] - tail[0]
            y = head[1] - tail[1]
            if abs(x) > 1 or abs(y) > 1:
                tail = (tail[0] + np.sign(x), tail[1] + np.sign(y))
                if knot == 8:
                    trail.add(tail)
            elif abs(x) <= 1 and abs(y) <= 1:
                break
            head, tail, _ = move(head, tail, line, trail)
        print(head, tail)

    return head, tail, trail



# Part 1
# if __name__ == "__main__":
#     file = openfile()
#     head = (0,0)
#     tail = (0,0)                # initial tail position aka s, in tuples
#     trail = set()               # tail travel history in sets (not dictionary)
#     trail.add(tail)
#     for line in file:
#         head, tail, trail = move(head, tail, line.strip().split(' '), trail)
#         #print(line.strip(), tail, head, len(trail))
#     print(len(trail))



if __name__ == "__main__":
    file = openfile()
    head = (0,0)
    tail = (0,0)                # initial tail position aka s, in tuples
    trail = set()               # tail travel history in sets (not dictionary)
    trail.add(tail)
    for line in file:
        #head, tail, trail = move(head, tail, line.strip().split(' '), trail)
        head, tail, trail = move2(head, tail, line.strip().split(' '), trail)
        print(line.strip(), tail, head, len(trail))
    #print(len(trail))



