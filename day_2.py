# Rock Paper Scissors
with open('input2.txt', mode = 'r') as f:
    for line in f.readlines():
        if line == '':
            print('next game...')
        else:
            print(line)
