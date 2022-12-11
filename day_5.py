# Day 5 Supply Stacks


def load_stack(line):
    print(line)
    for i in range(9):
        #print('to load the stack {}, checking the line position {}'.format(i, (1+4*i)))
        if line[(1+4*i)] == ' ':
            continue
            #print('blank')
        elif line[(1+4*i)] == str(i + 1):
            continue
            #print('load stack done!!')
        else:
            #print(i, (1+4*i), line[(1+4*i)])
            stack[i].append(line[(1+4*i)])
            #print('load {} into position stack {} at position {}'.format(line[(1+4*i)], i, (1+4*i)))
    return stack

def reverse_stack(stack):
    for i in range(9):
        stack[i].reverse()
    return stack

def load_command(line):
    token_list = line.split(' ')
    num = int(token_list[1])
    start = int(token_list[3])
    end = int(token_list[5])
    command_list.append([num, start, end])
    return command_list

def move(stack, command_list):
    num = command_list[0][0]
    start = command_list[0][1]
    end = command_list[0][2]
    for i in range(num):
        #print('Step {} : Move {} items from {} to {}'.format(i, num, start, end))
        stack[end-1].append(stack[start-1][-1])
        del stack[start-1][-1]
    del command_list[0]
    if command_list != []:
        print(stack, command_list[0])
        move(stack, command_list)
    return stack

def new_move(stack, command_list):
    num = command_list[0][0]
    start = command_list[0][1]
    end = command_list[0][2]
    for i in range(num):
        stack[end-1].append(stack[start-1][-num + i])
        del stack[start-1][-num + i]
    del command_list[0]
    if command_list != []:
        print(stack, command_list[0])
        new_move(stack, command_list)
    return stack




if __name__ == '__main__':
    command_list = []
    stack = []
    top_crate = []
    for i in range(1, 10):
        stack.append([])
    #print(stack)
    with open('input5.txt', mode = 'r') as f:
        for line in f:
            if line[:4] != 'move' and line != '\n':
                stack = load_stack(line.strip('\n'))
            elif line[:4] == 'move':
                command_list = load_command(line.strip('\n'))
    stack = reverse_stack(stack)
    final_stack = new_move(stack, command_list)
    print(final_stack)
    for i in range(9):
        top_crate.append(final_stack[i][-1])
    #print(top_crate)
    str = ''
    for i in top_crate:
        str += i
    print(str)





