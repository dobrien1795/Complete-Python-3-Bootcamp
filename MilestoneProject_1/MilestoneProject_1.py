#First Milestone project
#Create 2 player TicTacToe game

#Create it all in a function and return at the end of the game

#Function to print table when needed
def print_table(input_dict):
    table = print(' {AA} | {AB} | {AC} \n'
          '---------\n'
          ' {BA} | {BB} | {BC} \n'
          '---------\n'
          ' {CA} | {CB} | {CC}\n'.format(AA=input_dict['AA'], AB=input_dict['AB'], AC=input_dict['AC'],
        BA=input_dict['BA'], BB=input_dict['BB'], BC=input_dict['BC'],
        CA=input_dict['CA'], CB=input_dict['CB'], CC=input_dict['CC']))

    return table

#Function to check if the game is over and who won
def check_end(input_dict,used_locations):
    #If someone won
    if((input_dict['AA'] == input_dict['AB'] == input_dict['AC']) or
    (input_dict['BA'] == input_dict['BB'] == input_dict['BC']) or
    (input_dict['CA'] == input_dict['CB'] == input_dict['CC']) or
    (input_dict['AA'] == input_dict['BA'] == input_dict['CA']) or
    (input_dict['AB'] == input_dict['BB'] == input_dict['CB']) or
    (input_dict['AC'] == input_dict['BC'] == input_dict['CC']) or
    (input_dict['AA'] == input_dict['BB'] == input_dict['CC']) or
    (input_dict['AC'] == input_dict['BB'] == input_dict['CA'])):
        return True
    #If it's a draw
    elif (set(input_dict.keys()) == set(used_locations)):
        return 'Draw'
    else:
        return False

#Main function
#Could probably make this smaller and
#Create a separate function for user input
def tic_tac_toe():

    #Variables needed to play
    table_dict = {'AA':'AA','AB':'AB','AC':'AC',
                  'BA':'BA','BB':'BB','BC':'BC',
                  'CA':'CA','CB':'CB','CC':'CC'};
    #This will store used locations so they can't be picked again
    #Will also be used to determine when the end of the game is a draw
    used_spaces = []

    #Variables to keep track of whos turn it is
    player1 = 0
    player2 = 0

    #Start off user introduction
    print('This is the format:')
    print_table(table_dict)
    print("Player 1 will be 'X' and Player 2 will be 'O'")
    print('To make your move type the location you want to place your symbol e.g. AA/CB/...')
    play_game = input('Are you ready to play TicTacToe? (Y/N): ')

    #Start game loop
    if play_game == 'Y':
        game_on = True
        print('Ok lets start')
    else:
        game_on = False


    while game_on:

        #Player 1s turn, udpate if entry is correct, start again if not
        if player1 == 0:
            player1_input = input("Player 1's turn, enter location: ")

            #If the players pick is ok, then proceed with the below
            if (player1_input not in used_spaces) and (player1_input in table_dict.keys()):
                table_dict[player1_input] = 'X'
                used_spaces.append(player1_input)
                print_table(table_dict)

                #Check if they've won
                if(check_end(table_dict, used_spaces) == True):
                    return print('Game over. Winner is: Player 1')
                #Check if they've drawn
                elif (check_end(table_dict, used_spaces) == 'Draw'):
                    return print('Game over. It is a draw')
                player1 = 1
                player2 = 0

            #If selection is invalid, then ask them ro reinput
            elif (player1_input in used_spaces) or (player1_input not in table_dict.keys()):
                print('Invalid selection')
                continue

        #Player 2's input
        #Same logic as for Player 1
        if player2 == 0:
            player2_input = input("Player 2's turn, enter location: ")
            if (player2_input not in used_spaces) and (player2_input in table_dict.keys()):
                table_dict[player2_input] = 'O'
                used_spaces.append(player2_input)
                print_table(table_dict)
                if (check_end(table_dict, used_spaces) == True):
                    return print('Game over. Winner is: Player 2')
                elif (check_end(table_dict, used_spaces) == 'Draw'):
                    return print('Game over. It is a draw')
                player1 = 0
                player2 = 1

            elif (player2_input in used_spaces) or (player2_input not in table_dict.keys()):
                print('Invalid selection')
                continue

    else:
        return print('Game has been ended')


end_game = tic_tac_toe()