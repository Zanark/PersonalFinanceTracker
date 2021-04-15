# Personal Finance Tracker
##########################
# Author: Zanark

print(
    "Welcome to the Personal Finance Tracker App\n"
    + "You will be prompted to eneter details according to the Default Template. Template choice will be added in the future."
)

FileName = input("Enter the name of the record file")

f = open( FileName ,"a")

# Ask for Fiscal Year
FiscalYear = input("Enter the Fiscal Year")
f.write('# ' + FiscalYear)

while 1 > 0:    
    
    # Ask for Month
    Month = input("Enter the Month(Enter 0 to exit)")
    if Month == 0:
        break
    f.write('## ' + Month)

    # Ask for budget for the month
    MonthlyBudget = input("Enter the budget for the Month: " + Month)
    f.write('**MOnthly Budget:**' + MonthlyBudget)

    while 1 > 0:

        # Ask for Bank Name
        BankName = input("Enter the Bank's name(Enter 0 to exit)")
        if BankName == 0:
            break
        f.write('### ' + BankName)

        f.write('''| Date | Details | Credit | Debit | Closing Balance |
        | :---: | :---: | :---: | :---: | :---: |
        ''')

        Credit = 0.0
        Debit = 0.0
        ClosingBalance = 0.0

        while 1 > 0:

            Credit = 0.0
            Debit = 0.0
            
            # Ask for date of expense
            DateOfExpense = input("Enter the date of expense (Enter 0 to exit)")

            if(DateOfExpense == 0):
                break

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
                BasicSalary = float(input("Enter Basic Salary"))
                HouseRentAllowance = float(input("Enter House Rent Allowance"))
                SpecialAllowance = float(input("Enter Special Allowance"))
                Extra = float(input("Enter anything Extra you received (Bonus/Overtime)"))
                Deductions = float(input("Enter Deducations"))

                Credit = BasicSalary + HouseRentAllowance + SpecialAllowance + Extra - Deductions
                ClosingBalance = ClosingBalance + Credit - Debit

                f.write(f"| {DateOfExpense} | {BasicSalary} \n {HouseRentAllowance} \n {SpecialAllowance} \n {Extra} \n {Deducations} | {Credit} | {Debit} | {ClosingBalance} |")

            elif(ExpenseCategory == 2):
                TransferDetails = input("Enter the details of the transfer")

                Debit = float(input("Enter the Amount transfered"))

                ClosingBalance = ClosingBalance + Credit - Debit

                f.write(f"| {DateOfExpense} | {TransferDetails} | {Credit} | {Debit} | {Closing Balance} |")
                
            elif(ExpenseCategory == 3):
                TransferDetails = input("Enter the details of the Investment")

                Debit = float(input("Enter the Amount"))

                ClosingBalance = ClosingBalance + Credit - Debit

                f.write(f"| {DateOfExpense} | {TransferDetails} | {Credit} | {Debit} | {Closing Balance} |")
                
            elif(ExpenseCategory == 4):
                TransferDetails = input("Enter the details of the expenditure")

                Debit = float(input("Enter the Amount"))

                ClosingBalance = ClosingBalance + Credit - Debit

                f.write(f"| {DateOfExpense} | {TransferDetails} | {Credit} | {Debit} | {Closing Balance} |")

            elif(ExpenseCategory == 5):
                TransferDetails = input("Enter the details of the expenditure")

                Debit = float(input("Enter the Amount"))

                ClosingBalance = ClosingBalance + Credit - Debit

                f.write(f"| {DateOfExpense} | {TransferDetails} | {Credit} | {Debit} | {Closing Balance} |")

            else:
                TransferDetails = input("Enter the details of the expenditure")

                Debit = float(input("Enter the Amount"))

                ClosingBalance = ClosingBalance + Credit - Debit

                f.write(f"| {DateOfExpense} | {TransferDetails} | {Credit} | {Debit} | {Closing Balance} |")

            # All this goes under the details section

            # If amount added is +ve then add to Credit column else add to Debit column

            # After every entry update the closing balance variable and write the value after every step in the last column



        # At the end mention the total amount expended under each category with a section for final balance
        f.write(f"<br> --- **Closing Balance for {Month} on {BankName}:** {ClosingBalance} <br> <br> ---")

        # Repeat from 'Ask for BankName'



    # Check if the monthly budget was followed using the Expenses in Utilities, Hobby and Others and plot a bar graph for the difference.

    # Repeat from 'Ask for Month'

