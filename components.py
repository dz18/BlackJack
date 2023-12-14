import random

class Card:
    def __init__(self, name, value, suit):
        self.name = str(name) + " of " + suit
        self.value = value
        self.suit = suit

class BlackJack():
    limit = 21
    rounds = 1
    wallet = 10000
    winnings = 0
    newGame = True
    split = list()

    def __init__(self, cards, bet):
        self.deck = cards
        self.bet = bet
        self.dealersHand = random.sample(self.deck, 1)
        self.removeCardsFromDeck(self.deck, self.dealersHand)
        self.playersHand = random.sample(self.deck, 2)
        self.removeCardsFromDeck(self.deck, self.playersHand)
        self.dealersCount = self.count(self.dealersHand)
        self.playersCount = self.count(self.playersHand)

    def removeCardsFromDeck(self, tdeck, removeCards):
        ''''''
        for removeCard in removeCards:
            if removeCard in tdeck:
                tdeck.remove(removeCard)

    def setBet(self, bet):
        self.bet = bet

    def stay(self):
        '''''' 
        while(self.dealersCount < self.playersCount):
            newCard = random.sample(self.deck,1)
            self.dealersHand.append(newCard[0])
            self.removeCardsFromDeck(self.deck, newCard)
            self.dealersCount = self.count(self.dealersHand)
            
        if self.dealersCount > 21:
            return True
        elif self.dealersCount == self.playersCount:
            return None
        else:
            return False


    def hit(self):
        ''''''
        newCard = random.sample(self.deck,1)
        self.playersHand.append(newCard[0])
        self.removeCardsFromDeck(self.deck, newCard)
        self.playersCount = self.count(self.playersHand)
        
        if self.rounds == 1:
            newCard = random.sample(self.deck,1)
            self.dealersHand.append(newCard[0])
            self.removeCardsFromDeck(self.deck, newCard)
            self.dealersCount = self.count(self.dealersHand)
        self.rounds += 1

    def validate(self, hand):
        handSum = 0
        for card in hand:
            handSum += card.value
        if handSum > 21:
            return False
        return True
    
    def count(self, deck):
        c = 0
        num_aces = 0
        for card in deck:
            if card.value == 1:
                num_aces += 1
            else:
                c += card.value

        for i in range(num_aces):
            if c + 11 <= 21:
                c += 11
            else:
                c += 1

        return c

    def reset(self):
        ''''''
        suits = ['hearts', 'diamonds', 'spades', 'clubs']
        courts = ['king', 'queen', 'jester']
        self.deck = list()
        for value in range(1,14):
            for suit in suits:
                if value == 1:
                    self.deck.append(Card('Ace',value, suit))
                elif value > 10:
                    self.deck.append(Card(courts[11 - value],10, suit))
                else:
                    self.deck.append(Card(value,value,suit))
        self.dealersHand = random.sample(self.deck, 1)
        self.removeCardsFromDeck(self.deck, self.dealersHand)
        self.playersHand = random.sample(self.deck, 2)
        self.removeCardsFromDeck(self.deck, self.playersHand)
        self.rounds = 1
        self.newGame = True
        self.dealersCount = self.count(self.dealersHand)
        self.playersCount = self.count(self.playersHand)

    def split(self):
        ''''''
        print(self.playersHand)
        print(self.playersHand[0], self.playersHand[1])

    def printCards(self, hand):
        for card in hand:
            print(" - " + card.name)

    def playTerminal(self):
        while(True):
            print("Dealers Count :", self.dealersCount)
            self.printCards(self.dealersHand)
            print("Your Card Count :", self.playersCount)
            self.printCards(self.playersHand)
            if self.playersCount == 21 and self.rounds == 1:
                amountWon = self.bet * (1.5)
                print("BlackJack!! You win $" + "{:.2f}".format(amountWon))
                return amountWon
            else:
                print()
                print("1 | Hit")
                print("2 | Stand")
                inp = int(input(" >> "))
                print()
                if inp == 1:
                    self.hit()
                elif inp == 2:
                    result = self.stay()
                    if result == True:
                        amountWon = float(self.bet) * 1.5
                        print("Dealers Count :", self.dealersCount)
                        self.printCards(self.dealersHand)
                        print("Your Card Count :", self.playersCount)
                        self.printCards(self.playersHand)
                        print("Winner Winner!! You win $" + "{:.2f}".format(amountWon))
                        return amountWon
                    elif result == False:
                        print("Dealers Count :", self.dealersCount)
                        self.printCards(self.dealersHand)
                        print("Your Card Count :", self.playersCount)
                        self.printCards(self.playersHand)
                        print("Loser Loser!!")
                        return 0
                    else:
                        print("Dealers Count :", self.dealersCount)
                        self.printCards(self.dealersHand)
                        print("Your Card Count :", self.playersCount)
                        self.printCards(self.playersHand)
                        print("Push. We go again.")
                        print()
                        bet = self.bet
                        self.reset()
                        self.bet = bet
                        self.newGame = False
                if self.count(self.playersHand) > 21:
                    print("You lose! Exceeded 21.")
                    print("Your Card Count :", self.playersCount)
                    self.printCards(self.playersHand)
                    return 0 

