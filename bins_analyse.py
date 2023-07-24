
from split_bins_intermediate import splitbins_intermediate as splitbins_intermediate
def bins_analyse():

    suffix_l1w1 = "__l1w1"
    suffix_l1w2 = "__l1w2"
    suffix_l2w1 = "__l2w1"
    suffix_l2w2 = "__l2w2"

    for i in range(16):
        binname = "bin" + str(i + 1)
        binname_split_l1w1=binname + suffix_l1w1 + ".txt"

        print(binname + suffix_l1w1)
        single_split_l1w1 = splitbins_intermediate(binname_split_l1w1)
        print(single_split_l1w1)

        del single_split_l1w1['lmax']
        del single_split_l1w1['wmax']

        print(single_split_l1w1)

        filename = binname + '_' + suffix_l1w1 + '_modified.txt'
        with open(filename, "w") as f:
            count = 0

            for key, value in single_split_l1w1.items():
                #            f.write(f"+ ")
                f.write(f"{key}= {value}")
                count += 1

                if count % 3 == 0:
                    f.write("\n")
                else:
                    f.write("  ")


    # L1W2

        binname = "bin" + str(i + 1)
        binname_split_l1w2=binname + suffix_l1w2 + ".txt"

        print(binname + suffix_l1w2)
        single_split_l1w2 = splitbins_intermediate(binname_split_l1w2)
        print(single_split_l1w2)

        del single_split_l1w2['lmax']
        del single_split_l1w2['wmin']

        print(single_split_l1w2)

        filename = binname + '_' + suffix_l1w2 + '_modified.txt'
        with open(filename, "w") as f:
            count = 0

            for key, value in single_split_l1w2.items():
                #            f.write(f"+ ")
                f.write(f"{key}= {value}")
                count += 1

                if count % 3 == 0:
                    f.write("\n")
                else:
                    f.write("  ")


    # L2W1

        binname = "bin" + str(i + 1)
        binname_split_l2w1=binname + suffix_l2w1 + ".txt"

        print(binname + suffix_l2w1)
        single_split_l2w1 = splitbins_intermediate(binname_split_l2w1)
        print(single_split_l2w1)

        del single_split_l2w1['lmin']
        del single_split_l2w1['wmax']

        print(single_split_l2w1)

        filename = binname + '_' + suffix_l2w1 + '_modified.txt'
        with open(filename, "w") as f:
            count = 0

            for key, value in single_split_l2w1.items():
                #            f.write(f"+ ")
                f.write(f"{key}= {value}")
                count += 1

                if count % 3 == 0:
                    f.write("\n")
                else:
                    f.write("  ")


    # L2W2

        binname = "bin" + str(i + 1)
        binname_split_l2w2=binname + suffix_l2w2 + ".txt"

        print(binname + suffix_l2w2)
        single_split_l2w2 = splitbins_intermediate(binname_split_l2w2)
        print(single_split_l2w2)

        del single_split_l2w2['lmin']
        del single_split_l2w2['wmin']

        print(single_split_l2w2)

        filename = binname + '_' + suffix_l2w2 + '_modified.txt'
        with open(filename, "w") as f:
            count = 0

            for key, value in single_split_l2w2.items():
                #            f.write(f"+ ")
                f.write(f"{key}= {value}")
                count += 1

                if count % 3 == 0:
                    f.write("\n")
                else:
                    f.write("  ")






