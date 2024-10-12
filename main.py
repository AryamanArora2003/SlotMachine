# this is my python slot machine

#import the random module
import random


def spin():
    symbolList = ["🍒", "🍇", "🎂", "🍑", "🥥"]

    resultList = []

    #select 3 random symbols to display as output for spin
    for i in range(3):
        resultList.append(random.choice(symbolList))
    return resultList

def print_row(row):
    #prints each symbol from row list using .join operator, list symbols seperated by "x"
    print("\n**********")
    print(" | ".join(row))
    print("**********\n")


def payout(row,betAmount):
    #if bet wins return payout based on symbol
    if row[0]==row[1] == row[2]:
        if row[0] == "🍒":
            return betAmount*2
        elif row[0] =="🍇":
            return betAmount * 3
        elif row[0] =="🎂":
            return betAmount * 5
        elif row[0] =="🍑":
            return betAmount * 10
        elif row[0] =="🥥":
            return betAmount * 20

    #if bet does not win return no payout
    return 0


def chargeFee(coinBalance,betAmount):
    fee = betAmount
    while True:
        if coinBalance < fee:

            #if coinBalance is less than betting fee allow user option to add more funds or end program
            print("Insufficient funds would you like to add more Money Y/N")
            while True:
                response = str(input()).lower()
                if response == "y":
                    try:
                        addedFunds = int(float(input("Please enter how much you would like to add: $")))
                        print(f"You have added: ${addedFunds}")
                        print(f"You have now bet ${fee}")
                    except ValueError:
                        print("That is not a valid amount. Please enter a valid number.")
                    coinBalance += addedFunds
                    coinBalance -= fee
                    break

                #if no more funds are added end the slot machine program
                elif response == "n":
                    print("You have not entered anymore funds to play with. Program closing")
                    exit()
                else:
                    print ("Invalid input, please try again")
            break

        #if funds are sufficient subtract fee and update coinBalance
        else:
            coinBalance -= fee
            break
    print(f"Current Balance is: ${coinBalance}")

    #return the coinBalance to main after subtracting bet fee
    return coinBalance


def main():

    #use While loop for whole main function allow user to quit or keep plaing

    while True:

        print("******************************************")
        print("Python Slots 3000")
        print("🍒= 2x Multiplier\n🍇 3x Multiplier\n🎂5x Multiplier\n🍑10x Multiplier\n🥥20x Multiplier")
        print("******************************************")

        #while loop to get inital coin balance
        while True:

            try:
                coinBalance= int(float(input("Enter Coins! \nHow much would you like to gamble: $")))
                break
            except ValueError:
                print("That is not a valid amount. Please enter a valid number.")

        while coinBalance > -1:
            print(f"Current Balance is: ${coinBalance}")

            while True:
                betAmount = input("How much money would you like to bet? $")
                try:
                    betAmount = int(float(betAmount))
                    if betAmount < 1:
                        print("Minimum bet is $1 please enter a valid amount.")
                    else:
                        break
                    print(f"You have bet ${betAmount}")

                except ValueError:
                    print("That is not a valid amount. Please enter a valid number.")

            #use chargeFee method to subtract bet from coin balance
            coinBalance = chargeFee(coinBalance,betAmount)

            #row is a list value returned by spin method
            row = spin()
            print("spinning...")

            #use print_row method to output spin results to console
            print_row(row)

            #check if player won spin using payout method
            winnings = payout(row,betAmount)

            if winnings > 0:
                print(f"CONGRATS YOU WON\n${winnings}")
            else:
                print("Sorry you did not win please try again")

            #update coin balance based on winnings
            coinBalance += winnings

            #ask player if they want to keep playing if yes break while loop if no end program
            while True:

                contPlay =str(input("Would you like to play again? Y/N: ")).lower()

                if contPlay == "y":
                    break
                elif contPlay == "n":
                    print("Thank you for playing")
                    exit()
                else:
                    print("Invalid input, please try again")


#run main function
main()