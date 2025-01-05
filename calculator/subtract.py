def subtract_numbers(a: float, b: float) -> float:
    """This function returns the subtraction of two numbers

    Args:
        a (float): first number
        b (float): second number

    Returns:
        float: subtraction of the two numbers
    """
    return a - b


if __name__ == "__main__":
    print("SUBTRACTION OF TWO NUMBERS (INTEGER OR DECIMAL)")
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print("result: ", subtract_numbers(a, b))
