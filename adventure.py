#Athenea Godinez + Cecilia Wilson 
#Maze Runner Program
#Data.PYT
#Have fun!
def start():
    #Data script
    import Data
    print(Data.start())
    print(Data.attack())
    #give some prompts
    print("Now you must lead the group to safety but be careful of the grievers, flesh eating robots. AND USE THE NUMBER FOR YOUR ANSWER, DONT WRITE IT!")
    print("Which way will you turn first? Right or Left?")
    
    #convert the player's input() to lower_case
    answer = input(">").lower()

    if "r" in answer:
        #if player typed "right" or "r" lead him to griever_one()
        griever_one()
    elif "l" in answer:
        #else if player typed "left" or "l" lead him to griever_two()
        griever_two()
    else:
        #else call game_over() function with the "reason" argument
        game_over("don't you know how to type something properly?")
        
#griever one
def griever_one():
    #give some prompts
    print("You turn right and run into a griever. Oh no! What will you do?")
    print("1. Duck 2. Run away 3. Fight it")

    #take input()
    answer = input(">")

    if answer=="1":
        #the player is dead
        game_over("The griever killed you and everyone else, good job :/ loser!")
    elif answer=="2" or "3":
        #lead to The Glade
        print("You got lucky! Now run to the Glade")
        the_glade()
    else:
       #else call game_over() function with the "reason" argument
        game_over("don't you know how to type something properly?")

#griever two
def griever_two():
    #give some prompts
    print("You now have run into a huge griever. You only have one way of getting away. What will you do?")
    print("1. Fight it 2. Run away")

    #take input()
    answer = input(">")

    if answer=="1" or "fight it":
        #call game_over() function with the "reason" argument
        game_over("no bro, what?! you can't take a griever. You're done.")
    elif answer=="2" or "run away":
        #lead player to The Glade
        the_glade()

#the glade
def the_center():
    #some prompts
    print("You have escaped the griever and are now at the center of the maze.")
    print("Continue forward and look for the door")
    print("Where will you go now?")
    print("1.Right 2. Forward")

    #take input()
    answer = input(">")

    if answer=="1":
        #the player is dead, call game_over()
        game_over("do you not listen to basic instructions")
    elif answer=="2":
        #player moves on to searching for the code/key
        searching_for_key()

#searching for the key/code for escape
def searching_for_key():
    #some prompts
    print("You are so close now but you need to find the key/code.")
    print("To find the key you need to do some simple math")
    print("What is 2+4")

    #take input()
    answer = input(">")

    if answer=="6":
        #the player moves on to the door()
        door()
    else:
        #player is dead
        game_over("you need to go back to lower school with those math skills.")

    #second part of key - prompts
    print ("Uh oh, you need one more number.")
    print ("What is 5x5?")

    #take input()
    answer = input(">")

    if answer=="25":
        #the player moves on to the door()
        door()
    else:
        #player is dead
        game_over("you need to go back to lower school with those math skills.")
    

#the door/freedom
def door():
    #some prompts
    print("Wow! You have made it to the door, the last thing standing between you and freedom. But you need a code to open it. You don't have the code, who do you ask for it?")
    print("Be careful to not ask the snake")
    print("1. Teresa 2. Newt 3. Minho")

    #take input()
    answer = input(">")

    if answer=="1":
        #player is dead/wrong choice, call game_over()
        game_over("NO! WRONG! Never trust her >:/")
    elif answer=="2":
        #player is dead/wrong choice, call game_over()
        game_over("Wrong! He's awesome so I understand but no")
    elif answer=="3":
        #player escaped maze
        print("YAY! ALWAYS TRUST MINHO! HE'S THE BEST")
        print("You have escaped the maze!")
        #activate last_scene() function
        last_scene()

#past the door/last scene
def last_scene():
    #some prompts
    print("You are in the griever HQ")
    print("You and the group are walking through a dark hallway and you reach a door. You open it and see a screen that's playing a video of a blonde woman. What do you do?")
    print("1. Smash the screen 2. Keep watching")
    
    #take input()
    answer = input(">")

    if answer=="1":
        #player is dead
        game_over("Oh no! The room is on fire, you killed everyone. Good job!")
    if answer=="2":
        #player lives and discovers new information
        print("Oh no! There is DEADLY disease and you are the key to everyone's survival. Be careful out there.")
        print("To be continued...")
        play_again()
    
#game_over function accepts argument called "reason"
def game_over(reason):
    #print the "reason" in line
    print(reason)
    print("GAME OVER!")
    #ask player to play again or not by activating play_again()
    play_again()

#function to ask player if they want to play again or not
def play_again():
    print("Do you want to play again?(y or n)")
    
    #convert the player's input to lower_case
    answer = input(">").lower()

    if "y" in answer:
        #if player typed "yes" or "y" start game from the beginning
        start()
    else:
        #if player types anything other than "yes" or "y", exit
        exit()


#start the game
start()


