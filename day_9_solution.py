import aocd
import numpy as np


def part_one():

    with open('input9.txt', mode='r') as f:
        input = f.readlines()

    #input = aocd.get_data(year=2022, day=9).splitlines()

    head = (0, 0)
    tail = (0, 0)
    visited = set()
    visited.add(tail)

    for motion in input:
        direction, steps = motion.split()
        for _ in range(int(steps)):
            match direction:
                case 'U':
                    head = (head[0], head[1] + 1)
                case 'D':
                    head = (head[0], head[1] - 1)
                case 'R':
                    head = (head[0] + 1, head[1])
                case 'L':
                    head = (head[0] - 1, head[1])
            diff_x = head[0] - tail[0]
            diff_y = head[1] - tail[1]
            if abs(diff_x) > 1 or abs(diff_y) > 1:
                tail = (tail[0] + np.sign(diff_x), tail[1] + np.sign(diff_y))
                visited.add(tail)
    return len(visited)


def main():
    print(part_one())


if __name__ == '__main__':
    main()