# Balcalc

Balcalc is a simple command-line budget allocation calculator. It helps you divide your budget into "Wants", "Needs", and "Savings" using default or custom percentages.

## Usage

1. Run the program:
    ```sh
    python balcalc.py
    ```
2. Choose to calculate allocations or exit.
3. Enter your total budget amount.
4. Choose to use default allocations (Wants: 20%, Needs: 70%, Savings: 10%) or enter your own percentages (must total 100%).
5. View the calculated allocations.

## Example

```
=== Balcalc: Budget Allocation Calculator ===
1. Calculate budget allocations
2. Exit
Select an option (1-2): 1

Enter your total budget amount: 1000

Default allocations:
  Wants:   20%
  Needs:   70%
  Savings: 10%

Use default allocations? (Y/n): n
Enter your custom allocation percentages (must total 100%).
  Wants (%): 30
  Needs (%): 60
  Savings (%): 10

--- Allocation Results ---
Wants:   300.00
Needs:   600.00
Savings: 100.00
```

## Requirements

- Python 3.x
