#Tik tac toe
#Game
#while loop to keep running the game
print('welcome to tick tac toe')
while True:
    #play the game
    
    ##Set everything up(board, who is first, what marker chosen)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    
    turn = choose_player()
    print(turn)
    
    play_game = input('Ready to play? y or n?')
    if play_game =='y':
        game_on = True
    else:
        game_on = False
    
    
    
    ###Gameplay
    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            #choose position
            position = player_choice(the_board)
            #place marker
            place_marker(the_board,player1_marker,position)
            #check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game!')
                    game_on = False
                else:
                    turn = 'Player 2'
            
        else:
            if turn == 'Player 2':
            #show the board
                display_board(the_board)
            #choose position
                position = player_choice(the_board)
            #place marker
                place_marker(the_board,player2_marker,position)
            #check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game!')
                    game_on = False
                else:
                    turn = 'Player 1'
 
    
    if not replay():
        break
#Break out of the while loop on replay()