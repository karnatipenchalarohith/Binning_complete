# This is a sample Python script.

import re
import xlwt
from split_bins import splitbins as splitbins
from split_bins_intermediate import splitbins_intermediate as splitbins_intermediate

from segregate import segregate as segregate
from calculate_values import cal_values as cal_values
from extract_lmin_wmin import extractlminwmin as extractlminwmin
from Join_bins import join_bins as join_bins
from check_bins import check_bins_keys as check_bins_keys
from check_values_bins import check_bins_values as check_bins_values

from bins_analyse import bins_analyse as bins_analyse
from bins_same_length_width import bins_same_length_width as bins_same_length_width
from combine_modified_into_one import combine_modified_into_one as combine_modified_into_one
from findInputBinsLminLmaxWminWmax import findInputBinsLminLmaxWminWmax as findInputBinsLminLmaxWminWmax
from findPointModelCardsLengthWidth import findPointModelCardsLengthWidth as findPointModelCardsLengthWidth
from RebinMatchingBinsToPointModelCard import RebinMatchingBinsToPointModelCard as RebinMatchingBinsToPointModelCard
from RebinPointModelToBinnedEquation import RebinPointModelToBinnedEquation as RebinPointModelToBinnedEquation
from RebinSameParameterDifferentParameter import RebinSameParameterDifferentParameter as RebinSameParameterDifferentParameter

import pandas as pd

with open('modn.sp', 'r') as f:
    data = f.read()
found = re.findall(r'\d*\s?:\s?type', data, re.M | re.S)
print(found)

print(len(found))

pattern = '\d*\s?:\s?type\s?=[n,p]'

spt = re.split(pattern, data)
print(len(spt))
for founds in found:
    print(founds)

for spts in spt:
    print(spts)

print(spt[1])

with open('new.txt', 'w') as gg:
    gg.write(spt[1])
bin = []
for i in range(len(found)):
    print(i + 1)
    binname = "bin" + str(i + 1)
    print(binname)

    bin.append(binname)
print(bin)
print(bin[0])
print(bin[1])

[open(bin[i - 1] + '.txt', 'w').write(spt[i]) for i in range(1, len(bin) + 1)]

## all bins segregated


number_of_bins = len(found)

f = open("demofile2.xlsx", "a")

fields = "binned parameter"

first_row = 1

binned_all_parameters = []

all_splits = []

df1 = pd.DataFrame()

for i in range(number_of_bins):
    binname = "bin" + str(i + 1) + ".txt"
    binname_only="bin" + str(i + 1)
    single_splits = splitbins(binname)
    all_splits.append(single_splits)
    binned_parameters = segregate(single_splits)

    binned_all_parameters.append(binned_parameters)
    print(binned_parameters)
    print(all_splits)
    print(binned_all_parameters)
    (par_lmin_val, par_wmin_val, par_lmax_val, par_wmax_val) = extractlminwmin(single_splits)
    cal_l1w1 = cal_values(binned_parameters, single_splits, par_lmin_val, par_wmin_val)
    cal_l1w2 = cal_values(binned_parameters, single_splits, par_lmin_val, par_wmax_val)
    cal_l2w1 = cal_values(binned_parameters, single_splits, par_lmax_val, par_wmin_val)
    cal_l2w2 = cal_values(binned_parameters, single_splits, par_lmax_val, par_wmax_val)
    join_bins(binname_only,'_l1w1',cal_l1w1,binned_parameters,single_splits)
    join_bins(binname_only, '_l1w2', cal_l1w2, binned_parameters, single_splits)
    join_bins(binname_only, '_l2w1', cal_l2w1, binned_parameters, single_splits)
    join_bins(binname_only, '_l2w2', cal_l2w2, binned_parameters, single_splits)



for i in range(number_of_bins):
    binname = "bin" + str(i + 1)

#    single_splits = splitbins(binname)
    binname_split_l1w1 = binname + "__l1w1.txt"
    binname_split_l1w2 = binname + "__l1w2.txt"
    binname_split_l2w1 = binname + "__l2w1.txt"
    binname_split_l2w2 = binname + "__l2w2.txt"

    single_split_l1w1 = splitbins_intermediate(binname_split_l1w1)
    single_split_l1w2 = splitbins_intermediate(binname_split_l1w2)
    single_split_l2w1 = splitbins_intermediate(binname_split_l2w1)
    single_split_l2w2 = splitbins_intermediate(binname_split_l2w2)

    check_bins_keys(single_split_l1w1,single_split_l1w2,binname)
    check_bins_keys(single_split_l1w1, single_split_l2w1,binname)
    check_bins_keys(single_split_l1w1, single_split_l2w2,binname)
    check_bins_keys(single_split_l1w2, single_split_l2w1,binname)
    check_bins_keys(single_split_l1w2, single_split_l2w2,binname)
    check_bins_keys(single_split_l2w1, single_split_l2w2,binname)


    check_bins_values(single_split_l1w1,single_split_l1w2,binname)
    check_bins_values(single_split_l1w1, single_split_l2w1,binname)
    check_bins_values(single_split_l1w1, single_split_l2w2,binname)
    check_bins_values(single_split_l1w2, single_split_l2w1,binname)
    check_bins_values(single_split_l1w2, single_split_l2w2,binname)
    check_bins_values(single_split_l2w1, single_split_l2w2,binname)

bins_analyse()


final=bins_same_length_width()

print(final)

for key, value in final.items():
    print(value)


for key, value in final.items():
    combine_modified_into_one(value)



bins_array=findInputBinsLminLmaxWminWmax()

point_model_cards=findPointModelCardsLengthWidth()


print(bins_array)
print(point_model_cards)


matchBinsPointCards=RebinMatchingBinsToPointModelCard(bins_array,point_model_cards)


print(matchBinsPointCards)


FinalBinningEquation=RebinPointModelToBinnedEquation(matchBinsPointCards)

print(FinalBinningEquation)


RebinSameParameterDifferentParameter(matchBinsPointCards,FinalBinningEquation)




# combine_modified_into_one will create final single point model cards
# model cards are created upto this point

'''

#def join_bins(binnum,suffix,cal_l1w1,binned_parameters,all_parameters):


print(df1)


print(single_splits)
print(all_splits)
print(binned_all_parameters)






for count, ele in enumerate(binned_all_parameters):
    print(count+1)
    print(ele)



lmin_all = []
lmax_all = []
wmin_all = []
wmax_all = []



for count, ele in enumerate(all_splits):
    print(count)
    print(ele)
    print(len(ele))
    if "lmin" in ele:
        print(" lmin is there ")
        print("value=", ele["lmin"])
        lmin_all.append(ele["lmin"])
    if "lmax" in ele:
        print(" lmax is there ")
        print("value=", ele["lmax"])
        lmax_all.append(ele["lmax"])
    if "wmin" in ele:
        print(" wmin is there ")
        print("value=", ele["wmin"])
        wmin_all.append(ele["wmin"])
    if "wmax" in ele:
        print(" wmax is there ")
        print("value=", ele["wmax"])
        wmax_all.append(ele["wmax"])

print(lmin_all)
print(wmin_all)
print(lmax_all)
print(wmax_all)

print(len(lmin_all))
print(len(wmin_all))
print(len(lmax_all))
print(len(wmax_all))


print(number_of_bins)

print(single_splits)

print(binned_all_parameters)

# print(single_splits{1})
print(binned_all_parameters[1])

modified_param = []
for i in range(number_of_bins):
    binname = "bin" + str(i + 1) + ".txt"
    single_splits_fin = splitbins(binname)

    print("Bin Number" + " " + str(i + 1) + "the most")
    print(single_splits_fin)
    print(binned_all_parameters[i])
    (par_lmin_val, par_wmin_val, par_lmax_val, par_wmax_val) = extractlminwmin(single_splits_fin)


print(par_lmin_val, par_wmin_val, par_lmax_val, par_wmax_val)

binname_1 = "bin2.txt"

single_splits_fin_1 = splitbins(binname_1)
binned_parameters_1 = segregate(single_splits_fin_1)

(par_lmin_val, par_wmin_val, par_lmax_val, par_wmax_val) = extractlminwmin(single_splits_fin_1)

cal_l1w1 = cal_values(binned_parameters_1, single_splits_fin_1, par_lmin_val, par_wmin_val)
cal_l1w2 = cal_values(binned_parameters_1, single_splits_fin_1, par_lmin_val, par_wmax_val)
cal_l2w1 = cal_values(binned_parameters_1, single_splits_fin_1, par_lmax_val, par_wmin_val)
cal_l2w2 = cal_values(binned_parameters_1, single_splits_fin_1, par_lmax_val, par_wmax_val)

print(single_splits_fin_1)
print(binned_parameters_1)
print([par_lmin_val, par_wmin_val, par_lmax_val, par_wmax_val])
print(cal_l1w1)
print(cal_l1w2)
print(cal_l2w1)
print(cal_l2w2)

print(binned_parameters_1)
print(single_splits_fin_1)

print(len(single_splits_fin_1))
print(len(binned_parameters_1))
print(len(cal_l1w1))
print(len(cal_l1w2))

'''

'''
'''