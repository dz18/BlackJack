from components import Card, BlackJack
import json

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
    for k,v in userData['achievements'].items():
        if v['earned'] == True:
            pass
        elif k == 'Lucky Streak' and winStreak == 5: 
            ''' Win five hands in a row without busting or going over 21 '''
            v['earned'] = True
            print(f'Acievement Unlocked "{k}"!!')
        elif k == 'Split Personalilty' and splitWins == True:
            ''' Successfully split a pair of cards and win both hands '''
            v['earned'] = True
            print(f'Acievement Unlocked "{k}"!!')
        elif k == 'Five-Card Charlie' and CardCountWin == True:
            ''' Win a hand with a five-card total without busting '''
            v['earned'] = True
            print(f'Acievement Unlocked "{k}"!!')
        elif k == 'Marathon' and plays == 100:
            ''' Play 100 consecutive hands without leaving the table '''
            v['earned'] = True
            print(f'Acievement Unlocked "{k}"!!')
        elif k == 'BlackJack Tycoon' and userData['wallet'] == 1000000:
            ''' Accumulate a total chip count of one million in your wallet '''
            v['earned'] = True
            print(f'Acievement Unlocked "{k}"!!')
        elif k == 'Crescendo Conquest' and winnings == 1000000:
            ''' Accumulate a total chip count of one million in one sitting '''
            v['earned'] = True
            print(f'Acievement Unlocked "{k}"!!')

game = True
db = loadData()

while True:
    # Print save files
    print("\n~ Chose Account ~")
    for i,k in enumerate(db):
        if k["username"] == None:
            print(f"{i + 1} | <Empty>")
        else:
            print(f"{i + 1} | {k['username']}")
            print(f"   - Wallet: ${k['wallet']}")
    print("==|=================")
    print("Q | Quit")
    print("R | Reset Account\n")
    
    # Validate input
    try:
        inp = input("Enter index # or letter: ")
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
                print("\n~ Select Account to reset ~")
                for i,k in enumerate(db):
                    if k["username"] == None:
                        pass
                    else:
                        print(f"{i + 1} | {k['username']}")
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
        print(f"\nWinnings Today: ${winnings}")
        print(f"Wallet: ${user['wallet']}")
        try:
            inp = int(input("Place bet: $"))
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
    
    print(f"\nWinnings Today: ${winnings}")
    print(f"Wallet: ${user['wallet']}")

    if user["wallet"] < 5:
        print("Sorry, you dont have enough money to play.")
        break
    
    # Ask user if they want to play again
    checkAchievements(user,False, winStreak, winnings, False, plays)
    decision = True
    while decision:
        try:
            inp = str(input("Play Again? (Y/N): "))
            if inp.upper() == 'N':
                print("Thank you for playing!")
                decision = False
            elif inp.upper() == 'Y':
                print("We Play again!")
                decision = False
            else:
                pass
        except:
            pass

    if inp.upper() == 'N':
        break

saveData(db)





    


    
    
    

            
