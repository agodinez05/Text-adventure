#Data.PYT
def start():
    #give some prompts
    print("It is dark and you are in a rattling box, moving upward. As you approach the light you see a group of people crowding around you. You see the maze. Tall walls of rock.")
    print("You are in the Glade. Time to get adjusted. What job will you choose? AND USE THE NUMBER FOR YOUR ANSWER, DONT WRITE IT!")
    list=[1,2,3]
   
    #convert the player's input() to lower_case
    answer = input(">").lower()

    #just intro, doesn't matter what player picks
    if answer=="1" or "2" or "3":
        #prompts
        print("Good choice. Let's get started!")
        attack()
    
#Player is running through the forest when they are attacked
def attack():
        #background prompts
    print("You are in the woods shortly after your arrival. One of the other Glade members attacks you. What do you do?")
    list=["1,fight back","2, run"]

    #take input()
    answer = input(">")

    if answer=="1":
        #player dies
        game_over("You can't take this guy. You are too weak and he is crazy. Try again!")
    elif answer=="2":
        #player gets to safety
        print ("Smart idea! Get to the other Gladers and let them know what happened.")
        maze()

