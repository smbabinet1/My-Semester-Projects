#Scarlett Babinet
#2/12
#Word Counter

#Init
import string
#Functions
def wordcount(text):
    x= " "
    y= " "
    z= string.punctuation
    myTable=str.maketrans(x,y,z)
    text = (text.translate(myTable))
    x = text.split()
    y = len(x)
    print(x)
    return y

#Main
wordcount("Hello, my name. is Scarlett!")
