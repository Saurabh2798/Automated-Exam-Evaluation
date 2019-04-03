# necessary imports
import enchant
import tokenizer as tk
import score as sc
dictionary = enchant.Dict("en_US")   # create dictionary for US English

def SpellChecker(line,cosine): # function that checks for spelling errors
    for token in tk.tokens(line): # iterate over tokens
        spellMistakes=0 
        strippedToken=token.rstrip()
        if(dictionary.check(strippedToken)==False): # if it not an english dictionary word
            spellMistakes = spellMistakes+1 # compute spell mistakes
    print("Spelling mistakes >>>",spellMistakes)
    return spellMistakes