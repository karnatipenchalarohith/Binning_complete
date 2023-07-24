import re

def cal_values(binning_parameters,all_parameters,lmin,wmin):
    l = lmin
    w = wmin
    d={}
    for par in binning_parameters:
        l_par1 = 'l' + par
        w_par1 = 'w' + par
        p_par1 = 'p' + par

        par_val=0
        par_val_l=0
        par_val_w=0
        par_val_p=0

        for key, value in all_parameters.items():
            # print(key)
            if par == key:
                par_val = value
                print(par_val)

            if l_par1 == key:
                print(type(value))
                print(type(l))
                par_val_l = float(value) / float(l)
                print(par_val_l)

            if w_par1 == key:
                print(type(value))
                print(type(l))
                par_val_w = float(value) / float(w)
                print("w-type")
                print(par_val_w)

            if p_par1 == key:
                print(type(value))
                print(type(l))
                par_val_p = float(value) / (float(w) * float(l))
                print("p-type")
                print(par_val_p)

            final_par_val = float(par_val) + par_val_l + par_val_w + par_val_p
            d["final_{0}".format(par)] = final_par_val


   # print(d)
    return(d)


