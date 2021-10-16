def start():
    #give some prompts
    print("It is dark and you are in a rattling box, moving upward. As you approach the light you see a group of people crowding around you. You see the maze. Tall walls of rock.")
    print("Now you must lead the group to safety but be careful of the grievers, flesh eating robots.")

    #convert the player's input() to lower_case
    answer = input(">").lower()
    
    #prompt for player to choose character
    print("Pick your character, choose a letter.")
    print("a.Thomas, b.Newt, c.Minho")
    
    #selection for character
    if "a" in answer:
        print("Hello, Thomas.")
    if "b" in answer:
        print("Hello, Newt")
    if "c" in answer:
        print("Hello Minho")
        
    #selection for partner
    print("Choose your partner")
    print("d.Teresa, e.Chuck, f.Alby, g.Gally")
    
    #selection for partner
    if "d" in answer:
        print("You will lead the group with Teresa")
    if "e" in answer:
        print("You will lead the group with Chuck")
    if "f" in answer:
        print("You will lead the group with Alby")
    if "g" in answer:
        print("You will lead the group with Gally")
        
    #backstory/introduction for game
    print("You are standing in the field waiting for the gates to close for the night. But they don’t. Everyone is beginning to freak out. They seem to be blaming Thomas. You heard the grievers' cries. “We have to do something!” you exclaim. A small group, with you and your partner at the front, go into the maze to look for a way out.")
    print("The Maze Begins!")
  
def first turn():
    #player decides which way to turn
    print("Which way will you turn first? Right or Left?")
    #player chooses how to fight griever
    print("Oh no! You run into a griever. What do you do?")
    print("a.Duck, b.Run away, c.Fight it")
    if "a" in answer:
        print("You're Dead!")
        
#start the game
start()
first turn()


       


