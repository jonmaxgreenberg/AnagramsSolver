# -*- coding: utf-8 -*-
"""AnagramsSolver.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pl4yvva0AtyTb6HWcUfcRMsEIeNmRUO0

save the anagram dictionary in a file, pickle it maybe
"""

import pandas as pd
import collections
import itertools
fileObject = open("words.txt", "r")
data = fileObject.read()
words = data.split('\n')

# number of unique anagrams in english
print(words[10])
print(words[len(words) - 1])
print(len(words))

print([words[200]])

# Create a dict with key as the letter frequencies and value is list of the words

all_words_frequencies = {}
for word in words:
  freq = {}
  for letter in word:
    if letter in freq:
      freq[letter] += 1
    else:
      freq[letter] = 1
  
  # make sure the dict is ordered alphabetically, bc then the strings/keys will be equatable 
  freq = collections.OrderedDict(sorted(freq.items()))

  key = str(freq)
  print(key)
  #check if that frequency exists in the map

  if key in all_words_frequencies:
    all_words_frequencies[key].append(word)
    
  else:  # add it to the word frequency map
    list_of_words = word.split('\n')
    all_words_frequencies[key] =  list_of_words # just add the word in a list

# number of unique anagrama
len(all_words_frequencies)

for key, value in all_words_frequencies.items():
  if len(value) > 13:
    print(key)
    print(value)

#next up need to take in a word, and then a number of letters to add to it, start with just by adding one letter to it

def anagram_steal(base_word):
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
  
  # result_set = list(itertools.chain.from_iterable(result_set))
  return result_set

anagram_steal("talkers")

# to start the solution of adding two letters, create a list with all of the combinations of 2 letters in the alphabet
#loop thru alphabet nested, and make a list of strings with all two letter combinations
two_letter_combos = []
three_letter_combos = []

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for letter in alphabet:
  for letter2 in alphabet:
    combo = letter + letter2
    two_letter_combos.append(combo)

for letter in alphabet:
  for letter2 in alphabet:
    for letter3 in alphabet:
      combo = letter + letter2 + letter3
      three_letter_combos.append(combo)

print(len(three_letter_combos))
#next up need to take in a word, and then a number of letters to add to it, start with just by adding one letter to it

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
  return result_set

anagram_steal("talkers", 3)

# do this as a second step/option, if you want to be able to add 2 letters
# loop thru every combination, add it to the base word, and then get the anagram, and then same exact process, i can add it on to the function above