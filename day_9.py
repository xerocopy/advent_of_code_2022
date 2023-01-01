#Day 9: Rope Bridge
import math
def openfile():
    with open('test.txt', mode = 'r') as f:
        file = f.readlines()
        return file

def movehead(h, line):
    '''
    give the new h_ position
    '''
    ori = line[0]
    step = int(line[-1])
    if ori == 'U':
        h[1] += step
    elif ori == 'D':
        h[1] -= step
    elif ori == 'L':
        h[0] -= step
    elif ori == 'R':
        h[0] += step
    return h


def movetail(h_, h, t, trail):
    '''
    move the tail following head
    '''
    x1, y1, l1 = vector(h, t) #vectorise the previous position of ht
    x2, y2, l2 = vector(h_, h) # vectorise the head moving direction
    print(x1, y1, x2, y2)


    if x1 * x2 > 0 and y1 * y2 == 0:  # moving horizontal same direction, the l2 is the tail moving trail
        l2

    elif x1 * x2 < 0 and y1 * y2 == 0: # moving horizontal opposite direction, l2 - 2 is the real tail moving trail
        l2 -2


    elif x1 * x2 == 0 and y1 * y2 == 0:  # vertical to each other , the moving distance is different
        l2 -1


    elif x1 * x2 == 0 and y1 * y2 > 0: # moving vertical same direction, l2 is the tail moving trail
        l2

    elif x1 * x2 == 0 and y1 * y2 < 0: # moving vertical opposite direction, l2 -2 is the real tail moving trail
        l2 -2

    return t_, trail


def vector(h, t):
    '''
    give the h - t direction
    '''
    x = h[0] - t[0]
    y = h[1] - t[1]
    l = math.sqrt(x**2 + y**2)
    return x, y, l



if __name__ == "__main__":
    file = openfile()
    h = [0,0]
    t = [0,0]           # initial tail position aka s
    trail = []    # tail travel history
    for line in file:
        h_ = movehead(h, line.strip())
        t_, trail = movetail(h_, h, t, trail)
        print(line.strip(), t, h, trail)





