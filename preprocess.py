__author__      = "Jonathan Greenberg"
'''
This file Preprocesses all the words in the english dictionary:
  Splits the text file into separate words
  Creates a dictionary/map which maps every unique letter frequency to a list of words
  Uses pickle to save the dictionary as a pickle file to be imported by the AnagramsSolver.py file
'''
import pandas as pd
import collections
import itertools
import pprint
import sys
import pickle

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
two_letter_combos = []
three_letter_combos = []
pp = pprint.PrettyPrinter(indent=4)


for letter in alphabet:
  for letter2 in alphabet:
    combo = letter + letter2
    two_letter_combos.append(combo)

for letter in alphabet:
  for letter2 in alphabet:
    for letter3 in alphabet:
      combo = letter + letter2 + letter3
      three_letter_combos.append(combo)

# words originally from here: https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt

fileObject = open("words.txt", "r")
data = fileObject.read()
words = data.split('\n')

# Create a dict with key as the letter frequencies and value is list of the words

all_words_frequencies = {}
for word in words:
  freq = {}
  for letter in word:
    if letter in freq:
      freq[letter] += 1
    else:
      freq[letter] = 1
  
  # Make sure the dict is ordered alphabetically, bc then the strings/keys will be equatable 
  freq = collections.OrderedDict(sorted(freq.items()))

  key = str(freq)

  #check if that frequency exists in the map

  if key in all_words_frequencies:
    all_words_frequencies[key].append(word)
    
  else:
    list_of_words = word.split('\n')
    all_words_frequencies[key] =  list_of_words


with open('frequency_dict.pickle', 'wb') as handle:
    pickle.dump(all_words_frequencies, handle, protocol=pickle.HIGHEST_PROTOCOL)

