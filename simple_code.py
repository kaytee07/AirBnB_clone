def greet(name):
    """Print a greeting message."""
    print(f"Hello, {name}!")


def calculate_sum(a, b):
    """Calculate the sum of two numbers."""
    return a + b


def main():
    """Main function."""
    greet("Alice")
    result = calculate_sum(3, 7)
    print("The sum is:", result)


if __name__ == '__main__':
    main()
