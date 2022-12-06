# Calorie Counting
cals = []
tot = 0
with open('input1.txt', mode = 'r') as f:
    for line in f.readlines():
        if line == '\n':
            print('another elf appeared ....')
            cals.append(tot)
            tot = 0
            print('total cals for last appeared elf: {}'.format(cals[-1]))
        else:
            tot += int(line)

#print(max(cals))
sorted_cals = sorted(cals, reverse = True)
print(sorted_cals[0] + sorted_cals[1] + sorted_cals[2])


