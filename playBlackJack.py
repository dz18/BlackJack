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

root = tk.Tk()


style1 = ("Arial", 14, "bold italic")

selectAccount = tk.Frame(root)
resetAccount = tk.Frame(root)
mainGame = tk.Frame(root)

selectAccount.grid(row=0, column=0, sticky='nsew')
resetAccount.grid(row=0, column=0, sticky='nsew')
mainGame.grid(row=0, column=0, sticky='nsew')

lb1 = tk.Label(selectAccount, text='Select an Account', font=style1)
lb1.pack(pady=20)

lb2 = tk.Label(resetAccount, text='Reset account', font=style1)
lb2.pack(pady=30)

lb3 = tk.Label(mainGame, text='Main game', font=style1)
lb3.pack(pady=50)

account1 = tk.Button(selectAccount, text='Account 1')

selectAccount.tkraise()
root.geometry("1400x900")
root.title('BlackJack')
root.resizable(False,False)
root.mainloop()