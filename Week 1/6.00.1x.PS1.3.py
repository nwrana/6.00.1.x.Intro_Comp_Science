#==============================================================================
# Intro to Computer Science and Programming Using Python
# Week 1
# Problem Set 1.1
#  Problem 3
# (15 points possible)
# 
# Assume s is a string of lower case characters.
# 
# Write a program that prints the longest substring of s in which the letters occur 
#in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
# 
# Longest substring in alphabetical order is: beggh
# 
# In the case of ties, print the first substring. For example, if s = 'abcbcd', 
#then your program should print
# 
# Longest substring in alphabetical order is: abc
# 
#==============================================================================

#Way fo thinking:
#cycle through every letter in the string
#take the current letter and compare it against the previous letter:
#if previous number does not exist, create new list
#if previous number exists and current letter is in alphabetical order, add current letter to active list
#if the condition is False (current letter is not in alphabetical order)
    #add current list to master_list
    #increment index by one -> this will keep track of how many lists of alphabetical lists we have created
    #modify string by removing string of letters stored in active list from string   
    # as long as len(string) > 0, start while loop again 

s = 'abcdadebcdef'
start = 0
index = 0
master = []

for letter in s:
    if index+1 == len(s):
        string = s[start:]
        master.append(string)
        break
    elif letter <= s[index+1]:
        index += 1
    elif letter > s[index+1]:
        index += 1
        string = s[start:index]
        master.append(string)
        start = index #update new start position 

lengthTot = []
for element in master:
    lengthTot.append(len(element))

indexMax = lengthTot.index(max(lengthTot))
maxString = master[indexMax]

print('Longest substring in alphabetical order is: ' + str(maxString))

    

    