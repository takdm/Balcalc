# Balcalc: A simple budget allocation calculator

def get_float_input(prompt):
    """Prompt the user for a float input with error handling."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_allocation_input(defaults):
    """
    Allow the user to customise allocation percentages or use defaults.
    Returns a tuple: (wants_pct, needs_pct, savings_pct)
    """
    print("\nDefault allocations:")
    print(f"  Wants:   {defaults['wants']*100:.0f}%")
    print(f"  Needs:   {defaults['needs']*100:.0f}%")
    print(f"  Savings: {defaults['savings']*100:.0f}%")
    choice = input("\nUse default allocations? (Y/n): ").strip().lower()
    if choice == 'n':
        print("Enter your custom allocation percentages (must total 100%).")
        while True:
            wants = get_float_input("  Wants (%): ") / 100
            needs = get_float_input("  Needs (%): ") / 100
            savings = get_float_input("  Savings (%): ") / 100
            total = wants + needs + savings
            if abs(total - 1.0) < 1e-6:
                return wants, needs, savings
            else:
                print("Allocations must total 100%. Please try again.")
    else:
        return defaults['wants'], defaults['needs'], defaults['savings']

def main_menu():
    """Main menu for Balcalc."""
    print("=== Balcalc: Budget Allocation Calculator ===")
    print("1. Calculate budget allocations")
    print("2. Exit")
    choice = input("Select an option (1-2): ").strip()
    return choice

def main():
    # Default allocation percentages
    defaults = {'wants': 0.20, 'needs': 0.70, 'savings': 0.10}

    while True:
        choice = main_menu()
        if choice == '1':
            initial_value = get_float_input("\nEnter your total budget amount: ")
            wants_pct, needs_pct, savings_pct = get_allocation_input(defaults)
            wants = initial_value * wants_pct
            needs = initial_value * needs_pct
            savings = initial_value * savings_pct
            print("\n--- Allocation Results ---")
            print(f"Wants:   {wants:.2f}")
            print(f"Needs:   {needs:.2f}")
            print(f"Savings: {savings:.2f}\n")
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please select 1 or 2.")

if __name__ == "__main__":
    main()
