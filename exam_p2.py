def process_file(file_name):
    """
    Given a file name, returns a list of lists [name, gender, births]
    HINT: https://stackoverflow.com/a/35340988/941742

    :param file_name: a string
    :return: a list of lists, [[name1, gender1, births1], [name2, gender2, births2]...]

    Example:
    process_file('yob1880.txt')
        will return
    [["Mary","F",7065], ["Anna","F",2604],...]

    """
    new_list = []
    fp = open(file_name, "r")
    for line in fp:
        a = line.split(',')
        new_list.append(a)
    return new_list

def total_births(year):
    """

    :param year: an integer, between 1880 and 2010
    :return: an integer, the total births of all the babies in that year
    """
    text = 'babynames/yob' + str(year) + '.txt'
    a = process_file(text)
    return len(a)

def proportion(name, gender, year):
    """

    :param name: a string, first name
    :param gender: a string, "F" or "M"
    :param year: an integer, between 1880 and 2010
    :return: a floating number, the proportion of babies with the given name to total births in given year
    """
    num = 0
    for baby in process_file('babynames/yob' + str(year) + '.txt'):
        if baby[0] == name and baby[1] == gender:
            num += 1
    return num/total_births(year)

def highest_year(name, gender):
    """

    :param name: a string
    :param gender: a string, "F" or "M"
    :return: an integer, the year when the given name has the highest proportion over the years (among all the proportions of the same name in different years)
    """
    highyear = 0
    high = 0
    for i in range(1880, 2011):
        p = proportion(name, gender, i)
        if p > high:
            high = p
            highyear = i
    return highyear

def main():
    a = process_file('babynames/yob1880.txt')
    # print(a)
    print(total_births(1880))
    print(proportion('Angela', 'F', 1880))
    print(highest_year('Angela', 'F'))

if __name__ == '__main__':
    main()
