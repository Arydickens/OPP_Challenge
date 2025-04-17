
from pet import Pet


def main():
    pet_name = input("What is your pet's name? ")
    pet = Pet(pet_name)

    while True:
        print("\n--- Menu ---")
        print("1. Eat")
        print("2. Sleep")
        print("3. Play")
        print("4. Get Status")
        print("5. Train")
        print("6. Show Tricks")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            pet.eat()
        elif choice == "2":
            pet.sleep()
        elif choice == "3":
            pet.play()
        elif choice == "4":
            pet.get_status()
        elif choice == "5":
            trick = input("Enter a trick for your pet to learn: ")
            pet.train(trick)
        elif choice == "6":
            pet.show_tricks()
        elif choice == "7":
            print(f"Goodbye! {pet.name} will miss you!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    print("Welcome to this week's Python challenge! 🎉...")
    main()
    print("Challenge ended! Bye....")
