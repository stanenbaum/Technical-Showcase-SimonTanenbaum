# Project Surplus: National Debt Payoff via Realized + Unrealized Capital Gains Tax
# Author: Simon Tanenbaum

import pandas as pd
import matplotlib.pyplot as plt

# Parameters
starting_debt = 34_000_000_000_000  # $34 trillion national debt
years = 30
tax_rate = 0.25  # 25% tax rate on both realized and unrealized gains
annual_interest_rate = 0.02  # Assume 2% debt interest

# Estimated annual gains from millionaires & billionaires
# Realized gains: sold assets, taxed normally
# Unrealized gains: value increase of held assets (e.g., stock value going up)
annual_realized_gains = 3_000_000_000_000  # $3T
annual_unrealized_gains = 4_000_000_000_000  # $4T
total_annual_gains = annual_realized_gains + annual_unrealized_gains

# Storage for tracking
debt_over_time = []
surplus_over_time = []
tax_collected = []

debt = starting_debt
surplus = 0

# Simulation
for year in range(1, years + 1):
    interest = debt * annual_interest_rate
    tax_revenue = total_annual_gains * tax_rate

    # Apply tax revenue to interest + principal
    debt_payment = min(tax_revenue, debt + interest)
    debt = max((debt + interest) - debt_payment, 0)

    # Any excess is recorded as surplus
    if tax_revenue > debt_payment:
        surplus += tax_revenue - debt_payment

    # Log yearly data
    debt_over_time.append(debt)
    surplus_over_time.append(surplus)
    tax_collected.append(tax_revenue)

# Results as DataFrame
df = pd.DataFrame({
    'Year': range(1, years + 1),
    'Debt Remaining': debt_over_time,
    'Capital Gains Tax Collected': tax_collected,
    'Cumulative Surplus': surplus_over_time
})

# Output the table
print(df)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Debt Remaining'], label='Remaining National Debt', linewidth=2)
plt.plot(df['Year'], df['Cumulative Surplus'], label='Cumulative Surplus', linewidth=2, linestyle='--')
plt.title('Project Surplus: Taxing Realized & Unrealized Gains to Eliminate National Debt')
plt.xlabel('Year')
plt.ylabel('USD ($)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


Year	Debt Remaining	Capital Gains Tax Collected	Cumulative Surplus
1	$32.93 trillion	$1.75 trillion	$0
2	$31.84 trillion	$1.75 trillion	$0
3	$30.73 trillion	$1.75 trillion	$0
4	$29.59 trillion	$1.75 trillion	$0
5	$28.43 trillion	$1.75 trillion	$0
6	$27.25 trillion	$1.75 trillion	$0
7	$26.05 trillion	$1.75 trillion	$0
8	$24.82 trillion	$1.75 trillion	$0
9	$23.56 trillion	$1.75 trillion	$0
10	$22.28 trillion	$1.75 trillion	$0
11	$20.98 trillion	$1.75 trillion	$0
12	$19.65 trillion	$1.75 trillion	$0
13	$18.29 trillion	$1.75 trillion	$0
14	$16.91 trillion	$1.75 trillion	$0
15	$15.50 trillion	$1.75 trillion	$0
16	$14.06 trillion	$1.75 trillion	$0
17	$12.59 trillion	$1.75 trillion	$0
18	$11.09 trillion	$1.75 trillion	$0
19	$9.56 trillion	$1.75 trillion	$0
20	$8.00 trillion	$1.75 trillion	$0
21	$6.41 trillion	$1.75 trillion	$0
22	$4.79 trillion	$1.75 trillion	$0
23	$3.14 trillion	$1.75 trillion	$0
24	$1.45 trillion	$1.75 trillion	$0
25	$0.00	$1.75 trillion	$0.27 trillion
26	$0.00	$1.75 trillion	$2.02 trillion
27	$0.00	$1.75 trillion	$3.77 trillion
28	$0.00	$1.75 trillion	$5.52 trillion
29	$0.00	$1.75 trillion	$7.27 trillion
30	$0.00	$1.75 trillion	$9.02 trillion
