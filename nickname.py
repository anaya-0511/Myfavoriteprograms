#nickname
#a program thats generates a mythical creature

#functions
def nickname():
    option1 = input("Are you a either 1. Night owl or 2. Morning bird(input example: Night owl):  ")
    #night owl route
    if option1 == "Night owl":
        season = input("Fall or Winter?(all lowercase):  ")
        if season == "fall":
            activity = input("Choose an activity: 1. trick or treating or 2. hike in the forest(all lowercase, no numbers):  ")
            if activity == "hike in the forest":
                print("Your mythical creature is Bigfoot!")
            else:
                print("Your mythical creature is a Vampire!")
        else:
            activity = input("Choose an activity: 1. sledding or 2. baking christmas cookies(all lowercase, no numbers):  ")
            if activity == "sledding":
                print("Your mythical creature is a Yeti!")
            else:
                print("Your mythical creature is an Elf!")

    #night owl route
    elif option1 == "Morning bird":
        season = input("Summer or Spring?(all lowercase):  ")
        if season == "summer":
            activity = input("Choose an activity: 1. Painting or 2. Swimming(all lowercase, no numbers):  ")
            if activity == "Paintng":
                print("Your mythical creature is an Unicorn!")
            else:
                print("Your mythical creature is a Mermaid")
        else:
            activity = input("Choose an activity: 1. stroll in the garden or 2. play with animals(all lowercase, no numbers):  ")
            if activity == "stroll in the garden":
                print("Your mythical creature is a Garden Gnome!")
            else:
                print("Your mythical creature is a Forest Fairy!")
#main
nickname()




