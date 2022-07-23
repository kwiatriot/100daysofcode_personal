"""
Day 030 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 7/23/2022
"""

# Starting to handle catching exceptions

#FileNotFound - trying to open a file that doesn't exist
# with open("a_file.txt") as file:
#   file.read()

#KeyError - trying to call a key that doesn't exsist
# a_dictionary = {"key": "value"}
# value = a_dictonary["non_exsistant_key"]

#IndexError - trying to index a position that doesnt have a value
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#TypeError - trying to do something to a variable that isnt supported
# text = "abc"
# print(text + 5)

#Syntx for a Try/Except Block
#try:
    # Something that might cause an exception
#except:
    # Do this if there was an execption
#else:
    # Do this if there were NO exceptions
#finally:
    # Do this no matter what happens

#Alternates for the except block
#except ErrorType as variableName:
    # Do this if the specfified ErrorType was raised
    #print(f"This key {variableName} does not exsist")

# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Human height should not be over 3 meters.")

import pandas
# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Numbers are not in the alphabet. Only letters are accepted.")
        generate_phonetic()
    else:    
        print(output)

generate_phonetic()