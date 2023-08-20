import random
import time

class Player:
    def __init__(self, hand, money, play, stand):
        self.hand = []
        self.money = 1000
        self.stand = False
        self.play = True
    
    def cardchoice(self, deck):
        self.hand.append(deck.pop(random.randint(0, len(deck) - 1)))


def printnum(lst, name):
    time.sleep(.5)
    print("")
    time.sleep(.5)
    print(f"{name} Cards: ", end="")
    for x in lst:
        print(f"{x} ", end="")
    print("")
    time.sleep(.5)
    print(f"{name} Score: {sum(lst)}")


def cardchoice(lst, lst2, size):
    lst.append(lst2.pop(random.randint(0, size - 1)))


money = 1000
stand = False
play = True

cards = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

dealer = []
player = []

while play:
    while sum(player) <= 21 and not stand:
        time.sleep(.5)
        bet = int(input("Insert bet amount: "))
        while bet > money:
            bet = int(input(f"You only have ${money}. Choose a lower amount to bet: "))
        money -= bet

        cardchoice(dealer, cards, len(cards))

        cardchoice(player, cards, len(cards))
        cardchoice(player, cards, len(cards))

        printnum(dealer, "Dealer")
        #cardchoice(dealer, cards, len(cards)) # Dealer takes two from the start but doesnt reveal the second one 
        printnum(player, "Player")

        while sum(player) <= 21:
            choice = input("Hit, Stand, or Double?: ").lower()

            if choice == "hit":
                cardchoice(player, cards, len(cards))
                printnum(dealer, "Dealer")
                printnum(player, "Player")
            elif choice == "stand":
                stand = True
                break
            elif choice == "double":
                if money < bet: 
                    print(f"You only have ${money}. Choose a different option")
                    continue
                money -= bet
                bet *= 2
                cardchoice(player, cards, len(cards))
                printnum(dealer, "Dealer")
                printnum(player, "Player")
                break
            else:
                print("INVALID CHOICE")
                continue

    if sum(player) > 21:
        print("BUST!")
        bet = 0

    # Dealer Draw
    while sum(dealer) < 15 and bet > 0 or 21 - sum(dealer) > 21 - sum(player) and bet > 0:
        cardchoice(dealer, cards, len(cards))
        printnum(dealer, "Dealer")
        printnum(player, "Player")

    # WINNER STATUS
    if sum(dealer) > 21 and bet > 0:
        print("")
        time.sleep(.5)
        print("DEALER BUST!")
        time.sleep(.5)
        print(f"Earnings made: {bet}")
        money += (bet * 2)
        bet = 0
    elif 21 - sum(dealer) < 21 - sum(player) and bet > 0:
        print("")
        time.sleep(.5)
        print("Dealer Wins!")
        bet = 0
    elif 21 - sum(dealer) > 21 - sum(player) and bet > 0:
        print("")
        time.sleep(.5)
        print("Player Wins!")
        time.sleep(.5)
        print(f"Earnings made: {bet}")
        money += (bet * 2)
        bet = 0
    else:
        print("ITS A DRAW!")
        money += bet
        bet = 0
    
    time.sleep(.5)
    print(f"Remaining Money: {money}")
    time.sleep(.5)

    while True:
        choice = input("Play again?: ").lower()
        if choice == "yes" and money >= 50:
            stand = False
            cards = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
            dealer = []
            player = []
            break
        elif choice == "no":
            time.sleep(.5)
            print(f"Final Money: {money}")
            play = False
            break
        elif money < 50:
            print("Not enough money")
            print(f"Final Money: {money}")
            play = False
            break
        else:
            print("INVALID CHOICE! Enter yes or no")

