
from split_bins_intermediate import splitbins_intermediate as splitbins_intermediate
from sklearn import linear_model
import pandas as pd
import numpy as np
import scipy.linalg



def pointParameterToBinnedEquation(param_change):

#    filenames=['Width_10.03_length_10.0_after_bins_joined.txt', 'Width_10.03_length_20.0_after_bins_joined.txt', 'Width_900.03_length_10.0_after_bins_joined.txt', 'Width_900.03_length_20.0_after_bins_joined.txt']


#    param_change=[('voff', ['-0.13055048136967845', '-0.1305493606979063', '-0.130551120065', '-0.13055']), ('ku0', ['0.08929209162911265', '0.07954134387238285', '0.020772164482339473', '0.010774942167527748']), ('ua', ['-1.1116365917804089e-09', '-1.1118928574277168e-09', '-1.1115437900000002e-09', '-1.1118e-09']), ('width', ['1.003e-05', '1.003e-05', '0.00090003', '0.00090003']), ('ua1', ['2.3411901801889333e-09', '2.3415048227318047e-09', '2.3412212865e-09', '2.3415359e-09']), ('at', ['117864.18737158524', '117847.68173479561', '117865.01629999999', '117848.51']), ('length', ['1e-05', '2e-05', '1e-05', '2e-05']), ('k2', ['0.04434202028619442', '0.044341759241276174', '0.044342261364999996', '0.044342']), ('ub1', ['-4.429864031827891e-18', '-4.4298961868893316e-18', '-4.42984240025e-18', '-4.4298745e-18']), ('a0', ['1.0723618552299352', '1.0723923030907279', '1.07236956325', '1.0724']), ('ags', ['0.5006321372273181', '0.5007252424576272', '0.500626879', '0.50072']), ('keta', ['-0.05135412310209372', '-0.05137706195214357', '-0.051352062899999995', '-0.051375']), ('pdiblc2', ['0.0009745268207851446', '0.0009749964909621136', '0.00097453036', '0.000975']), ('cit', ['0.000828888793559322', '0.0008285106103838485', '0.00082891817', '0.00082854']), ('ub', ['2.326183780472333e-18', '2.326397946759721e-18', '2.3260858825000004e-18', '2.3263e-18']), ('pclm', ['0.718915940332004', '0.7188776969890329', '0.7189082360000001', '0.71887']), ('kvth0we', ['0.0034927660043377368', '0.003492714805333998', '0.0034927647175', '0.0034927135']), ('vth0', ['0.4395296895657278', '0.43952810873379855', '0.43953157858999997', '0.43953']), ('uc', ['1.9170908257659522e-10', '1.9168742023429712e-10', '1.9169165525e-10', '1.9167e-10']), ('kvth0', ['0.21784347179122632', '0.2185927240344965', '0.0014388097953023792', '0.0019415874804906503']), ('nfactor', ['0.9496504691908774', '0.9496561478215354', '0.9497143261500001', '0.94972']), ('kt2', ['-0.05519171839515753', '-0.05519156742372881', '-0.05519169165', '-0.055191541']), ('kt1', ['-0.24611092507833998', '-0.24611949793120638', '-0.24610728945', '-0.24611586']), ('vsat', ['73329.11977108175', '73329.48742871385', '73328.63227999999', '73329.0']), ('u0', ['0.030527531276704885', '0.03052545349451645', '0.030528077270000002', '0.030526']), ('ute', ['-1.811939560749003', '-1.8117251033399802', '-1.8119056685000001', '-1.8116912']), ('eta0', ['0.22767273185540876', '0.22769849930707875', '0.2276842375', '0.22771']), ('uc1', ['-8.06852788277667e-11', '-8.070698183250249e-11', '-8.067825900000001e-11', '-8.0699954e-11'])]




    for item in param_change:
        print(item)
        print(item[0])
        print(item[1])
        print(item[1][0])
        print(item[1][3])
        if item[0]=='length':
            leng=item[1]

        if item[0]=='width':
            weng=item[1]

        if item[0]=='kvth0':
            uc1=item[1]

    print(leng,weng, uc1)



    leng_rec = []
    for x in leng:
        leng_rec.append(1/float(x))

    weng_rec = []
    for x in weng:
        weng_rec.append(1 / float(x))

    lengweng_rec = []
    for x,y in zip(leng,weng):
        lengweng_rec.append(1 / (float(x)*float(y)))


    print(leng_rec,weng_rec, lengweng_rec)

    '''
    X = df_id_vg_0[['Area', 'Perimeter']]
    y = df_id_vg_0['C']
    
    
    
    
    X = df_id_vg_0[['Area', 'Perimeter']]
    y = df_id_vg_0['C']
    '''

    X=leng_rec


    uc1_param = []
    for x in uc1:
        uc1_param.append(float(x))



    df=pd.DataFrame([leng_rec,weng_rec, lengweng_rec,uc1_param])

    df.columns = ["length", "width", "p_term", "uc1_term"]


    X = df[['length', 'width','p_term']]
    y = df['uc1_term']

    #y=uc1_param




    print(X)

    print(y)





    '''
    regr = linear_model.LinearRegression()
    regr.fit(X, y)
    
    print(regr.coef_)
    
    equation = "2x + 3y + 1"
    
    # split the equation into its individual terms
    terms = equation.split(" + ")
    
    # create a list of the coefficients
    coefficients = []
    for term in terms:
        if "x" in term:
            coefficient = term.split("x")[0]
        elif "y" in term:
            coefficient = term.split("y")[0]
        else:
            coefficient = term
        coefficients.append(int(coefficient))
    
    
    print(coefficients)
    # solve the linear equation
    #x, y = np.solve(coefficients)
    
    #print(f"x = {x}, y = {y}")
    
    x, y = scipy.linalg.solve(coefficients,[5,7])
    
    print(f"x = {x}, y = {y}")
    '''


    A = np.array([[1,99999.99999999999,99700.89730807577,9970089730.807575], [1,49999.99999999999,99700.89730807577,4985044865.403788], [1,99999.99999999999,1111.0740753086009,111107407.53086007], [1,49999.99999999999,1111.0740753086009,55553703.76543003]])

    B = np.array([0.217843471791226,0.218592724034496,0.00143880979530237,0.00194158748049065])


    X2 = np.linalg.solve(A,B)


    print(X2)

    for item in X2:
        print(item)






    param_change_new=[]


    for item in param_change:
        print(item)
        print(item[0])
        print(item[1])
        it_all = []


        for it in item[1]:
            it_=float(it)
            it_all.append(it_)
            print(it_all)


        new_change=(item[0],it_all )
        param_change_new.append(new_change )


    print(param_change)
    print(param_change_new)



    for item in param_change_new:
        print(item)
        print(item[0])
        print(item[1])
        print(item[1][0])
        print(item[1][3])
        if item[0]=='length':
            leng=item[1]

        if item[0]=='width':
            weng=item[1]



    leng_rec = []
    for x in leng:
        leng_rec.append(1/float(x))

    weng_rec = []
    for x in weng:
        weng_rec.append(1 / float(x))

    lengweng_rec = []
    for x,y in zip(leng,weng):
        lengweng_rec.append(1 / (float(x)*float(y)))


    print(leng_rec,weng_rec,lengweng_rec)



    prim_term=[]
    for i in range(len(leng_rec)):
        prim_term.append(1)

    print(leng_rec)
    print(weng_rec)
    print(lengweng_rec)
    print(prim_term)

    grp_list=[]

    comp_grp_list=[]

    for i in range(len(leng_rec)):
        print(i)
        grp_list=[prim_term[i], leng_rec[i], weng_rec[i], lengweng_rec[i] ]
        comp_grp_list.append(grp_list)



    print(comp_grp_list)


    for item in comp_grp_list:
        print(item)

    final_binned_parameter=[]
    final_binned_parameter_all=[]
    for item in param_change_new:
        print(item)
        print(item[0])

        B=np.array(item[1])
        A=np.array(comp_grp_list)

        X2 = np.linalg.solve(A, B)

        print(X2)

        final_binned_parameter=[item[0],X2]
        final_binned_parameter_all.append(final_binned_parameter)

    print(final_binned_parameter_all)
    return(final_binned_parameter_all)
    #return(final_binned_parameter_all)