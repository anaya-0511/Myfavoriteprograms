#Anaya F
#Madlibs
#a fun and interactive game that allows users to input words and generate a nonsensical story
import random
#Functions
def madlibs():
    print("Welcome to mad libs!")
    name1 = input("Please input a name or input (random) if you don't know: ")
    if name1 == "random":
        name1 = ["Peter","Anna","Harry","Isabella","Charlie","Jessica"]
        name1 = random.choice(name1)
    place1 = input("Please input a place or input (random) if you don't know: ")
    if place1 == "random":
        place1 = ["Asgard","Hogwarts","Mars","Atlantis","The Emerald City","Narnia"]
        place1 = random.choice(place1)
    item1 = input("Please input an item or input (random) if you don't know: ")
    if item1 == "random":
        item1 = ["cat","book","macbook","can of pineapples","turtle","baby"]
        item1 = random.choice(item1)
    emotion = input("Please input an emotion or input (random) if you don't know: ")
    if emotion == "random":
        emotion = ["scared","baffled","alarmed","excited","irritated","disgusted"]
        emotion = random.choice(emotion)
    name2 = input("Please input another name or input (random) if you don't know: ")
    if name2 == "random":
        name2 = ["Pumpkin","Glep","Pim","Lucy","Bartholomew","Bunny"]
        name2 = random.choice(name2)
    nameof_famousperson = input("Please input the name of a famous person or input (random) if you don't know: ")
    if nameof_famousperson == "random":
        nameof_famousperson = ["Kim Kardashian","Elijiah Wood","Michael B. Jordan","Ryan Gosling","Beyonce","Emma Stone"]
        nameof_famousperson = random.choice(nameof_famousperson)
    place2 = input("Please input another place or input (random) if you don't know: ")
    if place2 == "random":
        place2 = ["London","Kenya","Japan","Portugal","Brazil","Chicago"]
        place2 = random.choice(place2)







    print(f"""On a dark and stormy night \033[1m{name1.upper()}\033[0m got teleported to the magical
          dimension of \033[1m{place1.upper()}\033[0m where they found a \033[1m{item1.upper()}\033[0m.
          \033[1m{name1.upper()}\033[0m was very \033[1m{emotion.upper()}\033[0m and then the \033[1m{item1.upper()}\033[0m said "Hello!
          My name is \033[1m{name2.upper()}\033[0m and I need your help.
          I need help getting to my owner \033[1m{nameof_famousperson.upper()}\033[0m will you help me?”
           \033[1m{name1.upper()}\033[0m then says sure and they go on a magical quest through \033[1m{place1.upper()}\033[0m.
          In the end \033[1m{name2.upper()}\033[0m gets returned to \033[1m{nameof_famousperson.upper()}\033[0m and \033[1m{name1.upper()}\033[0m gets teleported home to \033[1m{place2.upper()}\033[0m. """)
madlibs()
