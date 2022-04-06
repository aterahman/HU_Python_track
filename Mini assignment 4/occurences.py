class occurences:

    list1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

    #expression to find occurences of a in the list using maps,lambda and count
    occ = list(map(lambda x: x.lower().count('a') ,list1))

    print(occ)
