# necessary imports
from nltk.corpus import stopwords
import tokenizer as tk

def rmStop(data): # function to remove stop words
    stopWords=set(stopwords.words('english')) # Stopwords in English
    words=tk.tokens(data) # Tokenize data into words
    wordsFiltered=[] # an empty dict to store filtered words
    for w in words: # iterate over the words
        if w not in stopWords: # if the word is not in stopWords
            wordsFiltered.append(w) # append it to wordsFiltered
    return wordsFiltered # return the filtered words
