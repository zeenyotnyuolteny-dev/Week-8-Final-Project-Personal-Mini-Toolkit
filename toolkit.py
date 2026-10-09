
# Personal Mini-Toolkit — Week 8 Final Project

# Store tasks that the user adds during the program.
tasks = []


# Tool 1: Calculate two numbers using a chosen operation.
def calculator():
    print("\n--- Simple Calculator ---")

    try:
        num1 = float(input("Enter the first number: "))
        operation = input("Choose +, -, *, or /: ")
        num2 = float(input("Enter the second number: "))

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Sorry, you cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please try again.")
            return

        print(f"Your answer is: {result}")

    except ValueError:
        print("Please enter valid numbers.")


# Tool 2: Add, view, and remove tasks from a changing list.
def todo_list():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            task = input("Enter your task: ").strip()
            if task:
                tasks.append(task)
                print(f"Task added: {task}")
            else:
                print("Please enter a task.")

        elif choice == "2":
            if tasks:
                print("Your tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
            else:
                print("Your to-do list is empty.")

        elif choice == "3":
            if tasks:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
                try:
                    number = int(input("Enter the task number to remove: "))
                    if 1 <= number <= len(tasks):
                        removed = tasks.pop(number - 1)
                        print(f"Removed task: {removed}")
                    else:
                        print("That task number does not exist.")
                except ValueError:
                    print("Please enter a valid task number.")
            else:
                print("There are no tasks to remove.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")


# Tool 3: Check whether a number is even or odd.
def even_odd_checker():
    print("\n--- Even or Odd Checker ---")

    try:
        number = int(input("Enter a whole number: "))

        if number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")

    except ValueError:
        print("Please enter a whole number.")


# Main menu: repeat until the user chooses to quit.
def main():
    print("Welcome to My Personal Mini-Toolkit!")

    while True:
        print("\n===== MAIN MENU =====")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Even or Odd Checker")
        print("4. Quit")

        choice = input("Choose a tool (1-4): ").strip()

        if choice == "1":
            calculator()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            even_odd_checker()
        elif choice == "4":
            print("Thank you for using my toolkit. Goodbye!")
            break
        else:
            print(f"'{choice}' is not a valid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
