import tkinter as tk
import json

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

def createUser(db, userID):
    if newUsername == None:
        pass
    else:
        for account in db :
            if account['db'] == userID:
                db['username'] == newUsername.g
        

def loadSelectedUser(db, userID):
    user = db[userID]
    if user['username'] == None:
        id = userID
        makeAccount.tkraise()
    else:
        return user

db = loadData()
user = None
id = None

root = tk.Tk()

# Font styling
style1 = ("Arial", 14, "bold italic")
style2 = ("Arial", 14)


# Pages
selectAccount = tk.Frame(root)
resetAccount = tk.Frame(root)
makeAccount = tk.Frame(root)
mainGame = tk.Frame(root)

selectAccount.grid(row=0, column=0, sticky='nsew')
resetAccount.grid(row=0, column=0, sticky='nsew')
makeAccount.grid(row=0, column=0, sticky='nsew')
mainGame.grid(row=0, column=0, sticky='nsew')

# Page Labels
lb1 = tk.Label(selectAccount, text='Select an Account', font=style1)
lb1.pack(pady=20)

lb2 = tk.Label(resetAccount, text='Reset account', font=style1)
lb2.pack(pady=30)

lb3 = tk.Label(makeAccount, text='Make an Account', font=style1)
lb3.pack(pady=50)

lb4 = tk.Label(mainGame, text='Main game', font=style1)
lb4.pack(pady=80)

# Select Account Buttons
account1 = tk.Button(selectAccount, text=f"{db[0]['username']}", command=lambda : loadSelectedUser(db, 0), font=style2, width=20)
account1.pack()
account2 = tk.Button(selectAccount, text=f"{db[1]['username']}", command=lambda : loadSelectedUser(db, 1), font=style2, width=20)
account2.pack()
account3 = tk.Button(selectAccount, text=f"{db[2]['username']}", command=lambda : loadSelectedUser(db, 2), font=style2, width=20)
account3.pack()

# Make Account elements
label = tk.Label(makeAccount, text="Username")
newUsername = tk.Entry(makeAccount).pack()
submit = tk.Button(makeAccount, text='Submit', command= lambda : createUser(db, userID))

# Start game
selectAccount.tkraise()
root.geometry("1400x900")
root.title('BlackJack')
root.resizable(False,False)
root.mainloop()
saveData()