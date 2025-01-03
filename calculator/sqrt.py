import math

def sqrt_number(a: float) -> float:
    """This function returns the square root of a number

    Args:
        a (float): number

    Returns:
        float: square root of a number
    """
    return math.sqrt(a)

if __name__ == "__main__":
    print("SQUARE ROOT OF NUMBER (INTEGER OR DECIMAL)")
    a = float(input("Enter the number: "))
    print("result: ", sqrt_number(a))
