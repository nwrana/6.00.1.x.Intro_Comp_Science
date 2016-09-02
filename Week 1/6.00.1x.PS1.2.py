#Intro to Computer Science and Programming Using Python
#Week 1
#Problem Set 1.1

#Problem 2
#(10 points possible)

#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s. 
#For example, if s = 'azcbobobegghakl', then your program should print
#Number of times bob occurs is: 2

s = 'asdasbobobdasbobob'

key = 'bob'
length = len(s)
count = 0
index = 0

for letter in s:
    if letter == 'b' and length > 2:
        temp = letter + s[index + 1] + s[index + 2]
        if temp == key:
            count += 1
    index += 1
    length = len(s) - index #special case when b appears at end of string, cannot index past the length of the string
print('Number of times bob occurs is: ' + str(count))

#for i in range(5):
#    i += 1
#    print(i)