# Rock Paper Scissors
def whowins(player1, player2):
    '''This function is to test who wins the game. It returns the score for player2.
    '''
    # P1: A for rock, B for paper, C for scissors
    # P2: X for rock 1, Y for paper 2, Z for scissors 3
    # 0 if p2 lost, 3 if draw, 6 if p2 won
    if player2 == 'X' and player1 == 'B':
        return 0
    elif player2 == 'X' and player1 == 'C':
        return 6
    elif player2 == 'Y' and player1 == 'A':
        return 6
    elif player2 == 'Y' and player1 == 'C':
        return 0
    elif player2 == 'Z' and player1 == 'A':
        return 0
    elif player2 == 'Z' and player1 == 'B':
        return 6
    else:
        return 3

def whattochoose(player1, result):
    '''This function is to choose what the player2 is going to play when given the expected results.
        It returns the score of the sign player to choose
    '''
    # P1: A for rock, B for paper, C for scissors
    # result: loose(X), draw(Y), win(Z)
    # P2: X for rock 1, Y for paper 2, Z for scissors 3
    # 0 if p2 lost, 3 if draw, 6 if p2 won
    if result == 'Y':
            if player1 == 'A':
                return 1
            elif player1 == 'B':
                return 2
            elif player1 == 'C':
                return 3
    elif player1 == 'A' and result == 'X':
        return 3
    elif player1 == 'B' and result == 'X':
        return 1
    elif player1 == 'C' and result == 'X':
        return 2

    elif player1 == 'A' and result == 'Z':
        return 2
    elif player1 == 'B' and result == 'Z':
        return 3
    elif player1 == 'C' and result == 'Z':
        return 1


if __name__ == '__main__':
    tot = []
    with open('input2.txt', mode = 'r') as f:
        for line in f:
            temp = list(line.strip())
            player1 = temp[0]
            #player2 = temp[-1]
            result = temp[-1]
            #print(player1, player2)
            cnt = int(0)
            # part_1 of the day
            # P2: X for rock 1, Y for paper 2, Z for scissors 3
            # if player2 == 'X':
            #     cnt += 1
            # elif player2 == 'Y':
            #     cnt += 2
            # elif player2 == 'Z':
            #     cnt += 3
            # cnt += whowins(player1, player2)

            #part_2 of the day
            # result: loose(X), draw(Y), win(Z)
            if result == 'X':
                cnt += 0
            elif result == 'Y':
                cnt += 3
            elif result == 'Z':
                cnt += 6
            cnt += whattochoose(player1, result)
            tot.append(cnt)
        print(sum(tot))



