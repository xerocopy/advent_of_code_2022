# Cathode-Ray Tube

def openfile():
    with open('test.txt', 'r') as f:
        file = f.readlines()
        return file


def Part1():
    n_cycle = 0
    cycles = []
    X = 1
    sum = 0
    line_cnt = 0
    check_list = [20, 60, 100, 140, 180, 220]
    for line in openfile():
        line_cnt+=1
        if line.strip().split(' ')[0] == 'addx':
            n_cycle += 1
            if n_cycle in check_list:
                cycles.append([line_cnt, line.strip(), n_cycle, X, n_cycle * X])
            else:
                cycles.append([line_cnt, line.strip(), n_cycle, X, None])
            n_cycle += 1
            if n_cycle in check_list:
                cycles.append([line_cnt, line.strip(), n_cycle, X, n_cycle * X])
            else:
                cycles.append([line_cnt, line.strip(), n_cycle, X, None])
            X += int(line.strip().split(' ')[1])
        elif line.strip().split(' ')[0] == 'noop':
            n_cycle += 1
            if n_cycle in check_list:
                cycles.append([line_cnt, line.strip(), n_cycle, X, n_cycle * X])
            else:
                cycles.append([line_cnt, line.strip(), n_cycle, X, None])

    for item in cycles:
        if item[4] != None:
            #print(item)
            sum += item[4]
    return sum, cycles

def Part2():
    n_cycle = 0   # used to decide the drawing sequence/location on screen
    X = 1         # sprite horizontal location
    str = ''
    for line in openfile():
        if line.strip().split(' ')[0] == 'addx':
            n_cycle += 1
            x = n_cycle % 40
            y = n_cycle // 40
            if x == 39:
                print(str)
                str = ''
            else:
                if abs(X - x) <= 1:
                    str += '#'
                else:
                    str += '.'

            n_cycle += 1
            x = n_cycle % 40
            y = n_cycle // 40
            if x == 39:
                print(str)
                str = ''
            else:
                if abs(X - x) <= 1:
                    str += '#'
                else:
                    str += '.'
            X += int(line.strip().split(' ')[1])

        elif line.strip().split(' ')[0] == 'noop':
            n_cycle += 1
            x = n_cycle % 40
            y = n_cycle // 40
            if x == 39:
                print(str)
                str = ''
            else:
                if abs(X - x) <= 1:
                    str += '#'
                else:
                    str += '.'

    print('Done!')

def main():
    sum, cycles = Part1()
    print(sum)

    Part2()

if __name__ == '__main__':
    main()