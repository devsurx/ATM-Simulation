from getpass import getpass
import itertools
import random
from abc import ABC, abstractmethod
import time
import subprocess
from datetime import datetime


class Account:
    __account_number = random.randint(10000000000, 99999999999)
    __holder_name = None
    __account_type = None
    __balance = 0
    __pin = None

    def __init__(self, holder_name, account_type, balance, pin):
        self.__holder_name = holder_name
        self.__account_type = account_type
        self.__balance = balance
        self.__pin = pin

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount
    
    def get_balance(self):
        return self.__balance

    def get_pin(self):
        return self.__pin

    def get_holder_name(self):
        return self.__holder_name

    def get_account_number(self):
        pass

class Card:
    card_number = None
    expiry_date = None
    card_pin = None

    card_number = ""

    for i in range(16):
        card_number += str(random.randint(0, 9))

    
    today = datetime.now()

    def get_card_number(self):
        return self.card_number
    
    def get_card_pin(self):
        return self.card_pin

    def __init__(self, card_pin):
        self.expiry_date = f"{self.today.month:02d}/{self.today.year + 10}"
        self.card_pin = card_pin


    def verify_pin(self, pin):
        pass

    def get_holder_name(self, accountObj):
        return accountObj.get_holder_name()


class Transaction(ABC):
    @abstractmethod
    def process_transaction(self):
        pass

class DepositTransaction(Transaction):
    def process_transaction(self):
        print("Money Deposited")

class WithdrawalTransaction(Transaction):
    def process_transaction(self):
        print("Money Withdrawn")

class BalanceInquiryTransaction(Transaction):
    def process_transaction(self):
        print("Current Balance is ₹1000")


class ATM:
    def __init__(self, account):
        self.account = account

    def authenticate(self, pin, cardObj):

        time.sleep(1)
        # clrscr()

        if pin == cardObj.get_card_pin():
            return 1
        else:
            return 0
        

    def menu(self):
        pass

    def reciept(self):
        pass


def autoAuth(atm, userCard):
    card_pin_input = int(getpass("Enter card PIN: "))
    returnCode = atm.authenticate(card_pin_input, userCard)
    return returnCode

def loading():
    print("\nLoading...\n")

    for i in range(21):
        bar = "█" * i + "░" * (20 - i)
        print(f"\r[{bar}] {i*5}%", end="", flush=True)
        time.sleep(0.08)

    print("\n")

def dispense_cash():
    print("\nPreparing cash...")

    frames = [
        "[          ]",
        "[=         ]",
        "[==        ]",
        "[====      ]",
        "[======    ]",
        "[========  ]",
        "[==========]"
    ]

    for frame in frames:
        print(f"\rCash Slot {frame}", end="", flush=True)
        time.sleep(0.3)

    print("\n\n💵 Cash Dispensed Successfully!")
    print("Please collect your cash.")


def clrscr():
    subprocess.run("cls", shell=True)

def Simulation():
    
    print(r"""
███████╗████████╗███████╗███████╗██╗     
██╔════╝╚══██╔══╝██╔════╝██╔════╝██║     
███████╗   ██║   █████╗  █████╗  ██║     
╚════██║   ██║   ██╔══╝  ██╔══╝  ██║     
███████║   ██║   ███████╗███████╗███████╗
╚══════╝   ╚═╝   ╚══════╝╚══════╝╚══════╝

███╗   ███╗ ██████╗ ██╗   ██╗███╗   ██╗████████╗ █████╗ ██╗███╗   ██╗
████╗ ████║██╔═══██╗██║   ██║████╗  ██║╚══██╔══╝██╔══██╗██║████╗  ██║
██╔████╔██║██║   ██║██║   ██║██╔██╗ ██║   ██║   ███████║██║██╔██╗ ██║
██║╚██╔╝██║██║   ██║██║   ██║██║╚██╗██║   ██║   ██╔══██║██║██║╚██╗██║
██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██║ ╚████║   ██║   ██║  ██║██║██║ ╚████║
╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝

                      「 IMPENETRABLE 」

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        Security before convenience.
        Verification before trust.
        Every operation is authenticated.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
    loading()
    time.sleep(1)
    clrscr()


    print("""
==================================================
             CREATE NEW BANK ACCOUNT
==================================================

Please enter the following details to create
your new bank account.

--------------------------------------------------
1. Account Holder Name
2. Account Type (Savings / Current)
3. Initial Deposit
4. Create a 4-digit PIN
--------------------------------------------------

Let's get started!

==================================================
""")
    holder_name_input = input("Enter account holder name: ")
    account_type_input = input("Enter account type [Savings(S) or Current(C)]: ")
    initial_deposit_input = input("Enter initial deposit: ")
    pin_input = getpass("Enter a 4 digit pin: ")

    user = Account(holder_name_input, account_type_input, int(initial_deposit_input), pin_input)

    clrscr()

    print("""
==================================================
        ACCOUNT CREATED SUCCESSFULLY!
==================================================

Your bank account has been created.

Please keep your Account Number and PIN safe.

Thank you for choosing Python Bank.

==================================================
""")
    
    loading()
    time.sleep(1)
    clrscr()
    

    print("""
==================================================
              CREATE NEW ATM CARD
==================================================

Your account has been created successfully!

Please enter the following details to create
your ATM card.

--------------------------------------------------
1. Create a 4-digit PIN
2. Confirm PIN
--------------------------------------------------

Your card number and expiry date will be
generated automatically.

==================================================
""")
    card_pin_input = int(getpass("Enter card pin: "))
    card_pin_input_confirm = int(getpass("Re-enter card pin to confirm: ")) 

    if card_pin_input == card_pin_input_confirm:
        userCard = Card(card_pin_input_confirm)
    else:
        print("Re-enter the same pin")

    loading()
    clrscr()

    print(f"""
==================================================
         ATM CARD CREATED SUCCESSFULLY!
==================================================

Congratulations, {userCard.get_holder_name(user)}!

Your ATM card has been created successfully.

----------------------------------------------
Card Number : {userCard.card_number}
Expiry Date : {userCard.expiry_date}
----------------------------------------------

Please keep your card and PIN secure.
Do not share your PIN with anyone.

Thank you for choosing Python Bank!

==================================================
""")
    
    loading()
    time.sleep(1)
    clrscr()
    atm = ATM(user)

    print("""
==================================================
              USER AUTHENTICATION
==================================================

Please verify your identity to continue.

Enter the following details:

• ATM Card Number
• 4-Digit PIN

--------------------------------------------------
For your security, you have only 3 attempts to
enter the correct PIN.

==================================================
""")
    
    

    for tries in range(3, -1, -1):    
        returnCode = autoAuth(atm, userCard)
        
        if returnCode == 1:
            break
        else:
            print(f"Wrong data, entered try again\n{tries} tries left")
            continue

    time.sleep(2)
    clrscr()

    stopMenu = False
    while (stopMenu == False):
    
        print(f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                 S T E E L   M O U N T A I N                      ┃  
┃                    「 IMPENETRABLE 」                             ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫

SESSION STATUS    : AUTHENTICATED ✓
ACCESS LEVEL      : CUSTOMER
ACCOUNT HOLDER    : {user.get_holder_name()}
CURRENT BALANCE   : ₹{user.get_balance()}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    [1] Deposit Funds
    [2] Withdraw Funds
    [3] Balance Inquiry
    [4] Exit Secure Session

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

> SELECT OPERATION :
        """)

        choice = int(input(""))
        
        match choice:
            case 1:
                autoAuth(atm, userCard)
                amt = int(input("Enter amount to deposit: "))
                user.deposit(amt)
                
                print(f"""
==================================================
        DEPOSIT COMPLETED SUCCESSFULLY!
==================================================

Amount Deposited : ₹{amt}
Current Balance  : ₹{user.get_balance()}

Your funds have been credited successfully.

Thank you for choosing STEEL MOUNTAIN.

==================================================
""")

                time.sleep(2)
                clrscr()
            
            case 2:
                autoAuth(atm, userCard)
                amt = int(input("Enter amount to withdraw: "))
                if user.get_balance() > amt:
                    user.withdraw(amt)
                    dispense_cash()
                    time.sleep(2)
                    clrscr()

                else:
                    print("Insufficient Balance..")
                    time.sleep(2)
                    clrscr()

            case 3:
                autoAuth(atm, userCard)
                print(f"Current balance: {user.get_balance()}")
                time.sleep(2)
                clrscr()

            case 4:
                stopMenu == True
                print("Exiting...")
                break


# --------------- MAIN PROGRAM ---------------------

if __name__ == "__main__":
    Simulation()