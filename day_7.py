# Day 7 No Space Left On Device (Tree)
# 1749646

def openfile():
    with open('input7.txt', mode = 'r') as f:
        return f.readlines()

def read_command(file):
    '''list the files and their directories'''
    pwd = ''
    cnt = 0
    n_ls = 0
    n_cd_down = 0
    n_cd_up = 0
    n_dir = 0
    cnt_file = 0
    for line in file:
        cl = line.strip().split(' ')
        #print(cl)
        cnt += 1
        if cl[0] == '$':
            if cl[1] == 'cd' and cl[2] != '..':
                #print(line.strip('\n'))
                dir_size_list.append([pwd, cl[2], 0, 'dir']) # this calculate folders only contain sub-folders
                n_cd_down += 1
                if cl[2] == '/':
                    pwd = cl[2]
                else:
                    pwd += (cl[2] + '/')
                #print('Current pwd is {}'.format(pwd))
            elif cl[1] == 'cd' and cl[2] == '..':
                n_cd_up += 1
                pwd = pwd[:-1]
                while pwd[-1] != '/':
                    pwd = pwd[:-1]
                #print('Current pwd is {}'.format(pwd))
            elif cl[1] == 'ls':
                #print('List Current directory: {}'.format(pwd))
                n_ls+=1
        elif cl[0] == 'dir':
            #print(line.strip('\n'))
            n_dir += 1
        elif cl[0].isnumeric():
            cnt_file += 1
            size = cl[0]
            filename = cl[1]
            #print(pwd, filename, size)
            dir_size_list.append([pwd, filename, size, 'file']) # this calculate all the files
    print('total {} commands read! {} files found! {} dir, {} ls, {} cd up, {} cd down'.format(cnt, cnt_file, n_dir, n_ls, n_cd_up, n_cd_down))
    return dir_size_list
def find_dir(dir_size_list):
    '''
    1. find every directory (including subdirectory)
    2. check the size of every directory (incl. sub dir)
    '''
    for i in range(len(dir_size_list)):
        #print(dir_size_list[i])
        cnt = 0
        names = []
        tot_size = 0
        pwd = dir_size_list[i][0]
        for j in range(len(dir_size_list)):
            if pwd == dir_size_list[j][0][:len(pwd)]:
                names.append(dir_size_list[j][1])
                tot_size += int(dir_size_list[j][2])
                cnt += 1
                #print(i, pwd, j, dir_size_list[j][0], dir_size_list[j][1], cnt)
                #print(pwd, dir_size_list[j][0], cnt, dir_size_list[j][1], dir_size_list[j][2])
        #print('{},{}:  There are {} files in directory {}: {} with total size of {}'.format(i,j,cnt, pwd, names, tot_size))
        if pwd not in dir_tar_final and int(tot_size) < 100000:
            dir_tar_final[pwd] = [cnt, names, tot_size]
    return dir_tar_final


def folder_filter(dir_tar_final):
    for item in dir_tar_final.items():
        #print(item[0], item[1][2])
        if int(item[1][2]) < 100000 and item[0] not in final:
            #print(item[0], item[1][2])
            final[item[0]] = int(item[1][2])
    return final

def cal(final):
    tot = 0
    for item in final.items():
        tot += item[1][2]
    return tot


if __name__ == '__main__':
    dir_size_list = []
    dir_tar_final = {}
    final = {}
    file = openfile()
    dir_size_list = read_command(file)


    # list of all the files
    with open('day_7_tmp_dir_size_list.txt', 'w') as f:
        for i in dir_size_list:
            f.write(str(i) + '\n')

    dir_tar_final = find_dir(dir_size_list)
    # # dictionary of all the satisfactory directories
    with open('day_7_tmp_dir_tar_final.txt', 'w') as f:
        for i in dir_tar_final.items():
            f.write(str(i) + '\n')

    tot = cal(dir_tar_final)
    print(tot)

