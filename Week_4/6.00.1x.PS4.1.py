#==============================================================================
# Intro to Computer Science and Programming Using Python
# Week 4
# Problem Set 4.1
# Problem 1 - Word Scores
# (10 points possible)

#The first step is to implement some code that allows us to calculate the score for a single word. The function getWordScore should accept as 
#input a string of lowercase letters (a word) and return the integer score for that word, using the game's scoring rules.
# A Reminder of the Scoring Rules

# Hints
# 
#     You may assume that the input word is always either a string of lowercase letters, or the empty string "".
#     You will want to use the SCRABBLE_LETTER_VALUES dictionary defined at the top of ps4a.py. You should not change its value.
#     Do not assume that there are always 7 letters in a hand! The parameter n is the number of letters required for a bonus score 
#      (the maximum number of letters in the hand). Our goal is to keep the code modular - if you want to try playing your word game with n=10 or n=4, you will be able to do it by simply changing the value of HAND_SIZE!
#     Testing: If this function is implemented properly, and you run test_ps4a.py, you should see that the test_getWordScore() tests pass. Also test your implementation of getWordScore, using some reasonable English words.

#==============================================================================

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.
    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.
    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)
    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    
    word_value = 0
    
    for letter in word:
        word_value += SCRABBLE_LETTER_VALUES[letter]
    
    score = len(word) * word_value
    
    if len(word) == n:
        score += 50
    
    return score