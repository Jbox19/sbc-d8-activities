from random import randint

print("Input Short Cut Keys to Acces Bank:")
accounts = {}

def create_acc():
    for i in range(1):
            user_id = randint(000000, 1000000)
            bal = int(input("Input Balance: "))
            accounts[user_id] = bal
            print(f"\t\t{accounts}")

def check_bal():
    cb = int(input("Enter User ID to see balance: "))
    if cb in accounts:
         print(f"\t\tYour balance is {accounts[cb]}")

def deposit():
     dep = int(input("Enter User ID to deposit: ")) 
     if dep in accounts:
          depos = int(input("Enter Amount to Deposit: "))
          ds = accounts[dep] + depos
          accounts.update({dep:ds})
          print(f"\t\tYour New balance is {ds}")

def withdraw():
    w = int(input("Enter User ID to withdraw: "))  
    if w in accounts:
         wd = int(input("Enter Amount to Withdraw: ")) 
         wid = accounts[w] - wd
         accounts.update({w:wid})
         print(f"\t\tYou Withdraw {wid}") 

def delete_acc():
    d = int(input("Enter User ID to DELETE ACCOUNT: "))
    if d in accounts:
        accounts.pop(d)
        print(f"\t\tYour Account has been deleted!") 

def existing_acc():
     print(f"\t\tExisiting accounts {accounts.keys()}")

while True:
    ca = input("\nCreate account \t(ca) \nCheck balance \t(cb) \nDeposit \t(d) \nWithdraw \t(w) \nDelete Account \t(da) \nAccounts \t(a) \nQuit \t\t(q): ").lower().replace(" ", "")
    if ca == "ca":
        create_acc()
    elif ca == "cb":
         check_bal()
    elif ca == "d":
         deposit()
    elif ca == "w":
         withdraw()
    elif ca == "da":
         delete_acc()
    elif ca == "a":
         existing_acc()
    elif ca == "q":
        print("Cancel Bank Access")
        break
