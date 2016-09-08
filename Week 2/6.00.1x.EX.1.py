#Intro to Computer Science and Programming Using Python
#Week 2
#Exercise 3.3: guess my number

print('Please think of a number between 0 and 100!')

new_guess = 50
high = 100
low = 0
answer = False
while answer == False:
    #print'Is your secret number ' + str(new_guess) + '?'
    print('Is your secret number ' + str(new_guess) + '?')
    #accuracy = '{}'.format(raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
    accuracy = '{}'.format(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
    if accuracy == 'h':
        high = new_guess
    elif accuracy == 'l':
        low = new_guess
    elif accuracy == 'c':
        break
    else:
        print('I did not understand your input')
    new_guess = int((high + low) / 2)
    
print('Game over. Your secret number was: ' + str(new_guess))