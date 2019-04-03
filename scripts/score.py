def Score(cosine, spellMistakes): # function to compute the final score
    score = 1
    if cosine*100 > 75: # if the computed cosine similarity of the two sentences is greater than a threshold (75 here)
        score = score - ( 0.05 * spellMistakes) # compute the score
    else: 
        score = 0
        print("\nOutput >>> inaccurate answer") # return the message
    return score # return score
