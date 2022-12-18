# Day 7 No Space Left On Device (Tree)

def openfile():
    with open('input7.txt', mode = 'r') as f:
        return f.readlines()

def read_command(file):
    pwd = ''
    filename =''
    for line in file:
        cl = line.strip().split(' ')
        #print(cl)
        if cl[0] == '$':
            if cl[1] == 'cd' and cl[2] != '..':
                #print(line.strip('\n'))
                if cl[2] == '/':
                    pwd = cl[2]
                else:
                    pwd += (cl[2] + '/')
                #print('Current pwd is {}'.format(pwd))
            elif cl[1] == 'cd' and cl[2] == '..':
                pwd = pwd[:-1]
                while pwd[-1] != '/':
                    pwd = pwd[:-1]
                #print('Current pwd is {}'.format(pwd))
            elif cl[1] == 'ls':
                #print('List Current directory: {}'.format(pwd))
                continue
        elif cl[0] == 'dir':
            #print(line.strip('\n'))
            continue
        elif cl[0].isnumeric():
            size = cl[0]
            filename = cl[1]
            #print(filename, size)
            dir_size_list.append([pwd, filename, size])
    return dir_size_list

def find_dir(dir_size_list):
    '''
    1. find every directory (including subdirectory)
    2. check the size of every directory (incl. sub dir)
    '''
    for i in range(len(dir_size_list)):
        cnt = 0
        names = []
        tot_size = 0
        pwd = dir_size_list[i][0]
        for j in range(len(dir_size_list)):
            if pwd == dir_size_list[j][0][:len(pwd)]:
                names.append(dir_size_list[j][1])
                tot_size += int(dir_size_list[j][2])
                cnt += 1
        #print('{},{}:  There are {} files in directory {}: {} with total size of {}'.format(i,j,cnt, pwd, names, tot_size))
        if pwd not in dir_tar_final and tot_size < 100000:
            dir_tar_final[pwd] = [cnt, names, tot_size]

    return dir_tar_final


def cal_tot(dir_tar_final):
    tot = 0
    for i in dir_tar_final.items():
        tot += i[1][2]
    return tot


if __name__ == '__main__':
    dir_size_list = []
    dir_tar_final = {}

    file = openfile()
    dir_size_list = read_command(file)
    # # list of all the files
    with open('input7_dir_size_list.txt', 'w') as f:
        for i in dir_size_list:
            f.write(str(i) + '\n')

    dir_tar_final = find_dir(dir_size_list)
    # # dictionary of all the satisfactory directories
    with open('input7_dir_tar_final.txt', 'w') as f:
        for i in dir_tar_final.items():
            f.write(str(i) + '\n')

    tot = cal_tot(dir_tar_final)
    print(tot)

