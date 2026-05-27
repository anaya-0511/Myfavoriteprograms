#adventure
#a program thats takes users on a mini text adventure

#functions
def adventure():
   option1 = input("POV: You wake up in a enchanted forest.. what do you do? 1. save the hurt unicorn or 2. go over to the wishing tree:  ")
   #unicorn route
   if option1 == "save the hurt unicorn":
      palace = input("Congrats you've saved the unicorn! The unicorn tells you to follow it, do you either 1. follow the unicorn or 2. try and find a way out of the forest:  ")
      if palace == "follow the unicorn":
         print("The unicorn takes you to the princess's palace. The princess grants you magical powers!! You use those powers to take you home!")
      else:
         print("You leave the unicorn to try and find a way out, unfortunately there is no way out!! You're stuck here FOREVERRR" )
   #wishing tree route
   elif option1 == "go over to the wishing tree":
      wish = input("You go over to the wishing tree and you see a sign that says 'make a wish' and a some delicious apples. What do you do? 1. make a wish or 2. eat the apples:  ")
      if wish == "make a wish":
         print("Oh wow! Your wish came true!! The wishing tree magically disappered, and now your back home with your wish fulfilled!")
      else:
         print("Turns out the apple was a poisoned apple! You died a slow and painful death :(")
#main
adventure()


