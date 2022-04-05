class dict2list:

    #givent dictionary
    dict1 = {'HuEX': [1, 3, 4], 'is': [7, 6], 'best' : [4, 5]}

    listvalues = list(dict1.values())
    listkeys = list(dict1.keys())

    for i in range(len(listkeys)):
        listkeys[i]=listkeys[i].extend(listvalues[i])


    print(listkeys)
