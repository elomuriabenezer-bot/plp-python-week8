"""A small menu-driven toolkit with a guessing game, to-do list, and calculator."""

import random


def play_guessing_game():
    """Run a number guessing game until the player finds the secret number."""
    secret_number = random.randint(1, 10)
    print("I'm thinking of a number from 1 to 10.")

    while True:
        guess_text = input("Your guess (or q to quit this game): ").strip()
        if guess_text.lower() == "q":
            print(f"The number was {secret_number}.")
            break

        if not guess_text.isdigit():
            print("Please enter a whole number from 1 to 10.")
            continue

        guess = int(guess_text)
        if guess < secret_number:
            print("Too low. Try again!")
        elif guess > secret_number:
            print("Too high. Try again!")
        else:
            print(f"You got it! The number was {secret_number}.")
            break


def manage_todo_list(tasks):
    """Let the user add, view, or remove tasks in a changing list."""
    while True:
        print("\nTo-Do List: add / view / remove / back")
        action = input("Choose an action: ").strip().lower()

        if action == "add":
            task = input("Task to add: ").strip()
            if task:
                tasks.append(task)
                print(f"Added: {task}")
            else:
                print("A task cannot be empty.")

        elif action == "view":
            if tasks:
                print("Your tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
            else:
                print("Your to-do list is empty.")

        elif action == "remove":
            task = input("Task to remove: ").strip()
            if task in tasks:
                tasks.remove(task)
                print(f"Removed: {task}")
            else:
                print("That task is not on your list.")

        elif action == "back":
            break

        else:
            print("Choose add, view, remove, or back.")


def run_calculator():
    """Calculate the result of one basic arithmetic operation."""
    try:
        first_number = float(input("Enter the first number: "))
        operator = input("Choose +, -, *, or /: ").strip()
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        if second_number == 0:
            print("You cannot divide by zero.")
            return
        result = first_number / second_number
    else:
        print("Please choose +, -, *, or /.")
        return

    print(f"{first_number:g} {operator} {second_number:g} = {result:g}")


def main():
    """Show the main menu until the user chooses to quit."""
    tasks = []
    print("Welcome to your Personal Mini-Toolkit!")

    while True:
        print("\nChoose a tool:")
        print("1. Number Guessing Game")
        print("2. To-Do List")
        print("3. Simple Calculator")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            play_guessing_game()
        elif choice == "2":
            manage_todo_list(tasks)
        elif choice == "3":
            run_calculator()
        elif choice == "4":
            print("Thanks for using your Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print("Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
