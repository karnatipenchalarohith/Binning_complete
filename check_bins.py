


def check_bins_keys(dict1,dict2,binname):
    dict1_keys = dict1.keys()
    dict2_keys = dict2.keys()

    print(binname)
    print("\n")

    print(dict1)
    print("\n")

    print(dict2)
    print("\n")

    dict1_keys_set = set(dict1_keys)
    dict2_keys_set = set(dict2_keys)

    keys_in_dict1_not_in_dict2 = dict1_keys_set.difference(dict2_keys_set)
    keys_in_dict2_not_in_dict1 = dict2_keys_set.difference(dict1_keys_set)

    print(f"Keys in dict1 but not in dict2: {keys_in_dict1_not_in_dict2}")
    print(f"Keys in dict2 but not in dict1: {keys_in_dict2_not_in_dict1}")