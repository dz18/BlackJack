import random
from termcolor import colored

class Card:
    def __init__(self, name, value, suit):
        self.name = str(name) + " of " + suit
        self.value = value
        self.suit = suit

class BlackJack():
    limit = 21
    hidden = True
    wallet = 10000
    winnings = 0
    newGame = True
    rounds = 1

    def __init__(self, cards, bet, wallet):
        self.deck = cards
        self.bet = bet
        self.dealersHand = random.sample(self.deck, 1)
        self.removeCardsFromDeck(self.deck, self.dealersHand)
        self.playersHand = [random.sample(self.deck, 2)]
        self.removeCardsFromDeck(self.deck, self.playersHand)
        self.dealersCount = self.count(self.dealersHand)
        self.playersCount = [self.count(self.playersHand[0])]
        self.wallet = wallet

    def removeCardsFromDeck(self, tdeck, removeCards):
        ''''''
        for removeCard in removeCards:
            if removeCard in tdeck:
                tdeck.remove(removeCard)

    def setBet(self, bet):
        self.bet = bet

    def hit(self, hand=0):
        ''''''
        newCard = random.sample(self.deck,1)
        self.playersHand[hand].append(newCard[0])
        self.removeCardsFromDeck(self.deck, newCard)
        self.playersCount[hand] = self.count(self.playersHand[hand])
        
        if len(self.dealersHand) == 1:
            newCard = random.sample(self.deck,1)
            self.dealersHand.append(newCard[0])
            self.removeCardsFromDeck(self.deck, newCard)
            self.dealersCount = self.count(self.dealersHand)

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
        self.dealersHand = random.sample(self.deck, 2)
        self.removeCardsFromDeck(self.deck, self.dealersHand)
        self.playersHand = [random.sample(self.deck, 2)]
        self.removeCardsFromDeck(self.deck, self.playersHand)
        self.rounds = 1
        self.newGame = True
        self.dealersCount = self.count(self.dealersHand)
        self.playersCount = [self.count(self.playersHand)]

    def split(self):
        ''''''
        self.playersHand.append([self.playersHand[0][1]])
        del self.playersHand[0][1]
        self.playersCount.append(self.count(self.playersHand[1]))
        self.playersCount[0] = self.count(self.playersHand[0])

    def printCards(self, hand):
        for card in hand:
            if self.dealersHand == hand and self.hidden == True:
                print(" - " + colored(card.name, 'dark_grey'))
                break
            else:
                print(" - " + colored(card.name, 'dark_grey'))

    def printTable(self):
        print()
        if self.hidden == True:
            print('Dealers Count: ' + colored(self.dealersHand[0].value, 'yellow'))
        else:
            print('Dealers Count: ' + colored(self.dealersCount, 'yellow'))
        self.printCards(self.dealersHand)
        for i,k in enumerate(self.playersHand):
            print(f'Hand {i + 1}: ' + colored(self.playersCount[i], 'yellow'))
            self.printCards(k)

    def printMoveMenu(self):
        print("Press " + colored("1", "light_cyan") + " | Hit")
        print("Press " + colored("2", "light_cyan") + " | Stand")
        print("Press " + colored("3", "light_cyan") + " | Split")
            
    def nextHand(self, hand, playing):
        for i,k in enumerate(playing):
            if i != hand and k == True:
                return i
        return hand
    
    def getResults(self):
        ''''''
        result = {'winnings': self.bet, 'win' : False, 'blackjack': False, 'split': False, 'push' : False,'cardCount': int()}
        hit = True
        if len(self.playersCount) == 1:
            result['cardCount'] = len(self.playersHand[0])
            if self.playersCount[0] > 21:
                print(colored("\nBusted!! You exceeded 21.", "red"))
                result['winnings'] = 0
                return result
            while(self.dealersCount < self.playersCount[0] and self.playersCount[0] <= 21):
                newCard = random.sample(self.deck,1)
                self.dealersHand.append(newCard[0])
                self.removeCardsFromDeck(self.deck, newCard)
                self.dealersCount = self.count(self.dealersHand)
            if self.dealersCount <= 21:
                if self.dealersCount > self.playersCount[0]:
                    print(colored("\nLoser!!", "red"))
                    result['winnings'] = 0
                    return result
                elif self.dealersCount == self.playersCount[0]:
                    print("\nPush!! Returning your bet.")
                    return result
                else:
                    print(colored("\nWinner Winner!!", "light_green"))
                    result['winnings'] *= 1.5
                    result['win'] = True
                    return result
            else:
                result['winnings'] *= 1.5
                result['win'] = True
                print(colored("\nDealer bust!! You win $%.2f" % result['winnings'], 'light_green'))
            return result
        else:
            # Split
            result['split'] = True
            result['cardCount'] = max(len(self.playersHand[0]),len(self.playersHand[1]))
            hit == True
            while(self.dealersCount < self.playersCount[0] and self.dealersCount < self.playersCount[1]):
                newCard = random.sample(self.deck,1)
                self.dealersHand.append(newCard[0])
                self.removeCardsFromDeck(self.deck, newCard)
                self.dealersCount = self.count(self.dealersHand)
            if self.dealersCount <= 21:
                wins, losses, pushes = 0, 0, 0
                for i, k in enumerate(self.playersCount):
                    if k <= 21:
                        wins += 1 if self.dealersCount < self.playersCount[i] else 0
                        losses += 1 if self.dealersCount > self.playersCount[i] else 0
                        pushes += 1 if self.dealersCount == self.playersCount[i] else 0
                    else:
                        losses += 1
                if wins == 2:
                    result['winnings'] = (self.bet * 1.5) * 2
                    result['win'] = True
                    return result
                elif losses == 2:
                    result['winnings'] -= self.bet * 2 
                    return result
                elif pushes == 2:
                    result['winnings'] = self.bet
                    result['push'] = True
                    return result
                elif wins == 1 and losses == 1:
                    result['winnings'] = (self.bet * 1.5) - self.bet
                    return result
                elif wins == 1 and pushes == 1:
                    result['winnings'] = (self.bet * 1.5) + self.bet
                    result['push'] = True
                    return result
                elif losses == 1 and pushes == 1:
                    result['winnings'] = 0
                    result['push'] = True
                    return result
            else:
                # dealer bust
                bustCount = 0
                for i,playerCount in enumerate(self.playersCount):
                    if playerCount > 21:
                        bustCount += 1
                if bustCount == 0:
                    result['winnings'] = (self.bet * 1.5) * 2
                    result['win'] = True
                    return result
                elif bustCount == 1:
                    result['winnings'] = (self.bet * 1.5) - self.bet
                    result['win'] = True
                    return result
                
    def playTerminal(self):
        hand = 0
        playing = [True, False]
        if self.playersCount[0] == 21:
            print(colored('BlackJack!! Instant Winner +$%.2f!!' % (self.bet * 1.5), 'light_green'))
            return {'winnings': self.bet * 1.5, 'win' : True, 'blackjack': True, 'split': False, 'push' : False,'cardCount': 2}
        while True:
            if playing[0] == False and playing[1] == False:
                self.hidden = False
                break
            hand = self.nextHand(hand, playing)
            self.printTable()
            self.printMoveMenu()
            move = True
            while move == True:
                while True:
                    try:
                        inp = int(input(f'>> Hand {hand + 1}: '))
                        break
                    except:
                        print("Invalid input detected.")
                if inp == 1:
                    self.hit(hand)
                    bust = self.validate(self.playersHand[hand])
                    if bust == False:
                        playing[hand] = False
                    if len(self.playersHand) == hand:
                        self.rounds += 1
                    move = False
                elif inp == 2:
                    playing[hand] = False
                    move = False
                elif inp == 3:
                    if len(self.playersHand) == 2:
                        print('Reached Split Max.')
                    elif self.wallet < self.bet:
                        print(f'You need at least ${self.bet} to split.') 
                    elif self.playersHand[0][0].value != self.playersHand[0][1].value or self.rounds != 1:
                        print('Unable to split.')
                    else:
                        self.split()
                        self.printTable() 
                        self.printMoveMenu()
                        playing[1] = True
                        
        
        results = self.getResults()
        self.printTable()
        return results
        
            