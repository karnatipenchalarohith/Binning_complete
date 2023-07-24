
from split_bins_intermediate import splitbins_intermediate as splitbins_intermediate


def find_same_parameter(binname,filenames):
#    filenames=['Width_10.03_length_10.0_after_bins_joined.txt', 'Width_10.03_length_20.0_after_bins_joined.txt', 'Width_900.03_length_10.0_after_bins_joined.txt', 'Width_900.03_length_20.0_after_bins_joined.txt']
    var_name=[]

    for i in range(len(filenames)):
        print(filenames[i])
        print(i)
        var="var"+str(i)
        var_name.append(var)


    print(var_name)

    file_dict = []

    for i in range(len(filenames)):

        single_splits = splitbins_intermediate(filenames[i])
        var_name[i]=single_splits
        file_dict.append(single_splits)

    #    print(var_name[i])

    #print(single_splits)
    #print(var_name)
    print(file_dict)

    # Find all the keys that exist in at least one dictionary
    all_keys = set()
    for d in file_dict:
      all_keys |= set(d.keys())

    print (all_keys)
    # Check if the values for the keys are the same in all dictionaries
    different_pairs = []
    for key in all_keys:
      values = [d.get(key) for d in file_dict]
      if not all(values[0] == v for v in values[1:]):
        different_pairs.append((key, values))

    print(different_pairs)
    final_diff_pairs=[binname,different_pairs]
    return(final_diff_pairs)


'''
    for pair in different_pairs:
        key = pair[0]
        print(key)
        values = pair[1]
        print(values)
        for value in values:
            print(key, value)

    print(different_pairs)
'''