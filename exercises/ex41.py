# ex41

import random  # a module that generates random numbers
from urllib.request import (
    urlopen,
)  ##urllib.request is a Python module for openning URLs
import sys  # import system functions

WORD_URL = "http://learncodethehardway.org/words.txt"  # string
WORDS = []  # empty list

# dictionary
PHRASES = {
    "class %%%(%%%):": "Make a class named %%% that is-a %%%",
    "class %%%(object):\n\tdef__init__(self, ***)": "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)": "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()": "Set *** to an instance of class %%%.",
    "***.***(@@@)": "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'": "From *** get the *** attribute and set it to '***'.",
}

if len(sys.argv) == 2 and sys.argv[1] == "english":  # reads arguments from terminal
    # and checks the condition if there is ONE additional "english" argument
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False
    print(PHRASE_FIRST)


for word in urlopen(WORD_URL).readlines():  # loads up the words from the website
    WORDS.append(str(word.strip(), encoding="utf-8"))
    # The str(object, encoding=encoding, errors=errors) function returns the string version of the given object
    # strip() removes spaces at the beginning and at the end of the string
# thus this for-loop creates an array of all words from a file by link removing all spaces at the beginning and at the end of the string


def convert(snippet, phrase):
    # snippet is a key of 'PHRASE' dictionary
    # phrase is a value of 'PHRASE' dictionary. See 'try' block

    class_names = [
        tmr.capitalize() for tmr in random.sample(WORDS, snippet.count("%%%"))
    ]

    # random.sample(list_name, n) returns N elements from the list
    # .count('smth') returns the number of times the value in quotes appears in the list
    # thus lines 44-45 counts number of markers (%%%) in the phrase and returns as many words as there are markers from the 'WORDS' list and capitalizes them
    # number of words equals to the number of markers
    # %%% is a placeholder for any class_name in sample

    other_names = random.sample(WORDS, snippet.count("***"))

    # returns number of elements from the WORDS list equals to the number of *** markers in phrase;
    # *** is a placeholder for any variable_name in sample

    results = []
    param_names = []

    for tmp in range(0, snippet.count("@@@")):  # the loop fills the param_names list
        param_count = random.randint(1, 3)  # generates randomly the number [1,3]
        param_names.append(", ".join(random.sample(WORDS, param_count)))
        # random.sample(list_name, n) returns N elements from the 'WORDS' list

    print("param_names = ", param_names)

    for sentence in snippet, phrase:  # key, value

        result = sentence[:]  # copies list[from:length]

        print("sentence = ", sentence)

        for word in class_names:
            result = result.replace(
                "%%%", word, 1
            )  # replaces the first marker from class_name list

        for word in other_names:
            result = result.replace(
                "***", word, 1
            )  # replaces the first marker from other_name list

        for word in param_names:
            result = result.replace(
                "@@@", word, 1
            )  # replaces the first marker from param_names list

        results.append(result)
        print("results = ", results)

    return results


try:
    while True:
        snippets = list(
            PHRASES.keys()
        )  #'PHRASES' dictionary keys forms 'snippets' list
        random.shuffle(
            snippets
        )  # shuffles the 'snippets' list (reorganizes the order of the list items)

        for snippet in snippets:
            # snippet is one of the list elements which is key of 'PHRASES' dictionary
            phrase = PHRASES[
                snippet
            ]  # phrase is value of 'PHRASES' dictionary (e.g. Make a class named %%% that is-a %%%) found by key from 'snippets' list
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:  # if PHRASE_FIRST = True
                question, answer = (
                    answer,
                    question,
                )  # ... answer and question are swapped

            print("Question: ", question)
            input("> ")
            print(f"ANSWER: {answer}\n\n")

except EOFError:
    print("\nBye")
