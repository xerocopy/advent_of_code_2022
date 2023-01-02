#Day 9: Rope Bridge
import math
import numpy as np

def openfile():
    with open('test.txt', mode = 'r') as f:
        file = f.readlines()
        return file

def move(h, t, line, trail):
    '''
    give the new h_ position
    '''
    ori = line[0]
    step = int(line[-1])
    if ori == 'U':
        h[1] += step
        np.sign()
        

    elif ori == 'D':
        h[1] -= step
    elif ori == 'L':
        h[0] -= step
    elif ori == 'R':
        h[0] += step


    
    




if __name__ == "__main__":
    file = openfile()
    h = [0,0]
    t = [0,0]           # initial tail position aka s
    trail = []    # tail travel history
    for line in file:
        h  = move(h, t, line.strip())
        print(line.strip(), t, h, trail)





