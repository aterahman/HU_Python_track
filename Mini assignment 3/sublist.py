class sublist:

    #given list
    list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

    #given sublist
    sublist = ["h", "i", "j"]

    # adding the given sublist to the given list
    list1[2][1][2]= list1[2][1][2] + sublist

    print(list1)