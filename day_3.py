# Day #3 Rucksack Reorganization

def findcommonitem(str1, str2):
    items = []
    for i in str1:
        for j in str2:
            if i == j:
                items.append(j)
    return items


def prioritise(char):
    '''
    ord() returns a unicode of a character
    chr() returns a character with the given unicode integer
    '''
    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.
    if ord(char) in range(ord('a'), ord('z')+int(1)):
        priority = ord(char) - ord('a') + int(1)
    elif ord(char) in range(ord('A'), ord('Z') + int(1)):
        priority = ord(char) - ord('A') + int(27)
    return priority

def findbadge(line1, line2, line3):
    '''use hash table to find key value table'''
    badges = []
    dic1 = {}
    dic2 = {}
    dic3 = {}
    for i in line1.strip('\n'):
        if i not in dic1:
            dic1[i] = 1
        elif i in dic1:
            dic1[i] += 1
    for j in line2.strip('\n'):
        if j not in dic2:
            dic2[j] = 1
        elif j in dic2:
            dic2[j] += 1
    for k in line3.strip('\n'):
        if k not in dic3:
            dic3[k] = 1
        elif k in dic3:
            dic3[k] += 1

    for i in dic1.keys():
        if i in dic2.keys() and i in dic3.keys():
            badges.append(i)
    return badges[0]

if __name__ == '__main__':
    priority_list =[]
    group = []
    with open('input3.txt', mode = 'r') as f:
        for line in f:
            # #part 1
            # l = len(line)
            # str1 = line[:(l-int(1))//int(2)]
            # str2 = line[(l-int(1))//int(2):]
            # i = findcommonitem(str1, str2)
            # print('str1 = ', str1, 'str2 = ', str2, 'common:', i, 'priority', prioritise(i[0]))
            # priority_list.append(prioritise(i[0]))

            #part 2
            group.append(line)
            if len(group) < 3:
                continue
            elif len(group) == 3:
                badge = findbadge(group[0], group[1], group[2])
                priority_list.append(prioritise(badge))
                group = []
        print(sum(priority_list))
