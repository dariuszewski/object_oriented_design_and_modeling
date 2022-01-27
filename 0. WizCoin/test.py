from operator import indexOf
import os

from wizcoin import WizCoin

l = os.listdir('accounts')

with open('accounts/Alicebook.txt', 'r+') as file:
    for line in file:
        pass
    last_line = line
    booked_balance = last_line[len('Balance: WizCoin('):-2].split(', ')
    booked_balance = [int(i) for i in booked_balance]
    print(booked_balance)

n = WizCoin(*booked_balance)