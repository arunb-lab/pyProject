# Function Definition
def chk(n: int) -> None:
    """
    Checks if n is even or odd and prints the result.
    """
    if n % 2 == 0:
        print(f"{n} is Even.")
    else:
        print(f"{n} is Odd.")

# --- Main Execution Block ---

if __name__ == "__main__":
    try:
        # Get input
        i = input("Enter an integer: ")
        
        # Convert and check
        num = int(i)
        
        # Call the function
        chk(num)

    except ValueError:
        # Handle non-integer input
        print("Error: Invalid number.")