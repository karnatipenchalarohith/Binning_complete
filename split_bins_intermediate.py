import re

def splitbins_intermediate(filename):

    #filename="bin2.txt"
#    print(filename)
    filename2="model3.dat"


    f = open(str(filename))
    lines = f.readlines()
    #print(lines)
    f.close()

    f = open(filename2, 'w')
    for line in lines:
        f.write(line[0:])
    f.close()

    with open('model3.dat', 'r') as f:
        data = f.read()

#    if __name__=="__main__":
#        with open('model2.dat', 'r') as f:
#            data = f.read()

    #reExp = re.compile("=", flags=re.S)
    reExp = re.compile("\s*([+-.\w]+)\s*=\s*([+-.\w]+)\s*", flags=re.S)

    #reExp = re.compile("\s*(\w+)\s*=\s*([+-.\w]+)\s*", flags=re.S)

    extLst = dict(reExp.findall(data))

#    print(extLst)

#    print(extLst["lmin"])
#    print(extLst["lmax"])

#    print(extLst["wmin"])
#    print(extLst["wmax"])
    return extLst
