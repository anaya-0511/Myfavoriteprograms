#anaya
#hogwarts
#prompts user to type in their name, the program generates a hogwarts house

#init
import time
import random
#Functions
def house(name):
   if name == "Harry" or name == "Hermione" or name == "Ron":
     return "Gryffindor!"
   elif name == "Newt" or name == "Nymphadora" or name == "Pomona":
      return "Hufflepuff!"
   elif name == "Luna" or name == "Cho" or name == "Filius":
      return "Ravenclaw!"
   elif name == "Draco" or name == "Voldemort" or name == "Severus":
      return "Slytherin!"
   else:
    num = random.randint(1,4)
    if num == 1:
       return "Gyrffindor!"
    elif num == 2:
       return "Hufflepuff!"
    elif num == 3:
       return "Ravenclaw!"
    elif num == 4:
       return "Slytherin!"

def main():
   print("Welcome to Hogwarts!")
   name = input("Please enter your name: ")
   time.sleep(1)
   print("....")
   time.sleep(2)
   print(".......")
   print(house(name))


#main
main()
