import os.path
from wizcoin import WizCoin, WizCoinException

class BankAccount:
    def __init__(self, account_holder, start=WizCoin(0, 0, 0)):
        self._name = str(account_holder)
        self._balance = start
        if f"{account_holder}book.txt" in os.listdir('accounts'):
            with open(f'accounts/{account_holder}book.txt', 'r+') as file:
                for line in file:
                    pass
                last_line = line
                booked_balance = last_line[len('Balance: WizCoin('):-2].split(', ')
                booked_balance = [int(i) for i in booked_balance]
                self._balance = WizCoin(*booked_balance)
        else:
            with open('accounts/' + self._name + 'book.txt', 'w') as ledgerFile:
                ledgerFile.write(f'This account belongs to {self._name}\n-----------------------------\nbalance: {str(self._balance.__repr__())}\n')


    def deposit(self, amount):

        if not isinstance(amount, WizCoin):
            raise WizCoinException("Only currency accepted is WizCoin")
        if amount.galleons < 0 or amount.sickles < 0 or amount.knuts < 0 or amount.total <= 0:
            raise WizCoinException('Only positive number of WizCoins can be deposited') # deposit cannot be negative
        
        #self._balance = (self._balance + amount).change_to_galleons()
        self._balance = WizCoin(0,0,self._balance.total + amount.total)
        self._balance.change_to_galleons()

        with open('accounts/' + self._name + 'book.txt', 'a') as ledgerFile:
            ledgerFile.write("-----------------------------\nDeposit: " + str(amount) + '\n')
            ledgerFile.write('Balance: ' + str(self._balance.__repr__()) + '\n')

    def withdraw(self, amount):

        if not isinstance(amount, WizCoin):
            raise WizCoinException("Only currency accepted is WizCoin")
        if amount.galleons < 0 or amount.sickles < 0 or amount.knuts < 0 or amount.total <= 0:
            raise WizCoinException('Only positive number of WizCoins can be withdrawn')
        if self._balance.total < amount.total:
            return 'Not enough WizCoins'

        self._balance = WizCoin(0,0,self._balance.total + amount.total)
        self._balance.change_to_galleons()

        with open('accounts/' + self._name + 'book.txt', 'a') as ledgerFile:
            ledgerFile.write("-----------------------------\nWithdraw: " + str(amount) + '\n')
            ledgerFile.write('Balance: ' + str(self._balance.__repr__()) + '\n')

    @property
    def balance(self):
        return self._balance


acct = BankAccount('Alice')
acct.deposit(WizCoin(100, 100, 100))
acct.withdraw(WizCoin(0, 0, 71))
acct.balance


