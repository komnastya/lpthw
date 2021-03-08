def break_words(stuff): #function #1
    """The function will break up words for us."""
    words = stuff.split(' ') #separates words in a sentence and displays them in an array in quotes, separated by commas
    return words

def sort_words (words): #function #2
    """Sorts the words"""
    return sorted(words) #sorts words alphabetically

def print_first_word (words): #function #3
    """Print the first word after popping it off."""
    word = words.pop(0) #cuts out the first word, but if you call the method again, the second word will be first
    print (word)

def print_last_word (words): #function #4
    """Print the last word after popping it off."""
    word = words.pop(-1) #selects the last word, but if you call the method again, then the "last" will be the penultimate word
    print (word)
# thus .рoр (), cuts out the word with the specified index from the string

def sort_sentence (sentence): #function #5
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence) #inside function #5 call function #1

    return sort_words(words) #function #2 sorts the words received by function #1 inside function #5, thus function #5 returns the result of function #2

def print_first_and_last (sentence): #function #6
    """Print the first and last words of the sentence"""
    words = break_words(sentence) #function #1
    print_first_word(words) #function #3
    print_last_word(words) #function #4

def print_first_and_last_sorted (sentence): #function #7
    """Sorts the words then prints the first and last one"""
    words = sort_sentence(sentence) #function #5
    print_first_word(words)
    print_last_word(words)

a = "It is only with the heart that one can see rightly; what is essential is invisible to the eye"
b = break_words(a)
print (b)
print (sort_words(b))
