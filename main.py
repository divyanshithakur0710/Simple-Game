from sps import play_game

def main():
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Play Stone Paper Scissors")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            print("Game End")
            break
        else:
            print("Wrong choice")


main()