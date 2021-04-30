# Identity:
# Given a list of numbers, write a list comprehension that produces a copy of the list.
#    identity([1, 2, 3, 4, 5]) -> [1, 2, 3, 4, 5]
#    identity([]) -> []


def identity(nums):
    return [i for i in nums]


print(identity([1, 2, 3, 4, 5]))


# Doubled:
# Given a list of numbers, write a list comprehension that produces a list of each number doubled.
#    >>> doubled([1, 2, 3, 4, 5])
#    [2, 4, 6, 8, 10]
#    >>> doubled([-2, 2, -10, 10])
#    [-4, 4, -20, 20]


def doubled(nums):
    return [i * 2 for i in nums]


print(doubled([1, 2, 3, 4, 5]))
print(doubled([-2, 2, -10, 10]))


# Squared:
# Given a list of numbers, write a list comprehension that produces a list of the squares of each number.
#    >>> squared([1, 2, 3, 4, 5])
#    [1, 4, 9, 16, 25]
#    >>> squared([-2, 2, -10, 10])
#    [4, 4, 100, 100]


def squared(nums):
    return [i * i for i in nums]


print(squared([1, 2, 3, 4, 5]))
print(squared([-2, 2, -10, 10]))


# Evens:
# Given a list of numbers, write a list comprehension that produces a list of only the even numbers in that list.
#    >>> evens([1, 2, 3, 4, 5])
#    [2, 4]
#    >>> evens([1, 3, 5])
#    []
#    >>> evens([-2, -4, -7])
#    [-2, -4]


def evens(nums):
    return [x for x in nums if not x % 2]


print(evens([1, 2, 3, 4, 5]))
print(evens([1, 3, 5]))
print(evens([-2, -4, -7]))


# """Odds:
# Given a list of numbers, write a list comprehension that produces a list of only the odd numbers in that list.
#    >>> odds([1, 2, 3, 4, 5])
#    [1, 3, 5]
#    >>> odds([2, 4, 6])
#    []
#    >>> odds([-2, -4, -7])
#    [-7]


def odds(nums):
    return [x for x in nums if x % 2]


print(odds([1, 2, 3, 4, 5]))
print(odds([2, 4, 6]))
print(odds([-2, -4, -7]))


# Positives:
# Given a list of numbers, write a list comprehension that produces a list of only the positive numbers in that list.
#    >>> positives([-2, -1, 0, 1, 2])
#    [1, 2]


def positives(nums):
    return [x for x in nums if x > 0]


print(positives([-2, -1, 1, 2]))


# Selectively stringify nums:
# Given a list of numbers, write a list comprehension that produces a list of strings of each number that is divisible by 5.
#    >>> selective_stringify_nums([25, 91, 22, -7, -20])
#    ['25', '-20']


def selective_stringify_nums(nums):
    return [str(x) for x in nums if not x % 5]


print(selective_stringify_nums([25, 91, 22, -7, -20]))


# Words not 'the'
# Given a sentence, produce a list of the lengths of each word in the sentence, but only if the word is not 'the'.
#    >>> words_not_the('the quick brown fox jumps over the lazy dog')
#    [5, 5, 3, 5, 4, 4, 3]


def words_not_the(sentence):
    words = sentence.split(" ")
    return [len(x) for x in words if x != "the"]


print(words_not_the("the quick brown fox jumps over the lazy dog"))


# Vowels:
# Given a string representing a word, write a list comprehension that produces a list of all the vowels in that word.
#    >>> vowels('mathematics')
#    ['a', 'e', 'a', 'i']


def vowels(word):
    return [x for x in word if x in "aeiou"]


print(vowels("mathematics"))


# Vowels set:
# Given a string representing a word, write a set comprehension that produces a set of all the vowels in that word.
#    >>> vowels_set('mathematics')
#    set(['a', 'i', 'e'])


def vowels_set(word):
    return {x for x in word if x in "aeiou"}


print(vowels_set("mathematics"))


# Disemvowel:
# Given a sentence, return the sentence with all vowels removed.
#    >>> disemvowel('the quick brown fox jumps over the lazy dog')
#    'th qck brwn fx jmps vr th lzy dg'


def disemvowel(sentence):
    list = [x for x in sentence if x not in "aeiou"]
    s = ""
    for x in list:
        s += x
    return s


print(disemvowel("the quick brown fox jumps over the lazy dog"))


# Wiggle numbers:
# Given a list of number, return the list with all even numbers doubled, and all odd numbers turned negative.
#    >>> wiggle_numbers([72, 26, 79, 70, 20, 68, 43, -71, 71, -2])
#    [144, 52, -79, 140, 40, 136, -43, 71, -71, -4]


def wiggle_numbers(nums):
    return [x * 2 if not x % 2 else -x if x > 0 else x for x in nums]


print(wiggle_numbers([72, 26, 79, 70, 20, 68, 43, -71, 71, -2]))


def encrypt_lol(sentence):
    # """Encrypt lol:
    # Given a sentence, return the setence will all it's letter transposed by 1 in the alphabet, but only if the letter is a-y.
    #    >>> encrypt_lol('the quick brown fox jumps over the lazy dog')
    #    'uif rvjdl cspxo gpy kvnqt pwfs uif mbzy eph'
    # TODO
    abc = "abcdefghijklmnopqrstuvxyz"
    pass
