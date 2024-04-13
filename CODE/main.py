from db import *
from member import * 
from trainer import * 
from admin import *

def main_menu():
    """Display the main menu and handle user input."""
    while True:
        print("\nHealth and Fitness Club Management System")
        print("1. Member System")
        print("2. Trainer System")
        print("3. Administrative System")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            memmber_menu()
        elif choice == "2":
            trainer_menu()
        elif choice == "3":
            administrative_ui()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def memmber_menu():
    """Display the member menu and handle user input."""
    while True:
        print("\nMember System")
        print("1. Register Member")
        print("2. Update Member Details")
        print("3. Delete Member")
        print("4. Member Details")
        print("5. Book Session")
        print("6. Pay Payment")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_member_ui()
        elif choice == "2":
            update_member_ui()
        elif choice == "3":
            delete_member_ui()
        elif choice == "4":
            check_member_ui()
        elif choice == "5":
            book_class_ui()
        elif choice == "6":
            payment_ui()
        elif choice == "7":
            main_menu()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def trainer_menu():
    """Display the trainer menu and handle user input."""
    while True:
        print("\nTrainer System")
        print("1. Set Trainer Availability")
        print("2. Search Member")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            set_trainer_availability_ui()
        elif choice == "2":
            search_member_ui()
        elif choice == "3":
            main_menu()
        else:
            print("Invalid choice. Please enter a number between 1 and 2.")

if __name__ == "__main__":
    main_menu()

