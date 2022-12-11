# CAMP CLEANUP

def convert_line(line):
    left = line.split(',')[0]
    right = line.split(',')[1]
    left_list = [int(left.split('-')[0]),int(left.split('-')[1])]
    right_list = [int(right.split('-')[0]),int(right.split('-')[1])]
    new_line = [left_list, right_list]
    return new_line

def compare(new_line):
    left, right = new_line
    if left[0] <= right[0] and left[1] >= right[1]:
        return True
    elif left[0] >=right[0] and left[1] <= right[1]:
        return True
    else:
        return False

def overlap(new_line):
    left, right = new_line
    if left[0] > right[1]:
        return False
    elif left[1] < right[0]:
        return False
    else:
        return True

if __name__ == '__main__':
    with open('input4.txt', mode = 'r') as f:
        cnt = 0
        for line in f:
            #print(line)
            new_line = convert_line(line.strip('\n'))
            #print(new_line)
            #if compare(new_line):
            if overlap(new_line):
                cnt += 1
        print(cnt)

