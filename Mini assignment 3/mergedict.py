class mergedict:




        # given dictionary 1
        dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

        # given dictionary 2
        dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

        # merging the dictionaries
        # copying values of dictionary 1
        dict3 = dict1.copy()

        #copying values of dictionary 2
        for key,value in dict2.items():
            dict3[key]=value

        print(dict3)