def start_game():
    print("Welcome to the Adventure Game!")
    print("You are in a dark room. There are two doors: left and right.")
    choice = input("Do you want to go left or right? ").lower()

    if choice == "left":
        print("You find a treasure chest! You win!")
    elif choice == "right":
        print("You encounter a monster! Game Over!")
    else:
        print("Invalid choice, try again.")
        start_game()

start_game()
