# Get user input and convert to float
initial_value = float(input("Enter a number: "))

# Calculate budget allocations
wants = initial_value * 0.30
needs = initial_value * 0.50
savings = initial_value * 0.20

# Print results with formatted decimal places
print(f"Wants: {wants:.2f}")
print(f"Needs: {needs:.2f}")
print(f"Savings: {savings:.2f}")
