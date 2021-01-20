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

result_set = {}

# upload frequency dictionary from pickle file
all_words_frequencies ={}
with open('frequency_dict.pickle', 'rb') as handle:
    all_words_frequencies = pickle.load(handle)


def find_anagrams(base_word, added_letters):
  # get the word frequency of this word + the added letter
    freq = {}
    word_plus = base_word + added_letters
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

def anagram_steal(base_word, num_letters_to_add):
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  for letter in alphabet:
    find_anagrams(base_word, letter)
  
  if num_letters_to_add > 1:
    for combo in two_letter_combos:
      find_anagrams(base_word, combo)

  if num_letters_to_add > 2:
    for combo in three_letter_combos:
      find_anagrams(base_word, combo)

  pp.pprint(result_set)
  return result_set

anagram_steal(sys.argv[1], int(sys.argv[2]))
