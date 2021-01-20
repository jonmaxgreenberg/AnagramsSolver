__author__      = "Jonathan Greenberg"

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


all_words_frequencies ={}
with open('filename.pickle', 'rb') as handle:
    all_words_frequencies = pickle.load(handle)


def anagram_steal(base_word, num_letters_to_add):
  # start with base case, just adding one letter
  #loop thru the alphabet
  result_set = {}
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  for letter in alphabet:

    # get the word frequency of this word + the added letter
    freq = {}
    word_plus = base_word + letter
    for letter in word_plus:
      if letter in freq:
        freq[letter] += 1
      else:
        freq[letter] = 1
  
  # make sure the dict is ordered alphabetically, bc then the strings/keys will be equatable 
    freq = collections.OrderedDict(sorted(freq.items()))
    key = str(freq)
    
    # if this anagram is in all_words_frequencies then add to the result_set
    if key in all_words_frequencies:
      result_set[letter] = all_words_frequencies[key]
  
  if num_letters_to_add > 1:
    for combo in two_letter_combos:
      freq = {}
      word_plus = base_word + combo
      for letter in word_plus:
        if letter in freq:
          freq[letter] += 1
        else:
          freq[letter] = 1
    
    # make sure the dict is ordered alphabetically, bc then the strings/keys will be equatable 
      freq = collections.OrderedDict(sorted(freq.items()))
      key = str(freq)
      
      # if this anagram is in all_words_frequencies then add to the result_set
      if key in all_words_frequencies:
        result_set[combo] = all_words_frequencies[key]

  if num_letters_to_add > 2:
    for combo in three_letter_combos:
        freq = {}
        word_plus = base_word + combo
        for letter in word_plus:
          if letter in freq:
            freq[letter] += 1
          else:
            freq[letter] = 1
      
      # make sure the dict is ordered alphabetically, bc then the strings/keys will be equatable 
        freq = collections.OrderedDict(sorted(freq.items()))
        key = str(freq)
        
        # if this anagram is in all_words_frequencies then add to the result_set
        if key in all_words_frequencies:
          result_set[combo] = all_words_frequencies[key]
  pp.pprint(result_set)
  return result_set

anagram_steal(sys.argv[1], int(sys.argv[2]))
