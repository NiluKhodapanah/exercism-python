'''
import itertools

def find_anagrams(word, candidates):
    res = []
    for a in itertools.permutations(word):  #in this loop you want to find all possible anagrams
        anagram = set(''.join(a))
    all_anagrams = list(anagram)

    for ana in all_anagrams:
        if word == ana:
            res.append(ana)
    return res

'''

def find_anagrams(word, candidates):
    ana = []
    word_sorted = sorted(word.lower())
    for can in candidates:

        if word.lower() == can.lower():
            continue
        if sorted(can) == word_sorted:
            ana.append(can)
    return ana

        
    