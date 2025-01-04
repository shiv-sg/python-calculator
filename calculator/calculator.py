from add import add_numbers
from subtract import subtract_numbers
from multiply import multiply_numbers
from divide import divide_numbers
from square import square_number
from sqrt import sqrt_number


def get_valid_number(prompt: str):
    """Get a valid number from the user input, allowing them to quit.

    Args:
        prompt ([str]): The input prompt to show

    Returns:
        float: the entered number

    Raises:
        SystemExit: If the user enters 'q' or 'Q' to quit
    """
    while True:
        user_input = input(prompt)
        if user_input.lower() == "q":
            print("Quitting...")
            raise SystemExit()
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_valid_operation(prompt: str):
    """Get a valid operation from the user input, allowing them to quit.

    Args:
        prompt ([str]): The input prompt to show

    Returns:
        float: the entered operation
    """
    while True:
        operation = input(prompt)
        if operation in ["1", "2", "3", "4", "5", "6", "q", "Q"]:
            return operation
        else:
            print(
                "Invalid input. Please enter a number between 1 and 6 or enter 'q' or 'Q' to quit."
            )


if __name__ == "__main__":
    while True:
        print("\n")
        print("CALCULATOR")
        print("which operation you want to perform")
        print("1. add")
        print("2. subtract")
        print("3. multiply")
        print("4. divide")
        print("5. square")
        print("6. square root")
        print("q. quit")
        operation = get_valid_operation("enter your choice: ")

        if operation == "1":
            print("ADD OF TWO NUMBERS (INTEGER OR DECIMAL)")
            a = get_valid_number("Enter the first number: ")
            b = get_valid_number("Enter the second number: ")
            print("result: ", add_numbers(a, b))
        elif operation == "2":
            print("SUBTRACT OF TWO NUMBERS (INTEGER OR DECIMAL)")
            a = get_valid_number("Enter the first number: ")
            b = get_valid_number("Enter the second number: ")
            print("result: ", subtract_numbers(a, b))
        elif operation == "3":
            print("MULTIPLY OF TWO NUMBERS (INTEGER OR DECIMAL)")
            a = get_valid_number("Enter the first number: ")
            b = get_valid_number("Enter the second number: ")
            print("result: ", multiply_numbers(a, b))
        elif operation == "4":
            print("DIVIDE OF TWO NUMBERS (INTEGER OR DECIMAL)")
            numerator = get_valid_number("Enter the first number: ")
            denominator = get_valid_number("Enter the second number: ")
            print(
                "result: ", divide_numbers(numerator=numerator, denominator=denominator)
            )
        elif operation == "5":
            print("SQUARE OF NUMBER (INTEGER OR DECIMAL)")
            a = get_valid_number("Enter the number: ")
            print("result: ", square_number(a))
        elif operation == "6":
            print("SQUARE ROOT OF NUMBER (INTEGER OR DECIMAL)")
            a = get_valid_number("Enter the number: ")
            print("result: ", sqrt_number(a))
        elif operation == "q":
            print("Thank you for using the calculator. Goodbye!")
