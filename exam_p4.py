"""
What is the most interesting/funny/cool thing(s) about Python that you learned from this class or from somewhere else.

You can use code or a short paragraph to illustrate it.
"""


I think the coolest thing that I learned from this class about python is how there are so many ways to write the same code to complete the ultimate objective.
I like taking the creative liberty to think about how to solve a problem through various angles, as it challenges me to think about different ways of approaching a problem and the different steps required. I especially enjoy it when we learned to write one-line code to accomplish a task. For instance, I can write the following method in two ways to accomplish the same goals:

def returnvalue(word):
    d = {}
    for i in range(26):
        d[chr(97+i)] = 1+i
    newword = word.lower()
    value = 0
    for letter in newword:
        value += d[letter]
    return value

def returnvalue(word):
    return sum([ord(letter.lower())-96 for letter in word])