def multiply_numbers(a: float, b: float) -> float:
    """This function returns the multiplication of two numbers

    Args:
        a (float): first number
        b (float): second number

    Returns:
        float: multiplication of two numbers
    """
    return a * b


if __name__ == "__main__":
    print("MULTIPLICATION OF TWO NUMBERS (INTEGER OR DECIMAL)")
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print("result: ", multiply_numbers(a, b))
