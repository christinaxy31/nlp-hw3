import datasets
from datasets import load_dataset
from transformers import AutoTokenizer
from torch.utils.data import DataLoader
from transformers import AutoModelForSequenceClassification
from torch.optim import AdamW
from transformers import get_scheduler
import torch
from tqdm.auto import tqdm
import evaluate
import random
import argparse
from nltk.corpus import wordnet
from nltk import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer

random.seed(0)


def example_transform(example):
    example["text"] = example["text"].lower()
    return example


### Rough guidelines --- typos
# For typos, you can try to simulate nearest keys on the QWERTY keyboard for some of the letter (e.g. vowels)
# You can randomly select each word with some fixed probability, and replace random letters in that word with one of the
# nearest keys on the keyboard. You can vary the random probablity or which letters to use to achieve the desired accuracy.


### Rough guidelines --- synonym replacement
# For synonyms, use can rely on wordnet (already imported here). Wordnet (https://www.nltk.org/howto/wordnet.html) includes
# something called synsets (which stands for synonymous words) and for each of them, lemmas() should give you a possible synonym word.
# You can randomly select each word with some fixed probability to replace by a synonym.

nltk.download('wordnet')

def custom_transform(example):
    ################################
    ##### YOUR CODE BEGINGS HERE ###

    # Design and implement the transformation as mentioned in pdf
    # You are free to implement any transformation but the comments at the top roughly describe
    # how you could implement two of them --- synonym replacement and typos.

    # You should update example["text"] using your transformation

    qwerty_neighbors = {
    'a': 'qws', 'b': 'vgn', 'c': 'xdfv', 'd': 'ersfcx', 'e': 'wsdr', 'f': 'rtgvc', 
    'g': 'ftyhbv', 'h': 'gyujnb', 'i': 'ujko', 'j': 'huikmn', 'k': 'jiolm', 
    'l': 'kop', 'm': 'njk', 'n': 'bhjm', 'o': 'iklp', 'p': 'ol', 'q': 'wa', 
    'r': 'edft', 's': 'awedz', 't': 'rfgy', 'u': 'yhji', 'v': 'cfgb', 'w': 'qase', 
    'x': 'zsdc', 'y': 'tghu', 'z': 'asx'
    }


    def introduce_typos(word):
        if len(word) < 2 or random.random() > 0.5:
            return word
        # ifelse, then replace
        char_idx = random.randint(0, len(word) - 1）
        char = word[char_idx]

        if char in qwerty_neighbors:
            new_char = random.choice(qwerty_neighbors[char])
            word = word[:char_idx] + new_char + word[char_idx + 1:]

        return word

    def replace_with_synonym(word):
        synonym = set()
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonym = lemma.name().replace('_', ' ')
                if synonym.lower() != word.lower():
                    synonyms.add(synonym)
        if synonyms:
            return random.choice(list(synonyms))
        return word

    words = example["text"].split()
    transformed_words = []

    for word in words:
        if random.random() < 0.1:
            word = introduce_typos(word)

        if random.random() < 0,1 and wordnet.synsets(word):
            word = replace_with_synonym(word)

        transformed_words.append(word)

    transformed_sentence = ' .join(transformed_words)

    example["text"] = transformed_sentence
  
    

    

    ##### YOUR CODE ENDS HERE ######

    return example
