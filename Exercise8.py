while True:
    player1 = input("Player 1: rock, paper or scissors? ")
    player2 = input("Player 2: rock, paper or scissors? ")

    if player1 == player2:
        print("It's a tie!")
    elif (player1 == 'rock' and player2 == 'scissors') or (player1 == 'paper' and player2 == 'rock') or (player1 == 'scissors' and player2 == 'paper'):
        print("Congratulations! Player 1 wins!")
    else:
        print("Congratulations! Player 2 wins!")

    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != 'y':
        break