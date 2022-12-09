# Day #3 Rucksack Reorganization

def findcommonitem(str1, str2):
    items = []
    for i in str1:
        for j in str2:
            if i == j:
                items.append(j)
    return items


        print(i, 'is the first item in str1', ord(i))

    item = 'a'
    return item

def ascii(char):
    '''
    ord() returns a unicode of a character
    chr() returns a character with the given unicode integer
    '''
    return chr(ord(char))


if __name__ == '__main__':
    with open('input3.txt', mode = 'r') as f:
        for line in f:
            l = len(line)
            str1 = line[:(l-int(1))//int(2)]
            str2 = line[(l-int(1))//int(2):]
            i = findcommonitem(str1, str2)
            # for i in str1:
            #     print(ascii(i))
            # print(line, l, type(line))
            # print('str1 = ', str1)
            # print('str2 = ', str2)
