balance = 5000   
annualInterestRate = 0.2

startBalance = balance
#Set boundaries

#a lower bound of 0 soudns good but we can do better. If no interest was accrued,
#we could pay off the entire balance in 1 year by paying 1/12 of teh balance each month
lowerBound = balance / 12 

#what if we never made any payments all year ? a good upper bound would be 1/12 of the
#total after having interest compounded monthly for 1 year
for month in range(12):    
    interest = balance * (annualInterestRate / 12.0)    
    balance += interest    
upperBound = balance / 12
    
#Monthly payment upper bound = (Balance * (1 + Monthly interest rate)**12) / 12.0

lowestPayment = 0
startBalance = balance
count = 0
  
while balance > 0: 
    
    balance = startBalance 
    lowestPayment = (upperbound - lowerbound) / 2 
    #print('lowest payment: ' + str(lowestPayment))
    
    for month in range(12): 
        unpaidBalance = balance - lowestPayment      
        interest = unpaidBalance * (annualInterestRate / 12.0)    
        balance = unpaidBalance + interest
        count += 1

    if balance     
#result = int(lowestPayment)    
print('Lowest Payment: ' + str(lowestPayment))
print('Final count: ' + str(count))

