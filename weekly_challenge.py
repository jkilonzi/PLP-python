def large_power(base, exponent):
    """Check if base raised to the power of exponent is greater than 5000."""
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False

# Ask the user for input
base = float(input("Enter the base: "))  
exponent = float(input("Input the exponent: "))

# Call the function with user input
result = large_power(base, exponent)

# Print the result to standard output
print("Is", base, "raised to the power of", exponent, "greater than 5000?", result)

