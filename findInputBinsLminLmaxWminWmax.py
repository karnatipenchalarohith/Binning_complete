import os
import re
import itertools as it

from collections import defaultdict


from search_filename import find_filename as find_filename
from split_bins import splitbins as splitbins
from remove_dict_except import remove_dict_except as remove_dict_except

#find bins with lmin lmax


from segregate import segregate as segregate

def findInputBinsLminLmaxWminWmax():
    file1='bin1.txt'

    path = r'C:\Users\rkar\PycharmProjects\Binning'

    file=find_filename(file1,path)

    print(file)

    words = ['lmin', 'lmax', 'wmin', 'wmax']
    your_blacklisted_set = ['lmin', 'lmax', 'wmin', 'wmax']

    final_list=[]


    '''
    with open(file) as f:
        for i, line in enumerate(f.readlines()):
            for word in filter(lambda w: w in line, words):
                print(f'{path}, {i + 1}, {word}, {line.strip()}')
                print(f' {line.strip()}')
                reExp = re.compile("\s*([+-.\w]+)\s*=\s*([+-.\w]+)\s*", flags=re.S)
                extLst = dict(reExp.findall(line.strip()))
                print(extLst)
                for key in list(extLst.keys()):
                    if key not in your_blacklisted_set:
                        extLst.pop(key, None)
    
                    print(key)
    #               print(value)
    
    
                all_list = [path, extLst]
                final_list.append(all_list)
    
    
    
    print(all_list)
    print(final_list)
    '''

    '''
    for el in final_list:
        print(el[0])
        print(el[1])
        for key in list(el[1].keys()):
            if key not in your_blacklisted_set:
                el[1].pop(key, None)
    
    '''

    #print(final_list)




    number_of_bins = 16
    all_splits=[]
    binned_parameters=[]
    binned_all_parameters=[]

    all_dict_append=[]
    all_dict_append2=[]

    for i in range(number_of_bins):
        binname = "bin" + str(i + 1) + ".txt"
        binname_only="bin" + str(i + 1)
        single_splits = splitbins(binname)
        all_splits.append(single_splits)
        lmin_lmax_list=remove_dict_except(single_splits)
        new_df2={'binname':binname}
        new_df2.update(lmin_lmax_list)
        new_df={binname:lmin_lmax_list}
        all_dict_append.append(new_df)
        all_dict_append2.append(new_df2)

    print(single_splits)
    print(lmin_lmax_list)
    print(all_dict_append)

    print(all_dict_append2)
    return(all_dict_append2)

