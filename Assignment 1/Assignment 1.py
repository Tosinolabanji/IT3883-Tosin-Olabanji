# Program Name: Assignment1.py
# Course: IT3883 / Section
# Student Name: Tosin Olabanji
# Assignment Number: Assignment 1
# Due Date: 01/24/2026
# Purpose:
# This program implements a text-based menu that allows the user to
# append data to a buffer, clear the buffer, display the buffer,
# or exit the program.
# Resources Used:
# Class notes, instructor instructions, and personal logic.

# Initialize the input buffer as an empty string
input_buffer = ""

# Loop until the user chooses to exit
while True:
    print("\n--- Text Buffer Menu ---")
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")

    # Get the user's choice
    choice = input("Enter your choice (1-4): ")

    # Option 1: Append data
    if choice == "1":
        user_input = input("Enter text to append: ")
        input_buffer += user_input
        print("Text appended successfully.")

    # Option 2: Clear buffer
    elif choice == "2":
        input_buffer = ""
        print("Input buffer cleared.")

    # Option 3: Display buffer
    elif choice == "3":
        print("Current input buffer:")
        print(input_buffer)

    # Option 4: Exit program
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    # Invalid choice
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
