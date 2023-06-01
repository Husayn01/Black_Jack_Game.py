from dealCard import dealCard
from calculateScore import calculateScore
from compare import compare
import pyfiglet

blackJackArt = pyfiglet.figlet_format("BlackJack Game")
print(blackJackArt)

def playGame():
    userCards = []
    computerCards = []
    isGameOver = False

    for _ in range(2):
        userCards.append(dealCard())
        computerCards.append(dealCard())

    while not isGameOver:
        userScore = calculateScore(userCards)
        computerScore = calculateScore(computerCards)
        print("----------------------------------------")
        print(f"Your cards: {userCards}. Current score: {userScore}")
        print("----------------------------------------")
        print(f"Computer's first score: {computerCards[0]}")
        print("----------------------------------------")

        if userScore == 0 or computerScore == 0 or userScore > 21:
            isGameOver = True
        else:
            userShouldDeal = input("Type 'y' to get another card or 'n' to pass: ").lower()
            if userShouldDeal == "y":
                userCards.append(dealCard())
            else:
                isGameOver = True
                print("Exited Blackjack Game successfully")

    while computerScore != 0 and computerScore < 17:
        computerCards.append(dealCard())
        computerScore = calculateScore(computerCards)
    print("----------------------------------------")
    print(compare(userScore, computerScore))
    print("----------------------------------------")
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("----------------------------------------")
    playGame()
