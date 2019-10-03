# main_matrix = [[1,2,3],[4,5,6],[7,8,9]]
# def matrix():
#     return main_matrix

def magic(player_place_list, each_choice_list):
    main_matrix = [[1,2,3],[4,5,6],[7,8,9]]
    if not player_place_list:
        main_matrix = [[1,2,3],[4,5,6],[7,8,9]]
    else:
        for ind_1,i in enumerate(main_matrix):
            for ind_2,a in enumerate(i):
                if str(a) in player_place_list:
                  ind_3 = player_place_list.index(str(a))
                  main_matrix[ind_1][ind_2] = each_choice_list[ind_3]
                else:
                    main_matrix[ind_1][ind_2] = a
    return main_matrix    

def display_board(player_place_list, each_choice_list):
    board = ''
    for index,i in enumerate(magic(player_place_list, each_choice_list)):
        for n,a in enumerate(i):
            board += str(a)+'|'
            if n == len(i) - 1:
                board = board + '\n'
                break
    return board

def player_selection():
    player2 =''
    while player2 == '':
        player1 =input('Player 1 please select between "x" or "o" begin the game: ').lower()
        if player1 in ('x','o'):
            if player1 == 'x':
                player2 = 'o'
                print(f'Player_1 has selected {player1} and Player_2 has selected {player2}')
            else:
                player2 = 'x'
                print(f'Player_1 has selected {player1} and Player_2 has selected {player2}')
        else:
            print('Please enter a valid selection to begin the game')
    player_selection = [player1,player2]
    return player_selection 

def player_place(each_choice_list,selection,player_place_list,player_place_selection):
    for i in [[1,2,3],[4,5,6],[7,8,9]]:
        if player_place_selection in str(i):
            if player_place_selection not in player_place_list:
                print(f'Great Job!!')
                player_place_list.append(player_place_selection)
            else:
                print(f'Position {player_place_selection} is already occupied. Please enter a valid number between 1-9 that is on the the board')
                player_turn(each_choice_list,selection,player_place_list)
            break
    else:
        print('Please enter a valid number between 1-9 that is on the the board')
        player_turn(each_choice_list,selection,player_place_list)

def player_turn(each_choice_list,selection,player_place_list):
    if len(each_choice_list) == 0:
        player_place_selection = input(f'Player_1 please select where you want to insert your {selection[0]}: ')
        player_place(each_choice_list,selection,player_place_list,player_place_selection)
        return (selection[0])
    else:
        if each_choice_list[-1] == selection[0]:
            player_place_selection  = input(f'Player_2 please select where you want to insert your {selection[1]}: ')
            player_place(each_choice_list,selection,player_place_list,player_place_selection)
            return (selection[1])
        else:
            player_place_selection  = input(f'Player_1 please select where you want to insert your {selection[0]}: ')
            player_place(each_choice_list,selection,player_place_list,player_place_selection)
            return (selection[0])

def game_win(player_place_list, each_choice_list):
    main_matrix = magic(player_place_list, each_choice_list)
    winning_list = [['x','x','x'], ['o','o','o']]
    # game_win = None
    if [a for a in main_matrix for i in winning_list if a == i]:
        game_win = True
    elif [a for a in list(zip(main_matrix[0],main_matrix[1],main_matrix[2])) for i in winning_list if i ==list(a)]:
        game_win = True
    elif [a for a in winning_list if a == [main_matrix[0][0],main_matrix[1][1],main_matrix[2][2]]]:
        game_win = True
    elif [a for a in winning_list if a == [main_matrix[0][2],main_matrix[1][1],main_matrix[2][0]]]:
        game_win = True
    else:
        game_win = False
    return game_win

def winner(player_place_list, each_choice_list,selection):
    if game_win(player_place_list, each_choice_list):
        if selection[0] == each_choice_list[-1]:
            print('Player1 has won the game')
        else:
            print('Player2 has won the game')
        return True
    elif (len(each_choice_list) == 9):
        print('Tie game!! Game Over!!')
        return True

    else:
        return False


def each_choice():
    start = True
    while start:
        game = True
        while game:
            selection = player_selection()
            print(selection)
            print(f'Player1 will start the game with: {selection[0]}')

            each_choice_list = []
            player_place_list = []

            while not winner(player_place_list, each_choice_list, selection):
                    print(display_board(player_place_list, each_choice_list))
                    each_choice_list.append(player_turn(each_choice_list,selection,player_place_list))
                    display_board(player_place_list, each_choice_list)
                    # winner(player_place_list, each_choice_list, selection)
            game = False
        start = replay()

def replay():
    replay = input('Do you want to play again: y or n: ')
    if replay == 'y':
        start = True
    else:
        start = False
    return start
each_choice()

# def final():
#     game = True
#     while game:
#         each_choice()