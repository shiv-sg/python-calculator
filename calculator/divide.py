def divide_numbers(numerator: float, denominator: float) -> float:
    """This function returns the division of two numbers

    Args:
        a (float): first number
        b (float): second number

    Returns:
        float: division of two numbers
    """
    if denominator == 0:
        raise ValueError("Invalid input. Division by zero is not allowed.")
    return numerator / denominator


if __name__ == "__main__":
    print("DIVISION OF TWO NUMBERS (INTEGER OR DECIMAL)")
    numerator = float(input("Enter the first number: "))
    denominator = float(input("Enter the second number: "))
    print("result: ", divide_numbers(numerator, denominator))
