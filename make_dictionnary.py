from pathlib import Path
import pickle

path_wordlist = Path("fr_full.txt")
path_dictionnary = Path("dict_fr.pckl")

words = set()

MIN_OCCURENCES = 20

with open(path_wordlist, "r") as f_wordlist:
    for line in f_wordlist:
        word, occurences = line.split() 
        occurences = int(occurences)
        if occurences >= MIN_OCCURENCES:
            words.add(word)

pickle.dump(words, open(path_dictionnary, "wb"))