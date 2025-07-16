#the slot machine game
# Author: hajar1010
# Description:A fun terminal-based slot machine game written in Python. The player starts with a balance, places bets, spins the reels, and wins coins based on symbol matches.
import random

print("************************************************ ")
print("🎰 Welcome to the Slot Machine Game!")
balance = float(input("how much money they want to start with : "))

# Define Symbols
symbols = ["🍒", "🍋", "🔔", "🍉", "⭐", "💎"]

while balance > 0:
    bet = float(input("how much you want to bet : "))

    if bet > balance:
        print("You cannot bet more than your current balance!")
        continue

    balance -= bet  # Subtract the bet before spinning

    print("\nYour current balance is: $", round(balance, 2))
    print("************************************************ ")
    print("the machine is spinning .... ")

    # Spin the machine
    chosen = random.choices(symbols, k=3)

    # Print the 3 chosen symbols
    print("Here are the 3 chosen symbols : \n ", " | ".join(chosen))

    # Check for matches
    if chosen[0] == chosen[1] == chosen[2]:
        win = bet * 5
        balance += win
        print("BINGOOO you got the jackpot !! , you got bet *5 !")
    elif chosen[0] == chosen[1] or chosen[0] == chosen[2] or chosen[1] == chosen[2]:
        win = bet * 2
        balance += win
        print("GOOD you got 2 matches !! , you got bet *2 !")
    else:
        print("OH OHH 0 matches !!")

    print("Your updated balance is: $", round(balance, 2))

    # Check if player can continue
    if balance <= 0:
        print("You're out of money. Game over! 💀")
        break

    response = input("wanna play again buddy?? (yes/no) ").lower()
    if response == "yes":
        print("yeaah suure !\n")
        continue
    else:
        print("alright !!")
        break

