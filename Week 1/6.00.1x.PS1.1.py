#Intro to Computer Science and Programming Using Python
#Week 1
#Problem Set 1.1

#(10 points possible)
#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 
#'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5

#Need a variable that contaings all vowels to reference
vowels = ['a','e','i','o','u'] 

#need input from user
user_input = input('Please enter a string: ')

#declare count variable
count = 0
for letters in user_input:
    for vowel in vowels:
        if vowel == letters:
            count += 1
print('Number of vowels: ' + count)



