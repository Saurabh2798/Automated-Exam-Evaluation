# Necessary imports
import re, math
from collections import Counter

#Sample text
#text1="In 1909 Mamie Garvin Fields became one of the first African-American public school teachers in Charleston County, South Carolina"
#text2="In 1909 Mamie Garvin Fields wound up one of the main African-American government funded teachers in Charleston County, South Carolina"

def text_to_vector(text): # Function to convert text to vector
    WORD = re.compile(r'\w+') # regex for word
    words = WORD.findall(text) # find all words
    return Counter(words)

def get_cosine(vec1, vec2): # Function to compute cosine similarity
    intersection = set(vec1.keys()) & set(vec2.keys()) 
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator # return cosine similarity

