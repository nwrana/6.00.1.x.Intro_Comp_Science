'''
balance = the outstanding balance on the credit card
annualInterestRate = annual interest rate as a decimal
monthlyPaymentRate = minimum monthly payment rate as a decimal
minPayment = minimum amount paid on credit card
'''

balance = 4773
#monthlyPaymentRate = 0.02
fixed = 440
annualInterestRate = 0.2

totalMonths = 12
for month in range(totalMonths):
    
    print('balance: ' + str(balance))
    
    #minPayment = balance * monthlyPaymentRate  
    #unpaidBalance = balance - minPayment      
    unpaidBalance = balance - fixed    
    interest = unpaidBalance * (annualInterestRate / 12.0)    
    balance = unpaidBalance + interest
    
    #print('minPayment: ' + str(minPayment))
    print('unpaidBalance: ' + str(unpaidBalance))
    print('interest: ' + str(interest))
    
print(round(balance, 2))

 