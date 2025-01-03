def add_numbers(a: float, b: float) -> float:
    """This function returns the sum of two numbers

    Args:
        a (float): first integer
        b (float): second integer

    Returns:
        float: sum of the two numbers
    """
    return a + b

if __name__ == "__main__":
    print("SUM OF TWO NUMBERS (INTEGER OR DECIMAL)")
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print("result: ", add_numbers(a, b))
