from components import Card, BlackJack
import json
from termcolor import colored, cprint

suits = ['hearts', 'diamonds', 'spades', 'clubs']
courts = ['king', 'queen', 'jester']
placeholder = 'Enter index # or letter'

cards = list()
for value in range(1,14):
    for suit in suits:
        if value == 1:
            cards.append(Card('Ace',value, suit))
        elif value > 10:
            cards.append(Card(courts[11 - value],10, suit))
        else:
            cards.append(Card(value,value,suit))

def loadData():
    ''''''
    with open("BlackJackData.json") as f:
        data = json.load(f)
    return data 

def saveData(dataBase):
    ''''''
    with open("BlackJackData.json", "w") as f:
        json.dump(dataBase, f, indent=4) 

def resetData(database, userID):
    ''''''
    for i,k in enumerate(database):
        if userID == k["id"]:
            k['username'] = None
            k['wallet'] = 10000
            for keys, items in k['achievements'].items():
                items['earned'] = False

    with open("BlackJackData.json", "w") as f:
        json.dump(database, f, indent=4)

def checkAchievements(userData, splitWins, winStreak, winnings, CardCountWin, plays ):
    # checkAchievements(userdata, [Split, Win], winStreak, winnings, [Win, CardCount], plays)
    for k,v in userData['achievements'].items():
        if v['earned'] == True:
            pass
        elif k == 'Lucky Streak' and winStreak == 5: 
            ''' Win five hands in a row without busting or going over 21 '''
            v['earned'] = True
            print(f'Acievement Unlocked: {k}!!')
        elif k == 'Split Personalilty' and splitWins[0] == True and splitWins[1] == True:
            ''' Successfully split a pair of cards and win both hands '''
            v['earned'] = True
            print(f'Acievement Unlocked: {k}!!')
        elif k == 'Five-Card Charlie' and CardCountWin[0] == True and CardCountWin[1] >= 5:
            ''' Win a hand with a five-card total without busting '''
            v['earned'] = True
            print(f'Acievement Unlocked: {k}!!')
        elif k == 'Marathon' and plays == 100:
            ''' Play 100 consecutive hands without leaving the table '''
            v['earned'] = True
            print(f'Acievement Unlocked: {k}!!')
        elif k == 'BlackJack Tycoon' and userData['wallet'] == 1000000:
            ''' Accumulate a total chip count of one million in your wallet '''
            v['earned'] = True
            print(f'Acievement Unlocked: {k}!!')
        elif k == 'Crescendo Conquest' and winnings == 1000000:
            ''' Accumulate a total chip count of one million in one sitting '''
            v['earned'] = True
            print(f'Acievement Unlocked: {k}!!')

def postGameMenu():
    print('Press ' + colored('Y', 'light_cyan') + ' | Play Again')
    print('Press ' + colored('Q', 'light_cyan') + ' | Quit')
    print('Press ' + colored('A', 'light_cyan') + ' | Achievements')
    print('======================')

def printAchievements(userData):
    unlocked = list()
    locked = list()
    for name,desc in user['achievements'].items():
        if desc['earned'] == True:
            unlocked.append([name, desc])
        else:
            locked.append([name,desc])

    print()
    if len(unlocked) != 0:
        
        print(colored('~ UNLOCKED ~','blue'))  
        for desc in unlocked:
            print(' - ' + colored(desc[0], 'yellow') + ' : ' + (desc[1]['description']))
    if len(locked) != 0:
        print(colored('~ LOCKED ~','blue'))
        for desc in locked:
            print(' - ' + colored(desc[0], 'yellow') + ' : ' + desc[1]['description'])
    print()

game = True
db = loadData()

while True:
    # Print save files
    print(colored("\n~ Chose Account ~", "blue"))
    for i,k in enumerate(db):
        if k["username"] == None:
            print(f"Press " + colored(i + 1, "light_cyan") + " | <Empty>")
        else:
            print(f"Press " + colored(i + 1, "light_cyan") + " | " + k['username'])
            print( "         - Wallet: $%.2f" % (k['wallet']))
    print('============================')
    print("Press " + colored("Q", "light_cyan") + " | Quit")
    print("Press " + colored("R", "light_cyan") + " | Reset Account")
    
    # Validate input
    try:
        inp = input(" >> ")
        if inp.isnumeric():
            inp = int(inp)
            if inp - 1 < 0 or inp - 1 >= len(db):
                print("Input is out of range.")
                game = False
            else:
                break
        elif isinstance(inp, str):
            if inp.upper() == 'Q':
                print("Exiting program.")
                game = False
                break
            elif inp.upper() == 'R':
                print(colored("\n~ Select Account to reset ~", "blue"))
                for i,k in enumerate(db):
                    if k["username"] == None:
                        pass
                    else:
                        print("Press " + colored(i + 1, 'light_cyan') + " | " + k['username'])
                        print(f" - Wallet: {k['wallet']}")
                try:
                    inp = int(input(" >> "))
                    if inp - 1 < 0 or inp - 1 >= len(db):
                        print("Input is out of range. Try again")
                    else:
                        user = db[inp - 1]
                        resetData(db, user["id"])
                except:
                    print("Try again")
            else:
                print("Invalid Input")
    except:
        print("Invalid input.")
        game = False

if game != False:
    user = db[inp - 1]
    if user["username"] == None:
        newName = str(input("Set Username: "))
        user["username"] = newName
    winnings = 0
    bet = 0
    winStreak = 0
    plays = 0

# Start game if user has money
while (game == True) and (user["wallet"] >= 5):
    # User places a bet
    while bet == 0:
        print("\n" + colored('Winnings Today: ',"yellow"), end='')
        if winnings < 0:
            print(colored('$' + str(winnings), 'red'))
        else:
            print(colored('$' + str(winnings), 'light_green'))
        print(colored("Wallet: ", "yellow") + colored("$%.2f" % user['wallet'], 'light_green'))
        try:
            inp = int(input(colored("Place bet: $", "light_green")))
            if inp >= 5 and inp <= user["wallet"]:
                user["wallet"] -= inp
                winnings -= inp
                bet = inp
            elif inp < 5:
                print("The table minimum is $5")
            else:
                print("Your dont have that much money to bet.")
        except:
            print("Invalid Input. Try Again")

    # Game begins - BlackJack(Cards, Bet, wallet)
    result = BlackJack(cards, bet, user['wallet'])
    bet = 0
    print()
    result = result.playTerminal() # {'winnings': int(), 'win' : bool(), 'blackjack': bool(), 'split': bool(), 'push': bool(), 'cardCount':cardCount()}
    user["wallet"] += result['winnings']
    winnings += result['winnings']
    winStreak = winStreak + 1 if result['win'] == True else 0

    print("\n" + colored("Winnings Today: ", 'yellow'), end='')
    if winnings < 0:
        print(colored('$' + str(winnings), 'red'))
    else:
        print(colored('$' + str(winnings), 'light_green'))
    print(colored('Wallet: ', 'yellow') + colored('$%.2f' % user['wallet'],'light_green'))

    if user["wallet"] < 5:
        colored("Sorry, you dont have enough money to play.", "red")
        break
    
    # Ask user if they want to play again
    checkAchievements(user, [result['split'],result['win']], winStreak, winnings, [result['win'], result['cardCount']], plays)
    decision = True
    while decision:
        try:
            postGameMenu()
            inp = str(input('>> '))
            if inp.upper()== 'Q':
                print("Thank you for playing!")
                decision = False
            elif inp.upper() == 'Y':
                print("We Play again!")
                decision = False
            elif inp.upper() == 'A':
                printAchievements(user)
            else:
                pass
        except:
            pass

    if inp.upper() == 'Q':
        break

saveData(db)





    


    
    
    

            
