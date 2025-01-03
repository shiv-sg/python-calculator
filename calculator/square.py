def square_number(a: float) -> float:
    """This function returns the square of a number

    Args:
        a (float): number

    Returns:
        float: square of a number
    """
    return a * a


if __name__ == "__main__":
    print("SQUARE OF NUMBER (INTEGER OR DECIMAL)")
    a = float(input("Enter the number: "))
    print("result: ", square_number(a))
