monthly_income = int(input("Enter monthly income: "))
monthly_expenses = int(input("Enter monthly expenses: "))

print("monthly_income", monthly_income)
print("monthly_expenses", monthly_expenses)

# Subtask 2
savings = monthly_income - monthly_expenses
if savings > 0.20 * monthly_income:             
    print("You are saving enough!")
else:
    print("You need to save more.")




