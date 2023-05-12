''' 
Welcome to PyAdventure!
To Run this adventure open up the terminal and navigate to this Folder ("Basic_Concepts") by using
the cd command, to run the script and start learning about python run "Python3 Introduction.py"
'''

print("Welcome To PyAdventure!")
print("Each File Teaches about different programming concepts \nand should be run individually from one another.")
print("Before We test your Wits in an adventure you will \nHave an opportunity to learn concepts, these can")
print("Be from a nearby sign or anything in the enviroinment \nif you do not pass through a section perfectly")
print("you will be returned to the area before the challenge to \nrefresh your knowlege with the material. \nHave Fun and get Coding!")

def GuideBook1():
    GuideBook1 = '''
    You open your old guidebook and turn the pages over till you find a section that
    catches your eye, The Section Reads: "The ancient Art of python can be used to cast
    Spells and Help you achieve death defying feats when faced with a tricky situation.
    When facing an enemy in battle you will have to cast a python spell by typing it. 
    When faced with a difficult situation you will have to answer a multiple choice question."
    
    The art of python requires the use of a skill called "syntax" this is a precise skill
    where the typed answer must follow a set of guidelines such that the machine can undertsand them
    each programming language has their own syntax and different commands for achieving the same result.
    
    When running code in python any lines that are not a comment will be run. A comment denoted 
    by the # sybol means that everything on that line will not be run but is instead used for
    programmers to communicate what the lines around it do and how they fit into the program
    commenting all over code is good style. 
    
    Style refers to the way code is presented, anything that does not affect how the code is run
    but is implemented for readability of your code falls under style and not syntax. Good style 
    includes seperating big programs into seperate files, commenting on code for others to understand
    sperating functions and code blocks with lines and giving variables descriptive names
    
    Lastly our first spell (function) we can learn is called print()
    
    print() outputs whatever is in quotes out to the command line and is extremely useful for debugging
    and creating command line interfaces
    
    Ex: print("Hello World") would output:
    Hello World
    '''
    print(GuideBook1)

def WitchesHut():
    q1 = '''
    As you enter the dark and cold hut you feel the door start to shut behind you but by the time you notice
    the door has already shut as you heart cackling comging from the other side of the room. A Hideous Witch appears
    infront of you as a trap door opens beneath you. You need to think fast but you cant remeber the term for making
    your code easy to follow and read for others is it:
    A) Syntax
    B) Comment
    C) Style
    '''

    print(q1)

    choice = input("Choose by Typing A, B, Or C: ")

    while 1:
        if choice == "A":
            return 1
        if choice == "B":
            return 1
        if choice == "C":
            break
    
    q2 = '''
    Correct! You immediately remember that style is what refers to how code is written and grab the edge of the trap door
    to pull yourself up. While you attempt to summon the strength to pull yourself up you star thinking and cant remember
    what symbol is used to declare a comment. Was it:
    A) #
    B) &
    C) //
    '''

    print(q2)

    choice = input("Choose by Typing A, B, Or C: ")
    while 1:
        if choice == "A":
            break
        if choice == "B":
            return 1
        if choice == "C":
            return 1

    q3 = '''
    Correct! As you pull youself up and get to your feet you see the witch start casting a spell as the spell flies 
    at you, you must think of what the term is for precisely following a set of guidelines when coding, Was it:
    A) Style
    B) Comment
    C) Syntax
    '''

    print(q3)

    choice = input("Choose by Typing A, B, Or C: ")   

    while 1:
        if choice == "A":
            return 1
        if choice == "B":
            return 1
        if choice == "C":
            break
    
    q4 = '''
    Correct!, now that you are in Striking Distance you need to cast a spell that would print
    
    Begone Witch
    
    in the command line
    '''
    print(q4)

    spell = input("Enter Your Spell Here:")

    if spell != "print(\"Begone Witch\")":
        return 1
    
    outro = '''
    The Witch after being hit with your powerful spell goes flying and curses you swearing that she will be
    back. After your first encounter with the witch you take a sigh of relief and prepare for your next 
    adventure. 
    
    Thank you for playing the introduction please look through our system of adventures and chose the topic
    that you would like to learn about next.
    
    Happy Trails :)
    '''
    print(outro)


def main():
    intro = '''
    You awake in a strage but bustling town where a sense of adventure fills the air
    as you grab you sachel you rember to bring your guidebook in case you get lost.
    As you set foot out of the city you become excited about the possibilities your 
    journey could bring. After a few hours of walking you find yourself near a rickity
    abandoned looking hut. Before you set foot into this hut you take a second to 
    think about your options. You can check your guidebook for helpful information
    by entering 1 or you can enter the hut by entering 2 on the command line
    '''

    print(intro)
    choice = input("Enter 1 or 2 Here:")
    
    while 1:
        if choice == "1":
            GuideBook1()

        if choice == "2":
            break

        else:
           choice = input("Enter 1 or 2 Here:") 
    
    while 1: 
        D = WitchesHut()
        if D == 1:
            print("You Died, Before you jump back in take a look at the guidebook")
            GuideBook1()
        else:
            break

main()