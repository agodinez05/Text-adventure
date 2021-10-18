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

    if answer=="1":
        #call game_over() function with the "reason" argument
        game_over("no bro, what?! you can't take a griever. You're done.")
    elif answer=="2":
        #lead player to The Glade
        the_glade()

#the glade
def the_glade():
    #some prompts
    print("You have escaped the griever and are now at the Glade")
    print("Continue forward and look for the door")
    print("Where will you go now?")
    print("1.Right 2. Forward")

    #take input()
    answer = input(">")

    if answer=="1":
        #the player is dead, call game_over()
        game_over("do you not listen to basic instructions")
    elif answer=="2":
        #player moves on to door
        door()

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
        #player won the game
        print("YAY! ALWAYS TRUST MINHO! HE'S THE BEST")
        print("YOu have escaped the maze! Until next time <3")
        #activate play_again() function
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


def start():
    #give some prompts
    print("It is dark and you are in a rattling box, moving upward. As you approach the light you see a group of people crowding around you. You see the maze. Tall walls of rock.")
    print("Now you must lead the group to safety but be careful of the grievers, flesh eating robots.")
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

#start the game
start()





       


