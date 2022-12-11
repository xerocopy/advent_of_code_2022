# CAMP CLEANUP

def convert_line(line):
    left = line.split(',')[0]
    right = line.split(',')[1]
    new_line = (left, right)
    return new_line
def compare(new_line):
    left, right = new_line
    if left in right or right in left:
        return True
    else: return False


cnt = 0
with open('input4.txt', mode = 'r') as f:
    for line in f:
        new_line = convert_line(line.strip('\n'))
        print(new_line)
