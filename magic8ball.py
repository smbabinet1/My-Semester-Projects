#Scarlett Babinet
#1/27
#Init
import random
import time
magic8list = ["Yes" , "Very Likely" , "Outlook is Good!" , "Absolutely", "Without a Doubt" , "No" , "Why would you ask that, No" , "Absolutely Not", "No way" , "NO!" , "Possibly" , "Perhaps", "It is possible", "I don't know", "Maybe"] #15responses
#Functions
def magic8ball():
    print("Welcome to the Magic 8 Ball! Please ask it a yes or no question!")
    while True:
        question=input("Please ask a yes or no question.")
        x= question.endswith("?")
        if x == True:
            print("shake...")
            time.sleep(2)
            print("shake....")
            time.sleep(2)
            print("shake.....")
            time.sleep(2)
            response=random.randint(0,14)
            print(magic8list[response])
            print("Would you like to ask another question?")
            ans=input("yes/no")
            if ans== "no" or ans == "n":
                break
        else:
            print("ERROR: Please end your question with a '?'")
#Main
magic8ball()
