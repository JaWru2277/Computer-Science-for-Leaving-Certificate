# Question 16 (a)


# Function to calculate readability score of text
def calculate_readability_score(text):

    # Split the text into a list of words
    words = text.split()
    print("The list of words in the text is:\n", words)

    # Initialise the word counters
    word_count = len(words) # Number of words in list
    short_word_count = 0
    
    #(v) - Counter of short words
    for i in words:
        if len(i) <= 2:
            short_word_count += 1
    print("Short words:", short_word_count)
        #End of (v)

    # Initialise the number of sentences
    sentence_count1 = text.count(".")
    
    #(iii) - Makes the program count (!) as well
    sentence_count2 = text.count("!") 
    sentence_count_total = sentence_count1+sentence_count2
        #End of (iii)
    
    # Calculate the readability score
    #(vi) - Updated calculation of the readability score using formula
    score = 0.4*((word_count/sentence_count_total)+(100*((word_count-short_word_count)/word_count)))
    score = round(score, 2) # Round the score to 2 d.p.
        #End of (vi)
    return score

# Set the text for analysis
text1 = "Elaborate sentences influence readability in subtle and unpredictable ways."
text2 = "I do not like green eggs and ham! I do not like them Sam I am!"

# Calculate the score for text1
score1 = calculate_readability_score(text1)

#(i) - Prints the readability score followed by a blank line
print("Readability Score 1:", score1, "\n")
    #End of (i)

#(ii) 
score2 = calculate_readability_score(text2) # calls the function for text 2 as well
print("Readability Score 2:", score2, "\n") # prints score 2, followed by a blank line
    #End of (ii)
    
#(iv) - Compares two socres - score1 and score2
if score1 == score2:
    print("Both scores are the same.")
elif score1 < score2:
    print("The first text is easier to read.")
else:
    print("The second text is easier to read.")
    #End of (iv)
