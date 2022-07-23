class InvestmentReturn():
    def __init__(self):
        self.income = []
        self.expenses = []
        self.cash_flow = []
        
    def showIncome(self):
        state_income = input("What is your state income? Rental/Laundry/Storage/Misc:")
        if state_income.lower() == 'rental':
            rental = int(input("What is your rental income:"))
            self.income.append(rental) 
        elif state_income.lower() == 'laundry':
            laundry = int(input("How much is your laundry: "))
            self.income.append(laundry)
            
        elif state_income.lower() == 'storage':
            storage = int(input("What do you pay for storage"))
            self.income.append(storage)
            
        elif state_income.lower() == 'random':
            storage = int(input("Please state your random income: "))
            self.income.append(storage)
        elif state_income.lower =='quit':
            pass
         
        else:
            print("Try another command")
            monthly_income = int(sum(self.income))
            
        print(f"Your monthly income is: {monthly_income}")
            
    def showExpenses(self):
        state_expense = (input("Which expense would you like to state? Tax/Insurance/Utilities/Repairs/Mortgage/Other:"))
              
        if state_expense.lower() == 'tax':
            tax = int(input("What are your tax expenses:"))
            self.expenses.append(tax)
              
        elif state_expense.lower() == 'insurance':
            insurance = int(input("How much is your insurance expense:"))
            self.expenses.append(insurance)
              
        elif state_expense.lower() == 'utilities':
            utilities = int(input("Average utilities:"))
            self.expenses.append(utilities)
        elif state_expense.lower() == 'repairs':
            repairs = int(input("What is your average repair bill"))
            self.expenses.append(repairs)
            
        elif state_expense.lower() == 'mortgage':
            mortgage = int(input("How much do you pay for mortgage"))
            self.expenses.append(mortgage)
            
        elif state_expense.lower() == 'other':
            other = int(input("DO you have any other expenses: "))
            self.expenses.append(other)

        elif state_expense.lower == 'quit':
            pass
        
        else:
            print("Please try again")
       
        monthly_expenses = int(sum(self.expenses))
        
        print(f"Your monthly expenses total to: {monthly_expenses}")
              
    def showCashFlow(self):
        current_cashFlow = sum(self.income) - sum(self.expenses)
        self.cash_flow.append(current_cashFlow)
        print(f"Current cash flow is: {current_cashFlow}")
            
    def showROI(self):
        total_investment = int(input("How much would you like to invest: "))
        cashFlow = sum(self.cash_flow)
        annual_cashFlow = cashFlow * 12
        ROI = (annual_cashFlow / total_investment) * 100
    
p1=InvestmentReturn()
p1.showIncome()
p1.showExpenses()
p1.showCashFlow()