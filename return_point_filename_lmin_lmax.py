
from split_bins_intermediate import splitbins_intermediate as splitbins_intermediate

def return_point_filename_lmin_lmax(filename):
    single_splits = splitbins_intermediate(filename)
    new_dic = {'point_filename':filename,'length': single_splits.get('length'), 'width': single_splits.get('width')}

    return new_dic


    words = ['lmin', 'lmax', 'wmin', 'wmax']


'''

filename='Width_0.22_length_0.5_after_bins_joined.txt'

single_splits = splitbins_intermediate(filename)

print(single_splits)

print(single_splits.get('length'))
print(single_splits.get('width'))

new_dic={filename:{'length':single_splits.get('length'),'width':single_splits.get('width')}}

print(new_dic)
'''
