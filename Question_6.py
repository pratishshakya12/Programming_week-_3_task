player1=input("Player 1 Enter your move: ")
player2=input("Player 2 Enter your move: ")

if player1 == player2:
        print("It's a tie!")
else:
     if player1 == 'rock':
        if player2 == 'scissors':
             print("Player 1 wins")
        else:
             print("Player 2 wins")
     else:
        if player1 == 'paper':
            if player2 == 'rock':
                  print("Player 1 wins")
            else:
                  print("Player 2 wins")
        else:
            if player2 == 'paper':
                  print("Player 1 wins")
            else:
                  print("Player 2 wins")