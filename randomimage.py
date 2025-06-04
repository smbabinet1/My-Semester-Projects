#2/21
#Scarlett Babinet
#Random Movie Suggestion

#Init
import random
from PIL import Image
import requests
from io import BytesIO
import time
images=["https://tinyurl.com/movierecommendation1",#Titanic Image Source: IMDB movie ratings. https://www.imdb.com/title/tt0120338/?ref_=ls_i_1 © 1990-2025 by IMDb.com, Inc.
        "https://tinyurl.com/movierecommendation2", #The Dark Knight Image Source: IMDB movie ratings. https://www.imdb.com/title/tt0468569/ © 1990-2025 by IMDb.com, Inc.
        "https://tinyurl.com/movierecommendation3", #Avatar Image Source: IMDB movie ratings. https://www.imdb.com/title/tt0499549/ © 1990-2025 by IMDb.com, Inc.
        "https://tinyurl.com/movierecommendation4", #Toy Story 3 Image Source: IMDB movie ratings. https://www.imdb.com/title/tt0435761/ © 1990-2025 by IMDb.com, Inc.
        "https://tinyurl.com/movierecommendation5" #Cars Image Source: Disney.https://movies.disney.com/cars © 2025 Disney and its related entities
        ]
#Functions
def open_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()
def moviegenerator():
    global url
    global images
    print("Welcome to the Random Movie Recommendation Generator!")
    while True:
        ans = input("Would you like a recommendation?")
        if ans == "yes":
            time.sleep(2)
            print("Generating a Movie...")
            time.sleep(2)
            print("....")
            time.sleep(2)
            print(".....")
            time.sleep(2)
            url = images[random.randint(0,4)]
            open_image(url)
            if url == "https://tinyurl.com/movierecommendation1":
                print("""This Movie is Titanic. A poor artist and a rich debutante meet and fall in
love on the famously ill-fated maiden voyage of the 'unsinkable' Titanic.""")
            elif url == "https://tinyurl.com/movierecommendation2":
                print("""This Movie is The Dark Knight. A superhero movie of Batman putting an end to
havoc wreaked by the Joker.""")
            elif url == "https://tinyurl.com/movierecommendation3":
                print("""This Movie is Avatar. This is the story of a Marine dispatched to the moon
Pandora on a mission who becomes torn between following his orders and protecting
the world he feels is his home.""")
            elif url == "https://tinyurl.com/movierecommendation4":
                print("""This Movie is Toy Story 3. Toys are mistakenly delivered to a day-care
center instead of the attic right before Andy leaves for college, and it's
up to Woody to convince the other toys that they weren't abandoned and to
return home.""")
            else:
                print("""This Movie is Cars. Race car Lightning McQueen is living life
in the fast lane until he hits a detour on his way to the most important race of
his life. Stranded in Radiator Springs, a forgotten town on the old Route 66, he
meets Sally, Mater, Doc Hudson and a variety of quirky characters who help him
discover that there's more to life than trophies and fame.""")
        else:
            break
#Main

moviegenerator()


