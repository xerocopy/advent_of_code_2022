# Day #3 Rucksack Reorganization

def findcommonitem(str1, str2):
    for i in str1:
        print(i, 'is the first item in str1')

    item = 'a'
    return item

def ascii(char):
    '''
    Lexicographic order for letters a-z and A-Z
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
