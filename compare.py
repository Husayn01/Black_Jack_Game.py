def compare(userScore, computerScore):
    if userScore == computerScore:
        return "Draw"
        print("----------------------------------------")
    elif computerScore == 0:
        return "You lost! Opponent has a blackjack"
        print("----------------------------------------")
    elif userScore == 0:
        return "Win with a blackjack"
        print("----------------------------------------")
    elif userScore > 21:
        return "You went over. You lose!"
        print("----------------------------------------")
    elif computerScore > 21:
        return "Opponent went over. You win!"
        print("----------------------------------------")
    elif userScore > computerScore:
        return "You win!"
        print("----------------------------------------")
    else:
        return "You lose!"
        print("----------------------------------------")