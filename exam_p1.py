import string
def returnvalue(word):
    # d = {}
    # for i in range(26):
    #     d[chr(97+i)] = 1+i
    # newword = word.lower()
    # value = 0
    # for letter in newword:
    #     value += d[letter]
    # return value
    return sum([ord(letter.lower())-96 for letter in word])

def get_name_list():
    namelist = []
    roster = open("roster.txt", "r", encoding="utf8")
    for line in roster:
        a = line.lower()
        b = a.split()
        namelist.append(b[0])
    return namelist

def mostvaluable(name_list):
    end = 0
    d = {}
    for person in name_list:
        a = returnvalue(person)
        d[person] = a
        if a > end:
            end = a
            endperson = person
    return endperson, end

def get_words():
    wordlist = []
    words = open("positive-words.txt", "r", encoding="utf8")
    for line in words:
        wordlist.append(line.split()[0])
    return wordlist

def get_same_value_words(word_list, value):
    same_value = []
    for word in word_list:
        z = returnvalue(word)
        if z == value:
            same_value.append(word)
    return same_value

def main():
    v = returnvalue('Angela')
    # print(v)
    l = get_name_list()
    # print(l)
    m, p = mostvaluable(l)
    print('the most valuable is:', m, ", with a value of:", p)
    poswords = get_words()
    # print(poswords)
    # a = ['abc', 'basfd', 'csadf', 'Angela']
    # print(get_same_value_words(a, 40))
    print('The positive words that have the same value as Angela are:',get_same_value_words(poswords, v))


if __name__ == '__main__':
    main()
