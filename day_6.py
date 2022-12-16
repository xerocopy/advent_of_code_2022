#Day 6: Tuning Trouble


def openfile():
    with open('input6.txt', mode = 'r') as f:
        return f.read()

def findsignal(str, l):
    for i in range(len(str)-l +1):
        marker = []
        for j in range(l):
            marker.append(str[i + j])
        print(i, marker)
        if checkmarker(marker, l):
            print('Find marker at i = {}.'.format(i))
            return i

def checkmarker(marker, l):
    if len(marker) < l:
        return False
    elif len(marker) == l:
        while len(marker) != 0:
            if marker.pop() in marker:
                return False
        return True


if __name__ == '__main__':
    f = openfile()
    l = int(14)
    print(findsignal(f, l) + l)

