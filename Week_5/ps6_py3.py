# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 13:33:50 2016

@author: w15psnnw
"""

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        #Create a normal dictionary mapping
        lowerNorm = {}
        upperNorm = {}
        for i in range(0,26):
            lowerNorm[string.ascii_lowercase[i]] = i
            upperNorm[string.ascii_uppercase[i]] = i
                
        #create a dictionary with shifted values 
        lowerShift = {}
        upperShift = {}
        for i in range(0,26):
            ID = i + shift
            if  ID >= 26:
                ID = ID - 26
            lowerShift[string.ascii_lowercase[i]] = ID
            upperShift[string.ascii_uppercase[i]] = ID
        
        #map shifted keys to normal keys for lower letters
        lowerCombinedMap = {}
        for i in lowerShift.values():
            lowerLetterShift = list(lowerNorm.keys())[list(lowerNorm.values()).index(i)]
            lowerLetterNorm = list(lowerShift.keys())[list(lowerShift.values()).index(i)]
            lowerCombinedMap[lowerLetterNorm] = lowerLetterShift            
        
        #map shifted keys to normal keys for upper letters
        upperCombinedMap = {}
        for i in upperShift.values():
            upperLetterShift = list(upperNorm.keys())[list(upperNorm.values()).index(i)]
            upperLetterNorm = list(upperShift.keys())[list(upperShift.values()).index(i)]
            upperCombinedMap[upperLetterNorm] = upperLetterShift    
        
        #combine mapping into a single dictionary
        #finalMap = dict(lowerCombinedMap.items() + upperCombinedMap.items())
        finalMap = lowerCombinedMap.update(upperCombinedMap)        
        return finalMap

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        cipher = self.build_shift_dict(shift)
        cipherText = []
        for i in self.get_message_text():
            if i == " ":
                cipherText.append(" ")
            elif i in string.punctuation or i in string.digits:
                cipherText.append(i)
            else:
                cipherText.append(cipher[i])
        
        return ''.join(cipherText)