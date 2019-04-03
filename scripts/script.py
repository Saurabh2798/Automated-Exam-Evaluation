# Necessary imports
import sys
from PIL import Image
import pytesseract
from nltk.stem import WordNetLemmatizer

import removeStop as rs
import cosineSim as cs
import spellCheck as sc
import score as sr

# some variables to be used later
ocr=""
spellMistakes=0
score=0

def main(): # the main function

    image2 = Image.open(str(sys.argv[1])) # Get the path of uploaded image and read it
    text = pytesseract.image_to_string(image2, lang="eng") # Use pytesseract to extract text from image
    print("Your answer as detected by OCR >>> ", text)
    
    processed_data=rs.rmStop(text) # call rmStop with extracted text to remove stop words and store the result in processed_data

    lemmatizer = WordNetLemmatizer() # Lemmatizer to be used

    lemmatizedWords = [] # a dict to be used later
    for word in processed_data: # Iterate over the processed_data
        lemmatizedWords.append(lemmatizer.lemmatize(word.lower())) # lemmatize the words and append them to the dictionary
        
    keywordsString = str(sys.argv[2]) # Get the expected answer given as input by the user
    processedKeywords=rs.rmStop(keywordsString) # remove stopwords from expected answer
    
    lemmatizedWordsString = " ".join(lemmatizedWords) # convert the lemmatized words back to string, will be needed to compute cosine similarity
    processedKeywordsString = " ".join(processedKeywords) # convert the keywords to string, will be needed to compute cosine similarity

    text1 = lemmatizedWordsString # store the value of lemmatizedWordsString in a new variable
    text2 =  processedKeywordsString # store the value of keywordsString in a new variable

    vector1 = cs.text_to_vector(text1) # compute the vector for text1
    vector2 = cs.text_to_vector(text2) # compute the vector for text2

    cosine = cs.get_cosine(vector1, vector2) # compute the cosine similarity using the two vectors to compute similarity between the two
    
    spellMistakes = sc.SpellChecker(lemmatizedWordsString, cosine) # Compute the spell mistakes
    score = sr.Score(cosine, spellMistakes) # Compute the final score
    print("Cosine: ", cosine)
    print("Score: ",score)
    
    
if __name__ == '__main__':
    main() 
