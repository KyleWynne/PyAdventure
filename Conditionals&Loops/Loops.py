import random


def GuideBook():
    guidebook = """
    Welcome to the Loops Adventure!

    In this adventure, you will learn about two important looping constructs in Python: for loops and while loops.

    A for loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects. It allows you to execute a block of code repeatedly for each item in the sequence.

    Here's the basic syntax of a for loop:

    for item in sequence:
        # Code to be executed for each item

    The variable "item" takes on the value of each item in the sequence one by one, and the code inside the loop is executed for each iteration.

    On the other hand, a while loop repeatedly executes a block of code as long as a certain condition is true. It is useful when you don't know in advance how many times the code needs to be repeated.

    Here's the basic syntax of a while loop:

    while condition:
        # Code to be executed while the condition is true

    The condition is typically a comparison or logical expression that evaluates to either True or False.

    During the adventure, you will encounter challenges where you'll need to use both for and while loops to overcome obstacles.

    Good luck and have fun!

    Press Enter to continue...
    """
    input(guidebook)


def Challenge1():
    print("Challenge 1: The Mysterious Cave\n")
    print("You find yourself standing in front of a mysterious cave.")
    print("Legend has it that great treasures lie deep inside the cave.")
    print(
        "To enter the cave, you need to find the correct code that unlocks the entrance."
    )

    # generate a random number between 1 and 10
    code = random.randint(1, 10)

    guess = int(input("Enter a number between 1 and 10: "))

    while guess != code:
        print("Wrong code! Try again.")
        guess = int(input("Enter a number between 1 and 10: "))

    print(
        "Congratulations! You have unlocked the cave entrance and found the hidden treasures."
    )


def Challenge2():
    print("Challenge 2: The Magical Fountain\n")
    print(
        "You come across a magical fountain that grants a wish to anyone who drinks from it."
    )
    print(
        "To drink from the fountain, you must correctly answer a series of questions."
    )

    questions = [
        {"question": "What is the capital city of France?", "answer": "Paris"},
        {"question": "How many planets are there in the solar system?", "answer": "8"},
        {"question": "What is the largest mammal on Earth?", "answer": "Blue whale"},
    ]

    num_questions = len(questions)
    score = 0

    for question in questions:
        print("\n" + question["question"])
        answer = input("Your answer: ")

        if answer.lower() == question["answer"].lower():
            print("Correct answer! You're one step closer to making your wish.")
            score += 1
        else:
            print("Wrong answer! Keep trying.")

    if score == num_questions:
        print("\nCongratulations! You have answered all the questions correctly.")
        print("The magical fountain grants your wish!")
    else:
        print(
            "\nYou didn't answer all the questions correctly. Keep exploring and try again."
        )
        Challenge2()


def main():
    GuideBook()

    while True:
        print("\nChoose a challenge:")
        print("1. The Mysterious Cave")
        print("2. The Magical Fountain")
        print("3. Quit")

        choice = input("Enter the number of the challenge you want to try: ")

        if choice == "1":
            Challenge1()
        elif choice == "2":
            Challenge2()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for playing the While Loop Adventure!")


if __name__ == "__main__":
    main()
