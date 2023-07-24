
from statistics import mean




from split_bins_intermediate import splitbins_intermediate as splitbins_intermediate

def combine_modified_into_one(l):

#    l=['bin10___l1w1_modified.txt','bin11___l2w1_modified.txt']

    number_of_bins_same=len(l)

    if number_of_bins_same==2:
        single_split_file1 = splitbins_intermediate(l[0])
        single_split_file2 = splitbins_intermediate(l[1])
        if len(single_split_file1) != len(single_split_file2):
            print("something is wrong")

        dictionaryList=[single_split_file1,single_split_file2]


    elif number_of_bins_same==3:
        single_split_file1 = splitbins_intermediate(l[0])
        single_split_file2 = splitbins_intermediate(l[1])
        single_split_file3 = splitbins_intermediate(l[2])
        if len(single_split_file1) != len(single_split_file2):
            print("something is wrong")

        if len(single_split_file2) != len(single_split_file3):
            print("something is wrong")

        dictionaryList=[single_split_file1,single_split_file2,single_split_file3]




    elif number_of_bins_same==4:
        single_split_file1 = splitbins_intermediate(l[0])
        single_split_file2 = splitbins_intermediate(l[1])
        single_split_file3 = splitbins_intermediate(l[2])
        single_split_file4 = splitbins_intermediate(l[3])

        if len(single_split_file1) != len(single_split_file2):
            print("something is wrong")

        if len(single_split_file2) != len(single_split_file3):
            print("something is wrong")

        if len(single_split_file3) != len(single_split_file4):
            print("something is wrong")

        dictionaryList=[single_split_file1,single_split_file2,single_split_file3,single_split_file4]


    else :
        single_split_file1 = splitbins_intermediate(l[0])

        dictionaryList = [single_split_file1]


    for j in dictionaryList:

        for i in list(j):
        #    print(i)
            if i == 'lmin':
                j.update({'length': j.pop('lmin')})
            if i == 'lmax':
                j.update({'length': j.pop('lmax')})
            if i == 'wmin':
                j.update({'width': j.pop('wmin')})
            if i == 'wmax':
                j.update({'width': j.pop('wmax')})
    new = {}


#    if set(single_split_file1.keys()) == set(single_split_file2.keys()) or set(single_split_file1.keys()):

    if set(single_split_file1.keys())  :
        for key in single_split_file1.keys():
            print(key)
            new[key] = mean([float(d[key]) for d in dictionaryList])
    #        for d in dictionaryList:
    #            print(d)

    print(single_split_file1)
#    print(single_split_file2)
    print(new)

    combined_file_name="ZZ_Width_" + str(round(new['width']*1e6,2)) + "_length_" + str(round(new['length']*1e6,2)) + "_after_bins_joined.txt"

    with open(combined_file_name, "w") as f:
        count = 0
        for key, value in new.items():
            #            f.write(f"+ ")
            f.write(f"{key}= {value}")
            count += 1

            if count % 3 == 0:
                f.write("\n")
            else:
                f.write("  ")








    '''
    d = []
    for x in range(len(l)):
        print(x)
        print("string{0}".format(x))
    #    d["string{0}".format(x)] = splitbins_intermediate(l[x])
    
    
    '''
'''
    print(single_split_file1)
    print(single_split_file2)





    print(len(single_split_file1))
    print(len(single_split_file2))


    if len(single_split_file1) != len(single_split_file1) :
        print("something is wrong")

'''


    #dictionaryList = [single_split_file1,single_split_file2]




'''
    print(single_split_file1)
    print(single_split_file2)





    print(len(single_split_file1))
    print(len(single_split_file2))


    if set(single_split_file1.keys()) != set(single_split_file2.keys()):
        print("Parameters don't match")



    diff = set(single_split_file1) - set(single_split_file2)

    for key in single_split_file1.keys():
        if not key in single_split_file2.keys():
            print(key)



'''

    #dictionaryList = [single_split_file1,single_split_file2]


'''
    files=[single_split_file1,single_split_file2,new]

    fname=['first','second_','combined_']
    j=0
    for i in files:
        filename = fname[j] + '_check_bins_after_join.txt'
        print(i)
        print(filename)
        j+=1
        with open(filename, "w") as f:
            count = 0

            for key, value in i.items():
                #            f.write(f"+ ")
                f.write(f"{key}= {value}")
                count += 1

                if count % 3 == 0:
                    f.write("\n")
                else:
                    f.write("  ")
'''


'''
        for i in list(j[1]):
            if i == 'lmin':
                j[1].update({'length': j[1].pop('lmin')})
            if i == 'lmax':
                j[1].update({'length': j[1].pop('lmax')})
            if i ==  'wmin':
                j[1].update({'width': j[1].pop('wmin')})
            if i ==  'wmax':
                j[1].update({'width': j[1].pop('wmax')})
    
'''

'''
    dictionaryList = [single_split_file1,single_split_file2]
    
    
    new = {}
    
    for key in single_split_file1.keys():
        new[key] = mean([d[key] for d in dictionaryList ])
    print(new)
    
'''












