import os
from split_bins_intermediate import splitbins_intermediate as splitbins_intermediate


#path = r'C:\Users\rkar\PycharmProjects\Binning'



current_location=os.getcwd()

print(current_location)

files = []
for i in os.listdir(current_location):
    if os.path.isfile(os.path.join(current_location ,i)) and 'ZZ' in i:
        files.append(i)

print(files)
point_model_final_all=[]

for item in files:
    print(item)
    binnumb = item.rstrip('_after_bins_joined.txt')
    binnumb_fin = binnumb.lstrip('ZZ_')
    print(binnumb_fin)
    point_model_final=str(binnumb_fin) + '_point_modelcard.scs'
    print(point_model_final)
    point_model_final_all.append(point_model_final)




'''
with open(new_filename, "w") as f:
    f.write("simulator lang=spectre insensitive=yes \n")
    f.write("model modn bsim4  { ")
    f.write("\n")


single_splits = splitbins_intermediate(filename)
#print(single_splits)
count=0
with open(new_filename, "a+") as f:
    f.write("    "  + "0 :" + "  " + "type=n")
    f.write("\n")
    for key, value in single_splits.items():
        if count == 0 or count % 3 == 0:
            f.write("+ ")

        f.write(f"{key}={value}")
        count += 1
        if count % 3 == 0:
            f.write("\n")
        else:
            f.write("  ")

    f.write("\n")
    f.write("}")

'''
print(files)

print(point_model_final_all)

for item1,item2 in zip(files,point_model_final_all):
    print(item1)
    print(item2)

    with open(item2, "w") as f:
        f.write("simulator lang=spectre insensitive=yes \n")
        f.write("model modn bsim4  { ")
        f.write("\n")

    single_splits = splitbins_intermediate(item1)
    # print(single_splits)
    count = 0
    with open(item2, "a+") as f:
        f.write("    " + "0 :" + "  " + "type=n")
        f.write("\n")
        for key, value in single_splits.items():
            if count == 0 or count % 3 == 0:
                f.write("+ ")

            f.write(f"{key}={value}")
            count += 1
            if count % 3 == 0:
                f.write("\n")
            else:
                f.write("  ")

        f.write("\n")
        f.write("}")

