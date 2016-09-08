balance = 4773   
annualInterestRate = 0.2
 
#Guess and check method - algorithm
#want to minimize lowestPayment

lowestPayment = 0
startBalance = balance
count = 0
  
while balance > 0: 
    
    balance = startBalance 
    lowestPayment += 10 
    print('lowest payment: ' + str(lowestPayment))
    
    for month in range(12): 
        unpaidBalance = balance - lowestPayment      
        interest = unpaidBalance * (annualInterestRate / 12.0)    
        balance = unpaidBalance + interest
        print(balance) 
    
    count += 1
    
#result = int(lowestPayment)    
print('Lowest Payment: ' + str(lowestPayment))
print('Final count: ' + str(count))

