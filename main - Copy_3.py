# This is a sample Python script.

import re
import xlwt
from split_bins import splitbins as splitbins
from segregate import segregate as segregate
from calculate_values import cal_values as cal_values
from extract_lmin_wmin import extractlminwmin as extractlminwmin

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
    single_splits = splitbins(binname)
    all_splits.append(single_splits)
    binned_parameters = segregate(single_splits)
    binned_all_parameters.append(binned_parameters)
    print(binned_parameters)
    print(all_splits)
    print(binned_all_parameters)


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