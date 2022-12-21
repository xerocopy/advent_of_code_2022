# Day 8: Treetop Tree House

def openfile():
    with open('input8.txt', mode = 'r') as f:
        file = f.readlines()
        return file

def file_to_table(file):
    '''make the data into a dataframe'''
    n_rows = 0
    df = []
    for line in file:
        row = []
        n_cols = len(line.strip())
        n_rows += 1
        for index in range(len(line.strip())):
            row.append(line.strip()[index])
        df.append(row)
    return df, n_rows, n_cols
    #print('Dimension of the forest is: {} rows by {} cols.'.format(n_rows, n_cols))

def check_tree(df):
    '''interate through trees inside the grid'''
    cnt = 0
    for i in range(1, len(df)-1):
        for j in range(1, len(df)-1):
            if check_visibility(df, i, j):
                cnt +=1
    return cnt


def check_visibility(df, i, j):
    '''check visibility of each tree inside the grid'''
    height = df[i][j]
    not_vis = 0
    # direction 1
    for n in range(0, i):
        if df[n][j] < height:
            continue
        else:
            not_vis += 1
            break
    # direction 2
    for n in range(i + 1, len(df)):
        if df[n][j] < height:
            continue
        else:
            not_vis += 1
            break
    # direction 3
    for n in range(0, j):
        if df[i][n] < height:
            continue
        else:
            not_vis += 1
            break
    # direction 4
    for n in range(j + 1, len(df)):
        if df[i][n] < height:
            continue
        else:
            not_vis += 1
            break

    if not_vis == 4:
        return False
    else:
        return True

def check_tree2(df):
    '''interate through trees inside the grid'''
    scores = []
    tmp = []
    for i in range(1, len(df)-1):
        for j in range(1, len(df)-1):
            score = view_range(df, i, j)
            scores.append(score[3])
    return max(scores)


def view_range(df, i, j):
    height = df[i][j]
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    cnt_4 = 0
    # direction 1
    for n in reversed(range(0, i)):
        if df[n][j] < height:
            cnt_1 += 1
        else:
            cnt_1 += 1
            break
    # direction 2
    for n in range(i + 1, len(df)):
        if df[n][j] < height:
            cnt_2 += 1
        else:
            cnt_2 += 1
            break
    # direction 3
    for n in reversed(range(0, j)):
        if df[i][n] < height:
            cnt_3 += 1
        else:
            cnt_3 += 1
            break
    # direction 4
    for n in range(j + 1, len(df)):
        if df[i][n] < height:
            cnt_4 += 1
        else:
            cnt_4 += 1
            break

    return [i, j, df[i][j], cnt_1 * cnt_2 * cnt_3 * cnt_4, cnt_1, cnt_2, cnt_3, cnt_4]


if __name__ == '__main__':
    file = openfile()
    df, n_rows, n_cols = file_to_table(file)

    cnt_interior = check_tree(df)
    cnt_exterior = n_cols * 2 + n_rows * 2 - 4
    print('Part1 Answer: {}'.format(cnt_interior + cnt_exterior))
    print('Part2 Answer: {}'.format(check_tree2(df)))
