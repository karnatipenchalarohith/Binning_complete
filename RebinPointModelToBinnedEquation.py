


from split_bins_intermediate import splitbins_intermediate as splitbins_intermediate
from find_same_parameter import find_same_parameter as find_same_parameter

from pointParameterToBinnedEquation import pointParameterToBinnedEquation as pointParameterToBinnedEquation

def RebinPointModelToBinnedEquation(binned_allocated):
    #binned_allocated=[{'bin1.txt': ['Width_10.03_length_10.0_after_bins_joined.txt', 'Width_10.03_length_20.0_after_bins_joined.txt', 'Width_900.03_length_10.0_after_bins_joined.txt', 'Width_900.03_length_20.0_after_bins_joined.txt']}, {'bin2.txt': ['Width_10.03_length_1.2_after_bins_joined.txt', 'Width_10.03_length_10.0_after_bins_joined.txt', 'Width_900.03_length_1.2_after_bins_joined.txt', 'Width_900.03_length_10.0_after_bins_joined.txt']}, {'bin3.txt': ['Width_10.03_length_0.5_after_bins_joined.txt', 'Width_10.03_length_1.2_after_bins_joined.txt', 'Width_900.03_length_0.5_after_bins_joined.txt', 'Width_900.03_length_1.2_after_bins_joined.txt']}, {'bin4.txt': ['Width_10.03_length_0.18_after_bins_joined.txt', 'Width_10.03_length_0.5_after_bins_joined.txt', 'Width_900.03_length_0.18_after_bins_joined.txt', 'Width_900.03_length_0.5_after_bins_joined.txt']}, {'bin5.txt': ['Width_1.23_length_10.0_after_bins_joined.txt', 'Width_1.23_length_20.0_after_bins_joined.txt', 'Width_10.03_length_10.0_after_bins_joined.txt', 'Width_10.03_length_20.0_after_bins_joined.txt']}, {'bin6.txt': ['Width_1.23_length_1.2_after_bins_joined.txt', 'Width_1.23_length_10.0_after_bins_joined.txt', 'Width_10.03_length_1.2_after_bins_joined.txt', 'Width_10.03_length_10.0_after_bins_joined.txt']}, {'bin7.txt': ['Width_1.23_length_0.5_after_bins_joined.txt', 'Width_1.23_length_1.2_after_bins_joined.txt', 'Width_10.03_length_0.5_after_bins_joined.txt', 'Width_10.03_length_1.2_after_bins_joined.txt']}, {'bin8.txt': ['Width_1.23_length_0.18_after_bins_joined.txt', 'Width_1.23_length_0.5_after_bins_joined.txt', 'Width_10.03_length_0.18_after_bins_joined.txt', 'Width_10.03_length_0.5_after_bins_joined.txt']}, {'bin9.txt': ['Width_0.53_length_10.0_after_bins_joined.txt', 'Width_0.53_length_20.0_after_bins_joined.txt', 'Width_1.23_length_10.0_after_bins_joined.txt', 'Width_1.23_length_20.0_after_bins_joined.txt']}, {'bin10.txt': ['Width_0.53_length_1.2_after_bins_joined.txt', 'Width_0.53_length_10.0_after_bins_joined.txt', 'Width_1.23_length_1.2_after_bins_joined.txt', 'Width_1.23_length_10.0_after_bins_joined.txt']}, {'bin11.txt': ['Width_0.53_length_0.5_after_bins_joined.txt', 'Width_0.53_length_1.2_after_bins_joined.txt', 'Width_1.23_length_0.5_after_bins_joined.txt', 'Width_1.23_length_1.2_after_bins_joined.txt']}, {'bin12.txt': ['Width_0.53_length_0.18_after_bins_joined.txt', 'Width_0.53_length_0.5_after_bins_joined.txt', 'Width_1.23_length_0.18_after_bins_joined.txt', 'Width_1.23_length_0.5_after_bins_joined.txt']}, {'bin13.txt': ['Width_0.22_length_10.0_after_bins_joined.txt', 'Width_0.22_length_20.0_after_bins_joined.txt', 'Width_0.53_length_10.0_after_bins_joined.txt', 'Width_0.53_length_20.0_after_bins_joined.txt']}, {'bin14.txt': ['Width_0.22_length_1.2_after_bins_joined.txt', 'Width_0.22_length_10.0_after_bins_joined.txt', 'Width_0.53_length_1.2_after_bins_joined.txt', 'Width_0.53_length_10.0_after_bins_joined.txt']}, {'bin15.txt': ['Width_0.22_length_0.5_after_bins_joined.txt', 'Width_0.22_length_1.2_after_bins_joined.txt', 'Width_0.53_length_0.5_after_bins_joined.txt', 'Width_0.53_length_1.2_after_bins_joined.txt']}, {'bin16.txt': ['Width_0.22_length_0.18_after_bins_joined.txt', 'Width_0.22_length_0.5_after_bins_joined.txt', 'Width_0.53_length_0.18_after_bins_joined.txt', 'Width_0.53_length_0.5_after_bins_joined.txt']}]
    bins_different_all=[]


    for item in binned_allocated:
        print(item)
        print(item)
        for k,v in item.items():
            print(k)
            print(v)
            bins_different=find_same_parameter(k,v)
            bins_different_all.append(bins_different)

    print(bins_different_all)

    binAndBinnedEquation_all=[]

    for item in bins_different_all:
        print(item)
        print(item[0])
        print(item[1])
        binned_eq=pointParameterToBinnedEquation(item[1])
        binAndBinnedEquation=[item[0],binned_eq]
        binAndBinnedEquation_all.append(binAndBinnedEquation)


    print(binAndBinnedEquation_all)

    print("Hiii")
    empt_list_all=[]
    for item in binAndBinnedEquation_all:
        empt_list=[]
    #    print(item)
        empt_list.append(item[0])
        new_lit_all=[]
        new_lit=[]
        for item in item[1]:
    #        print(item[0])
    #        print(item[1].tolist())
            new_lit=[item[0],item[1].tolist()]
            new_lit_all.append(new_lit)
        empt_list.append(new_lit_all)
        empt_list_all.append(empt_list)

    print(empt_list)
    print(empt_list_all)
    return(empt_list_all)

#    for it in item:
#        print (it)
#        print (it)

'''        
    print(item[1])
    print(item[1][0])
    print(item[1][1])
    print(item[1][0][1])
    for item in item[1][0][1]:
        print(item)


'''



'''
filenames=['Width_10.03_length_10.0_after_bins_joined.txt', 'Width_10.03_length_20.0_after_bins_joined.txt', 'Width_900.03_length_10.0_after_bins_joined.txt', 'Width_900.03_length_20.0_after_bins_joined.txt']
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



for pair in different_pairs:
    key = pair[0]
    print(key)
    values = pair[1]
    print(values)
    for value in values:
        print(key, value)

print(different_pairs)
'''




'''



# Check if the values for the keys are the same in all dictionaries
different_pairs = []
for key in all_keys:
    for d in file_dict:
        values=[d.get(key)]
        for v in values[1:]:
            if not all(values[0] == v:
                different_pairs.append((key, values))
            

  values = [d.get(key) for d in file_dict]
  if not all(values[0] == v for v in values[1:]):
    different_pairs.append((key, values))

'''

