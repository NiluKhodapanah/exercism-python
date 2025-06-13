"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return "un"+ word


def make_word_groups(vocab_words):

    vocab_words = list(vocab_words)
    prefix = vocab_words[0]
    output = prefix 

    for item in vocab_words[1:]:
        output += " :: " + prefix + item 

    return output


def remove_suffix_ness(word):
    consonants = "bcdfghjklmnpqrstvwxyz"
    actual_word = word[:-4]
    if actual_word[-2] in consonants and actual_word[-1] == 'i': 
        actual_word = actual_word.replace(actual_word[-1], 'y')
        return actual_word
    else:
        return actual_word


def adjective_to_verb(sentence, index):
    li_sen = sentence.replace('.','').split()
    word = li_sen[index]
    return word+'en'
