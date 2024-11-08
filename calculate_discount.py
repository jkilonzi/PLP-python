def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount."""
    # Calculate the final price based on the discount percentage
    final_price = price - (price * discount_percent)

    # Check if the discount percentage is greater than or equal to 20%
    if discount_percent >= 0.2:
        return final_price  # Return the discounted price
    else:
        return price  # Return the original price if discount is less than 20%

# Get user input
price = float(input("Enter the price in Ksh: "))  # Convert input to float for calculations
discount_percent = float(input("Enter the discount percentage (as a decimal): "))  # Convert input to float

# Call the function and get the final price
final_price = calculate_discount(price, discount_percent)

# Print whether the discount percentage is more than 20% and the final price
print("Is the discount percentage more than 20%?", discount_percent >= 0.2)
print("The final price after discount is:", final_price)

