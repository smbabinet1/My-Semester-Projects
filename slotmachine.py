#scarlett babinet
#slot machine
#Init
import random
import time
symbols = ["❀" , "✿", "7","❁", "✾","❋","❃","✤","☘", '♥', '♦', '♠', '♣', '☆']
weights = [0.07,0.07,0.0007,0.07,0.07,0.07,0.07,0.07,0.07,0.07,0.07,0.07,0.07,0.07]
#1. Start the player with 100 credits
credit= 100
#Functions
def slotmachine():
    global symbols
    global weights
    global credit
    #1. Introduction
    print("Welcome to The Slot Machine!")
    while True:
    #2. Ask spin or quit
        print("You have " + str(credit) + " credits.")
        x=input("Would you like to spin or quit?")
        if x== "spin" and credit>=0:
            bet=int(input("How much would you like to bet? Your winnings will be multiplied by this."))
            if bet<=credit:
                credit=credit-bet
                print("You have " + str(credit) + " credits.")
        #3. Randomly pull 3 items from your list
        #make sure to store these in a vriable
                credit= credit - bet #2. Every spin costs 1  credits
                outcome1=random.choices(symbols,weights)[0]
                outcome2=random.choices(symbols,weights)[0]
                outcome3=random.choices(symbols,weights)[0]

        #4. Display the three images the outcome
                print(outcome1)
                print("..")
                time.sleep(2)
                print(outcome2)
                print("...")
                time.sleep(2)
                print(outcome3)
        #5. Determine the outcome (if,elif,else)
                if outcome1 == 2 and outcome2 == 2 and outcome3 == 2:
                    credit= credit+100*bet #3. Jackpot = x100 reward
                    print("JACKPOT!!!")
                    print("You have "+ str(credit) + " credits!")
                elif outcome1 == outcome2 and outcome1==outcome3 and outcome2==outcome3:
                    credit = credit+10*bet #4. 3 of a kind = x10 reward
                    print("You win!")
                    print("You have "+ str(credit) + " credits!")
                elif outcome1 == outcome2 or outcome2==outcome3 or outcome1==outcome3:
                    credit = credit+2*bet #4b. 2 of a kind = x2 reward
                    print("You win!")
                    print("You have "+ str(credit) + " credits!")
                else:
                    print("You lose.")
                    print("You have "+ str(credit) + " credits.")
            else:
                print("Sorry, you can not bet more credits than you have!")
                response=int(input("Would you like to 1) Bet Less or 2) Purchase 10 more credits"))
                if response==2:
                    credit=credit+100
        elif x == "spin" and credit <=0: #6. Do not let them play w/ 0 credits
            print("You don't have enough credits to spin! Would you like to purchase 100 more credits?")
            choice=input("yes or no")
            if choice== "yes":
                credit= 100
            else:
                print("You are broke! You cannot continue to play.")
                break
        else:
            break
#Main

slotmachine()



