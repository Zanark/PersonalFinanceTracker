# Welcome Message

print(
    "Welcome to the Personal Finance Tracker App\n"
    + "You will be prompted to eneter details according to the Default Template. Template choice will be added in the future."
)

# Ask for Fiscal Year
FiscalYear = input("Enter the Fiscal Year")

# Ask for Month
Month = input("Enter the Month")

# Ask for budget for the month
MonthlyBudget = input("Enter the budget for the Month: " + Month)

# Ask for Bank Name
BankName = input("Enter the Bank's name")

# Ask for date of expense
DateOfExpense = input("Enter the date of expense")

# Ask for Expense Catagory

#Show following expense categories to chose from
# 1. Salary         Green
# 2. Transfer       Violet
# 3. Investment     Blue
# 4. Utilities      Grey
# 5. Hobby          Orange
# 6. Reimbursable   Yellow
# 7. Others         Normal

print('''
Expense Categories
# 1. Salary     
# 2. Transfer     
# 3. Investment   
# 4. Utilities     
# 5. Hobby          
# 6. Reimbursable   
# 7. Others         
''')

ExpenseCategory = input("Choose the category of expense")
# Under reimburable category, the first entry will have a red bar nad teh second entry confirming the reimbursement will have a green bar

# If 1 is chosen, then ask for the following:
# Basic Salary
# HRA
# Special Allowance
# Ask if anything added?
# Deductions

if(ExpenseCategory == 1):
    BasicSalary = input("Enter Basic Salary")
    HouseRentAllowance = input("Enter House Rent Allowance")
    SpecialAllowance = input("Enter Special Allowance")
    Extra = input("Enter anything Extra you received (Bonus/Overtime)")
    Deductions = input("Enter Deducations")

# All this goes under the details section

# If amount added is +ve then add to Credit column else add to Debit column

# After every entry update the closing balance variable and write the value after every step in the last column

# At the end mention the total amount expended under each category with a section for final balance

# Repeat from 'Ask for Bank Name'

# Check if the monthly budget was followed using the Expenses in Utilities, Hobby and Others and plot a bar graph for the difference.

# Repeat from 'Ask for Month'

