import random

board = [ '' for i in range(9)]
avail_choice = ['X','O']


def chooseMode():
    print('Welcome to TIC-TAC-TOE game')
    print('These are the playing modes : \n 1.Computer mode \n 2.Player Mode')
    choice = int(input('Enter your choice : '))
    if choice == 1:
        computerMode()
    else:
        playerMode()

def chooseStyle():
    print('Available Choices: ',avail_choice)
    u_choice = input('Enter Choice : ')
    while u_choice not in avail_choice:
        u_choice = input('Enter Choice : ')
    if u_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'
    return [u_choice,c_choice]

def computerMode():
    choices = chooseStyle()
    c_choice , u_choice = choices[1] , choices[0]
    
    while board.count(''):

        print('available places: ', availablePlaces())
        print('Your Turn...')
        box_num = int(input('Enter the box number : '))
        if box_num not in availablePlaces():
            continue
        board[box_num] = u_choice
        printBoard()
        if win():
            print('Player Won...!!!')
            break
        print('Computers turn...')
        box_num = random.choice(availablePlaces())
        board[box_num] = c_choice
        printBoard()
        if win():
            print('Computer Won...!!!')
            break

    else:
        print('The game ended in a DRAW...!!!')



def playerMode():
    choices = chooseStyle()
    c_choice, u_choice = choices[1], choices[0]

    while board.count(''):
        print(board.count(''))
        print('available places: ', availablePlaces())
        print('Player 1  Turn...')
        try:
            box_num = int(input('Enter the box number : '))
        except Exception as e:
            print('You missed the chance...')
            continue
        
        if box_num not in availablePlaces():
            continue
        board[box_num] = u_choice
        printBoard()
        if win():
            print('Player 1 Won...!!!')
            break

        if availablePlaces():
            print('available places: ', availablePlaces())
            print('Player 2  Turn...')
            try:
                box_num = int(input('Enter the box number : '))
            except Exception as e:
                print('You missed the chance...')
                continue
            if box_num not in availablePlaces():
                continue
            board[box_num] = c_choice
            printBoard()
            if win():
                print('Player 2 Won...!!!')
                break
    else:
        print('The game ended in a DRAW...!!!')


def availablePlaces():
    avail_place = []
    for i in range(len(board)):
        if board[i] == '':
            avail_place.append(i)
    return avail_place

def win():
    if (board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or (board[0] == 'O' and board[1] == 'O' and board[2] == 'O' ):
        return True
    elif (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or (board[3] == 'O' and board[4] == 'O' and board[5] == 'O'):
        return True
    elif (board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or (board[6] == 'O' and board[7] == 'O' and board[8] == 'O'):
        return True
    elif (board[0] == 'X' and board[3] == 'X' and board[6] == 'X') or (board[0] == 'O' and board[3] == 'O' and board[6] == 'O'):
        return True
    elif (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or (board[1] == 'O' and board[4] == 'O' and board[7] == 'O'):
        return True
    elif (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or (board[2] == 'O' and board[5] == 'O' and board[8] == 'O'):
        return True
    elif (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or (board[3] == 'O' and board[4] == 'O' and board[5] == 'O'):
        return True
    elif (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or (board[3] == 'O' and board[4] == 'O' and board[5] == 'O'):
        return True
    else:
        return False


def printBoard():
    print('|  {0}   |  {1}   |   {2}  |'.format(board[0],board[1],board[2]))    
    print('--------------------')
    print('|  {0}   |  {1}   |   {2}  |'.format(board[3],board[4],board[5]))    
    print('--------------------')
    print('|  {0}   |  {1}   |   {2}  |'.format(board[6], board[7], board[8]))
    

chooseMode()
