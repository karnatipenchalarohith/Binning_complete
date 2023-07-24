from split_bins_intermediate import splitbins_intermediate as splitbins_intermediate

def findSameAndDifferentParameters(binname,filenames):

    file_dict = []

    for i in range(len(filenames)):

        single_splits = splitbins_intermediate(filenames[i])

        file_dict.append(single_splits)

    #    print(var_name[i])

    #print(single_splits)
    #print(var_name)
    #print(file_dict)

    # Find all the keys that exist in at least one dictionary
    all_keys = set()
    for d in file_dict:
      all_keys |= set(d.keys())

    #print (all_keys)
    # Check if the values for the keys are the same in all dictionaries
    different_pairs = []
    for key in all_keys:
      values = [d.get(key) for d in file_dict]
      if not all(values[0] == v for v in values[1:]):
        different_pairs.append((key, values))

    #print(different_pairs)


    same_pairs = []
    for key in all_keys:
      values = [d.get(key) for d in file_dict]
      if  all(values[0] == v for v in values[1:]):
        same_pairs.append((key, values))


    #print(same_pairs)
    return(same_pairs)
