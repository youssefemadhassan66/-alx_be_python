monthly_income = int(input("Enter your monthly income: "));
monthly_expenses = int(input("Enter your total monthly expenses:"));
monthly_savings = monthly_income - monthly_expenses;
ProjectedSaving = monthly_savings * 12 + (monthly_savings * 12 * 0.05);
print("Your monthly savings is " + str(monthly_savings));
print("Projected savings after one year, with interest, is:" + str(ProjectedSaving));
