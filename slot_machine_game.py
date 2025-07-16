#the slot machine game
# Author: hajar1010
# Description:A fun terminal-based slot machine game written in Python. The player starts with a balance, places bets, spins the reels, and wins coins based on symbol matches.
import random
#Ask the player how much money they want to start with
print("************************************************ ")
print("🎰 Welcome to the Slot Machine Game!")
balance=float(input("how much money they want to start with : "))
#Let them bet a certain amount each round (must be ≤ their balance)
bet=float(input("how much you want to bet : "))
while bet<=balance:
#Define Symbols
    balance -= bet
    print("\nYour current balance is: $", balance)
    symbols =["🍒", "🍋", "🔔", "🍉", "⭐", "💎"]
#Use random.choices() to select 3 symbols per spin
    list=random.choices(symbols ,k=3)
# Spin the Machine
    print("************************************************ ")
    print("the machine is spinning .... ")

#Print the 3 chosen symbols as the slot output
    print("Here are the 3 chosen symbols : \n ", "| ".join(list))
#Check Win/Lose
    if list[0]==list[1]==list[2]:
        winnings= bet*5
        print("BINGOOO you got the jackpot !! , you got bet *5 !")
    elif list[0]==list[1]  or list[0]== list[2] or list[2]==list[1]:
        winnings= bet*2
        print("GOOD you got 2 matches !! , you got bet *2 !")
    else:
        winnings=0
        print("OH OHH 0 matches !! " )

    if balance <= 0:
        print("You're out of money. Game over! 💀")
        break
    balance += winnings
    print("Your updated balance is: $", balance)
    response = input("wanna play again buddy?? (yes/no)")
    if response == "yes":
        print("yeaah suure !")
        continue
    else :
        print("alright Thanks for playing!!!")
        break
else :
    print("You're out of money. Game over! 💀")
