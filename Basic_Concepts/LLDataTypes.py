''' 
Welcome to PyAdventure Data Types!
To Run this adventure open up the terminal and navigate to this Folder ("Basic_Concepts") by using
the cd command, to run the script and start learning about low level data types in python run "Python3 LLDataTypes.py"
'''

print("Welcome To PyAdventure: Low Level Data Types!")
print("Each File Teaches about different programming concepts \nand should be run individually from one another.")
print("Before We test your Wits in an adventure you will \nHave an opportunity to learn concepts, these can")
print("Be from a nearby sign or anything in the enviroinment \nif you do not pass through a section perfectly")
print("you will be returned to the area before the challenge to \nrefresh your knowlege with the material. \nHave Fun and get Coding!")

def Notes():
    Notes = '''
    You open your notes and find one that catches your eye, 
    the note reads: Low level data types can help users 
    utilize their python skills to make different types of applications.
    
    Python requires the use of a skill called low level data types. Data types are classifications of data 
    that determine the kind of operations that can be performed on them and what values they can take. The art of python
    has several built-in data types that can be used to store and manipulate data.
    
    Python has a data type to represent numbers, called integers. 
    An integer represent a whole number in Python, such as 1, 2, 3, 4, 5, etc. 
    In Python, integers are represented by the 'int' data type.
    
    Python has a data type to represent decimal numbers, called floats.
    A float is a decimal number, such as 1.23, 2.34, 3.45, etc. 
    In Python, floats are represented by the 'float' data type.
    
    Python has a data type to represent a sequence of characters, called strings.
    A string is a sequence of characters, such as "hello", "world", "Python", etc. 
    In Python, strings are represented by the 'str' data type.

    In Python, you don't need to explicitly declare data types when you create a variable. 
    Python automatically infers the data type based on the value assigned to the variable.

    If one wanted to declare a data type for a variable, one can do so by using the syntax:

    variable_name: data_type = value
   
    Examples include:
    
    age: int = 30
    pi: float = 3.14 
    name: str = "John"

    In the command line, type 1 to read the note again, or 2 to continue with your coffee shop adventure.

    '''
    print(Notes)

def BaristaRegister():
    q1 = '''
    You make your way to the register. 
    A friendly barista welcomes you to the coffee shop, asking you what you would like to drink today.
    You proceed to order an iced lavender oat milk latte, your favorite! The barista asks what size latte you would like.
    Oh no! You didn't specify that in your initial order. The barista lists the different size options:
    12 oz, 16 oz, or 20 oz. What data type would represent these different sizes in python?
    
    A) String
    B) Integer
    C) Float
    '''

    print(q1)

    choice = input("Choose by Typing A, B, Or C: ")

    while 1:
        if choice.upper() == "A":
            return 1
        if choice.upper() == "B":
            break
        if choice.upper() == "C":
            return 1
    
    q2 = '''
    Correct! You immediately remember that integers are what refers to whole numbers in Python.
    The barista then asks you for your name to keep track of the order when it's ready.
    You say your 5-letter name and the barista writes it down on the cup. 
    What data type would be used to represent your name?

    A) String
    B) Float
    C) Boolean
    '''

    print(q2)

    choice = input("Choose by Typing A, B, Or C: ")
    while 1:
        if choice.upper() == "A":
            break
        if choice.upper() == "B":
            return 1
        if choice.upper() == "C":
            return 1

    q3 = '''
    Correct! As you finish ordering, the barista tells you that your iced lavender oat milk latte will be $6.56. 
    Luckily, you have enough money to pay for this drink. Your card works and the transaction goes through.
    However, you are worried about coding and how this price can be represented in python.
    How would $6.56 be represented python?
    
    A) Boolean
    B) Array
    C) Float
    '''

    print(q3)

    choice = input("Choose by Typing A, B, Or C: ")   

    while 1:
        if choice.upper() == "A":
            return 1
        if choice.upper() == "B":
            return 1
        if choice.upper() == "C":
            break
    
    q4 = '''
    Correct!, now that you've paid for your drink, you need to thank the barista for taking your order. 
    To communicate your gratitude, type
    
    Thank You!
    
    in the command line
    '''
    print(q4)

    message = input("Enter Your Message Here: ")

    if message != "Thank You!":
        return 1

    q4 = '''
    The barista appreciated your thanks and goes on to make your drink. 
    You sit down at a table and text your friends to meet you here to study together.
    You want their ordering process to go smoother than yours did, 
    so you emphasize being specific with the size of their drink.
    How would you tell them to declare their size of drink in python, if they wanted a 16 oz coffee?
    
    A) size: int = 16
    B) size: bool = False
    C) size: float = 1.6
    '''

    print(q4)

    choice = input("Choose by Typing A, B, Or C: ")   

    while 1:
        if choice.upper() == "A":
            break
        if choice.upper() == "B":
            return 1
        if choice.upper() == "C":
            return 1
    
    outro = '''
    Yay! Your friends got your message! They're on their way.
    After a couple minutes, the drink is ready for you at the pickup counter.
    You take your first sip and sigh in satisfaction, because iced lavender oat milk lattes are your favorite.
    
    Thank you for playing with Low Level Data types. To learn other topics, please look through our system of adventures and chose the topic
    that you would like to learn about next.
    
    Happy Trails :)
    '''
    print(outro)


def main():
    intro = '''
    You are a busy student hoping to study in a comfortable place.
    You find your way to a local coffee shop,
    where people of different backgrounds chat amongst themselves 
    and enjoy their freshly brewed cups of coffee.
    Before you make your way to the register to order, 
    you need to think about how to navigate ordering at this new place.
    You can check your notes for helpful information by entering 1,
    or you can make your way to the register by entering 2 on the command line.
    '''

    print(intro)
    choice = input("Enter 1 or 2 Here: ")
    
    while 1:
        if choice.upper() == "1":
            Notes()

        if choice.upper() == "2":
            break

        else:
           choice = input("Enter 1 or 2 Here: ") 
    
    while 1: 
        D = BaristaRegister()
        if D == 1:
            print("You messed up your order! Before you try again, take a look at your notes.")
            Notes()
        else:
            break

main()