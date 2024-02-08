import time

def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a mysterious forest.")
    print("Your objective is to find the hidden treasure.")
    print("Let's begin!\n")
    time.sleep(1)

def choose_path():
    print("You come across a fork in the road.")
    print("Which path will you take?")
    print("1. Left")
    print("2. Right")
    choice = input("Enter your choice (1 or 2): ")
    while choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        choice = input("Enter your choice (1 or 2): ")
    return choice

def explore_left():
    print("You chose the left path.")
    print("You encounter a wild bear!")
    print("What will you do?")
    print("1. Fight the bear")
    print("2. Run away")
    choice = input("Enter your choice (1 or 2): ")
    while choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        print("You bravely fight the bear...")
        time.sleep(1)
        print("But unfortunately, the bear is too strong.")
        print("You have been defeated.")
        return False
    else:
        print("You wisely choose to run away from the bear.")
        print("You escape and continue your journey.")
        return True

def explore_right():
    print("You chose the right path.")
    print("You find a hidden cave.")
    print("Do you want to enter the cave?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice (1 or 2): ")
    while choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        print("You enter the cave and discover the hidden treasure!")
        print("Congratulations! You win!")
        return True
    else:
        print("You decide not to enter the cave.")
        print("You continue your journey.")
        return True

def main():
    intro()
    path_choice = choose_path()
    if path_choice == '1':
        left_result = explore_left()
        if not left_result:
            print("Game Over!")
            return
    else:
        right_result = explore_right()
        if right_result:
            print("Game Over!")
            return

if __name__ == "__main__":
    main()
