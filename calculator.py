"""Small calculator for the Git pull request practice."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    print("=== SUPER CALCULATOR ===")
    print("8 + 2 =", add(8, 2))
    print("8 - 2 =", subtract(8, 2))
    print("8 * 2 =", multiply(8, 2))
    print("8 / 2 =", divide(8, 2))


if __name__ == "__main__":
    main()
