#Day 9: Rope Bridge
import numpy as np

def openfile():
    with open('input9.txt', mode = 'r') as f:
        file = f.readlines()
        return file

def Part2():
    file = openfile()
    head = (0,0)
    rope = []
    for _ in range(10):
        rope.append((head))
    trail = set()
    trail.add((0,0))
    for line in file:
        direction = line.split(' ')[0]
        steps = int(line.split(' ')[1])
        print('direction', direction,'steps', steps)
        for step in range(steps):
            print('step: ', step)
            for n_knot in range(9):
                print('n_knot: ', n_knot)
                if n_knot == 0:  # this is the head knot
                    if direction == 'U':
                        rope[n_knot] = (rope[n_knot][0], rope[n_knot][1] + 1)
                    elif direction == 'D':
                        rope[n_knot] = (rope[n_knot][0], rope[n_knot][1] - 1)
                    elif direction == 'R':
                        rope[n_knot] = (rope[n_knot][0] + 1, rope[n_knot][1])
                    elif direction == 'L':
                        rope[n_knot] = (rope[n_knot][0] - 1, rope[n_knot][1])
                    rope, trail = move_next(n_knot, rope, trail)
                else:
                    rope, trail = move_next(n_knot, rope, trail)

    return rope, len(trail)

def move_next(n_knot, rope, trail):
        x = rope[n_knot][0] - rope[n_knot+1][0]
        y = rope[n_knot][1] - rope[n_knot+1][1]
        if abs(x) > 1 or abs(y) > 1:
            rope[n_knot+1] = (rope[n_knot+1][0] + np.sign(x), rope[n_knot+1][1] + np.sign(y))
            if n_knot == 8:
                trail.add(rope[n_knot+1])
                print(rope[0], rope[-1], len(trail))
            else:
                print('now moving: ',n_knot, n_knot+1)
        return rope, trail

def main():
    print(Part2())

if __name__ == "__main__":
    main()