import re


def segregate(df):
#print(df)

#df={'lmin': '1e-005', 'lmax': '2e-05', 'wmin': '1.003e-005', 'wmax': '90.003e-05', 'version': '4.5', 'rgeomod': '1', 'binunit': '2', 'paramchk': '1', 'mobmod': '0', 'capmod': '2', 'igcmod': '0', 'igbmod': '0', 'diomod': '1', 'rdsmod': '1', 'rbodymod': '0', 'rgatemod': '0', 'permod': '1', 'acnqsmod': '0', 'trnqsmod': '0', 'tempmod': '0', 'wpemod': '1', 'tnom': '25', 'dtox': '5.958e-010', 'epsrox': '3.9', 'wint': '1.02e-008', 'lint': '2.595e-008', 'll': '0', 'wl': '0', 'lln': '1', 'wln': '1', 'lw': '0', 'ww': '0', 'lwn': '1', 'wwn': '1', 'lwl': '0', 'wwl': '0', 'llc': '0', 'wlc': '0', 'lwc': '0', 'wwc': '0', 'lwlc': '0', 'wwlc': '0', 'xl': '-1.5e-08', 'xw': '0', 'dlc': '2.595e-008', 'dwc': '0', 'xpart': '1', 'toxref': '3e-009', 'dlcig': '2.5e-009', 'vth0': '0.43953', 'k1': '0.448', 'k2': '0.044342', 'k3': '-3.7', 'k3b': '1.2', 'w0': '0', 'dvt0': '0.09708', 'dvt1': '0.3053', 'dvt2': '-0.6939', 'dvt0w': '0', 'dvt1w': '0', 'dvt2w': '0', 'dsub': '0.633', 'minv': '-0.34', 'voffl': '-1.22e-009', 'dvtp0': '1.46e-006', 'dvtp1': '0', 'lpe0': '9.921e-009', 'lpeb': '2.178e-008', 'web': '0', 'wec': '0', 'scref': '1e-006', 'kvth0we': '0.0034927135', 'lkvth0we': '0', 'wkvth0we': '0', 'pkvth0we': '0', 'k2we': '0.0038', 'lk2we': '0', 'wk2we': '0', 'pk2we': '0', 'xj': '1.6e-007', 'ngate': '9e+019', 'ndep': '5.8e+017', 'nsd': '1e+020', 'phin': '0', 'cdsc': '0', 'cdscb': '0', 'cdscd': '0', 'cit': '0.00082854', 'voff': '-0.13055', 'tvoff': '1.500000e-03', 'nfactor': '0.94972', 'eta0': '0.22771', 'etab': '-0.308', 'ud': '0', 'lud': '0', 'wud': '0', 'pud': '0', 'ku0we': '0', 'lku0we': '0', 'wku0we': '0', 'pku0we': '0', 'u0': '0.030526', 'ua': '-1.1118e-009', 'ub': '2.3263e-018', 'uc': '1.9167e-010', 'vsat': '73329', 'a0': '1.0724', 'ags': '0.50072', 'a1': '0', 'a2': '0.995', 'b0': '0', 'b1': '0', 'keta': '-0.051375', 'dwg': '0', 'dwb': '0', 'pclm': '0.71887', 'pdiblc1': '0', 'pdiblc2': '0.000975', 'pdiblcb': '0', 'drout': '0.5', 'pvag': '0.6279', 'delta': '0.005', 'pscbe1': '4.5e+008', 'pscbe2': '1e-020', 'fprout': '0', 'pdits': '0', 'pditsd': '0', 'pditsl': '0', 'rsh': '7.28', 'rdsw': '200', 'rsw': '90.88', 'rdw': '90.88', 'prwg': '0', 'prwb': '0', 'wr': '1', 'alpha0': '1.454e-007', 'alpha1': '2.295', 'beta0': '17.8', 'agidl': '2.593e-009', 'bgidl': '1.8508e+009', 'cgidl': '0.25', 'egidl': '0.2624', 'aigbacc': '0.01213', 'bigbacc': '0.006537', 'cigbacc': '0.2809', 'nigbacc': '4.05', 'aigbinv': '0.35', 'bigbinv': '0.03', 'cigbinv': '0.006', 'eigbinv': '1.1', 'nigbinv': '1', 'aigc': '0.01', 'bigc': '0.00144', 'cigc': '1.515e-005', 'aigsd': '0.008379', 'bigsd': '0.0002699', 'cigsd': '3.925e-020', 'nigc': '1', 'poxedge': '1', 'pigcd': '2.171', 'ntox': '1', 'xrcrg1': '12', 'xrcrg2': '1', 'cgso': 'cgon', 'cgdo': 'cgon', 'cgbo': '0', 'cgdl': 'cgln', 'cgsl': 'cgln', 'clc': '1e-007', 'cle': '0.6', 'cf': 'cfn', 'ckappas': '0.6', 'ckappad': '0.6', 'acde': '0.4', 'moin': '5.346', 'noff': '1.973', 'voffcv': '-0.0904', 'kt1': '-0.24611586', 'kt1l': '0', 'kt2': '-0.055191541', 'pkt2': '0', 'wkt2': '0', 'lkt2': '0', 'ute': '-1.8116912', 'ua1': '2.3415359e-009', 'ub1': '-4.4298745e-018', 'uc1': '-8.0699954e-011', 'prt': '0', 'at': '117848.51', 'pat': '0', 'wat': '0', 'lat': '0', 'jss': '2.85e-07', 'jsd': '2.85e-07', 'jsws': '6.9e-13', 'jswd': '6.9e-13', 'jswgs': '6.9e-13', 'jswgd': '6.9e-13', 'njs': '1', 'njd': '1', 'ijthsfwd': '0.01', 'ijthdfwd': '0.01', 'ijthsrev': '0.01', 'ijthdrev': '0.01', 'bvs': '11.25', 'bvd': '11.25', 'xjbvs': '1', 'xjbvd': '1', 'pbs': '0.6882682', 'pbd': '0.6882682', 'cjs': 'cjn', 'cjd': 'cjn', 'mjs': '0.359', 'mjd': '0.359', 'pbsws': '0.32', 'pbswd': '0.32', 'cjsws': 'cjswn', 'cjswd': 'cjswn', 'mjsws': '0.202', 'mjswd': '0.202', 'pbswgs': '0.952', 'pbswgd': '0.952', 'cjswgs': 'cjswgn', 'cjswgd': 'cjswgn', 'mjswgs': '0.541', 'mjswgd': '0.541', 'tpb': '1.49e-3', 'tcj': '9.05e-4', 'tpbsw': '8.94e-04', 'tcjsw': '8.09e-04', 'tpbswg': '0.00133', 'tcjswg': '0.00088', 'xtis': '3', 'xtid': '3', 'jtsswgs': '1.09e-009', 'jtsswgd': '1.09e-009', 'njtsswg': '11.6', 'xtsswgs': '0.2886', 'xtsswgd': '0.2886', 'tnjtsswg': '1.08', 'vtsswgs': '10', 'vtsswgd': '10', 'dmcg': '2.05e-007', 'dmci': '3.15e-007', 'dmdg': '0', 'dmcgt': '0', 'dwj': '0', 'xgw': '0', 'xgl': '-3.1e-008', 'rshg': '8.23', 'gbmin': '1e-012', 'rbpb': '50', 'rbpd': '50', 'rbps': '50', 'rbdb': '50', 'rbsb': '50', 'saref': '1.00e-05', 'sbref': '1.00e-05', 'ngcon': '1', 'wlod': '5e-007', 'kvth0': '2.2e-009', 'lkvth0': '-1e-008', 'wkvth0': '2.2e-006', 'pkvth0': '-5e-014', 'llodvth': '1', 'wlodvth': '1', 'stk2': '2.5e-009', 'lodk2': '1', 'lodeta0': '2', 'ku0': '-3.2e-008', 'lku0': '2e-007', 'wku0': '7e-007', 'pku0': '-5e-014', 'llodku0': '1', 'wlodku0': '1', 'kvsat': '0.4', 'steta0': '-1.1e-010', 'tku0': '0.03', 'lvth0': '0', 'wvth0': '0', 'pvth0': '0', 'lk2': '0', 'lcit': '0', 'pcit': '0', 'lvoff': '0', 'pvoff': '0', 'leta0': '0', 'peta0': '0', 'lu0': '0', 'pu0': '0', 'lvsat': '0', 'pvsat': '0', 'la0': '0', 'pa0': '0', 'lpclm': '0', 'ppclm': '0', 'lpdiblc2': '0', 'ppdiblc2': '0', 'fnoimod': '1', 'noia': 'noian', 'noib': 'noibn', 'noic': 'noicn', 'em': '3.00e7', 'ef': '0.904', 'minr': '1e-3'}
    #df={'lmin': '1.2e-006', 'lmax': '1e-005', 'wmin': '1.003e-005', 'wmax': '90.003e-05', 'version': '4.5', 'rgeomod': '1', 'binunit': '2', 'paramchk': '1', 'mobmod': '0', 'capmod': '2', 'igcmod': '0', 'igbmod': '0', 'diomod': '1', 'rdsmod': '1', 'rbodymod': '0', 'rgatemod': '0', 'permod': '1', 'acnqsmod': '0', 'trnqsmod': '0', 'tempmod': '0', 'wpemod': '1', 'tnom': '25', 'dtox': '5.958e-010', 'epsrox': '3.9', 'wint': '1.02e-008', 'lint': '2.595e-008', 'll': '0', 'wl': '0', 'lln': '1', 'wln': '1', 'lw': '0', 'ww': '0', 'lwn': '1', 'wwn': '1', 'lwl': '0', 'wwl': '0', 'llc': '0', 'wlc': '0', 'lwc': '0', 'wwc': '0', 'lwlc': '0', 'wwlc': '0', 'xl': '-1.5e-08', 'xw': '0', 'dlc': '2.595e-008', 'dwc': '0', 'xpart': '1', 'toxref': '3e-009', 'dlcig': '2.5e-009', 'vth0': '0.44000255', 'lvth0': '-4.6939282e-009', 'k1': '0.448', 'k2': '0.044420158', 'lk2': '-7.763527e-010', 'k3': '-3.7', 'k3b': '1.2', 'w0': '0', 'dvt0': '0.09708', 'dvt1': '0.3053', 'dvt2': '-0.6939', 'dvt0w': '0', 'dvt1w': '0', 'dvt2w': '0', 'dsub': '0.633', 'minv': '-0.34', 'voffl': '-1.22e-009', 'dvtp0': '1.46e-006', 'dvtp1': '0', 'lpe0': '9.921e-009', 'lpeb': '2.178e-008', 'web': '0', 'wec': '0', 'scref': '1e-006', 'kvth0we': '0.0035080237', 'lkvth0we': '-1.5207765e-010', 'wkvth0we': '0', 'pkvth0we': '0', 'k2we': '0.0038', 'lk2we': '0', 'wk2we': '0', 'pk2we': '0', 'xj': '1.6e-007', 'ngate': '9e+019', 'ndep': '5.8e+017', 'nsd': '1e+020', 'phin': '0', 'cdsc': '0', 'cdscb': '0', 'cdscd': '0', 'cit': '0.00094159467', 'lcit': '-1.1229833e-009', 'voff': '-0.13088478', 'tvoff': '1.500000e-03', 'lvoff': '3.3253987e-009', 'nfactor': '0.94802421', 'lnfactor': '1.6844423e-008', 'eta0': '0.2200075', 'leta0': '7.650975e-008', 'etab': '-0.308', 'ud': '0', 'lud': '0', 'wud': '0', 'pud': '0', 'ku0we': '0', 'lku0we': '0', 'wku0we': '0', 'pku0we': '0', 'u0': '0.031147016', 'lu0': '-6.1686146e-009', 'ua': '-1.0351999e-009', 'lua': '-7.608768e-016', 'ub': '2.2622927e-018', 'lub': '6.3579065e-025', 'uc': '1.9814412e-010', 'luc': '-6.4308095e-017', 'vsat': '73219.038', 'lvsat': '0.0010922656', 'a0': '1.0632966', 'la0': '9.0425265e-008', 'ags': '0.47288051', 'lags': '2.7653248e-007', 'a1': '0', 'a2': '0.995', 'b0': '0', 'b1': '0', 'keta': '-0.044517814', 'lketa': '-6.8113118e-008', 'dwg': '0', 'dwb': '0', 'pclm': '0.73030143', 'lpclm': '-1.1354958e-007', 'pdiblc1': '0', 'pdiblc2': '0.00083459861', 'lpdiblc2': '1.3946211e-009', 'pdiblcb': '0', 'drout': '0.5', 'pvag': '0.6279', 'delta': '0.005', 'pscbe1': '4.5e+008', 'pscbe2': '1e-020', 'fprout': '0', 'pdits': '0', 'pditsd': '0', 'pditsl': '0', 'rsh': '7.28', 'rdsw': '200', 'rsw': '90.88', 'rdw': '90.88', 'prwg': '0', 'prwb': '0', 'wr': '1', 'alpha0': '1.454e-007', 'alpha1': '2.295', 'beta0': '17.8', 'agidl': '2.593e-009', 'bgidl': '1.8508e+009', 'cgidl': '0.25', 'egidl': '0.2624', 'aigbacc': '0.01213', 'bigbacc': '0.006537', 'cigbacc': '0.2809', 'nigbacc': '4.05', 'aigbinv': '0.35', 'bigbinv': '0.03', 'cigbinv': '0.006', 'eigbinv': '1.1', 'nigbinv': '1', 'aigc': '0.01', 'bigc': '0.00144', 'cigc': '1.515e-005', 'aigsd': '0.008379', 'bigsd': '0.0002699', 'cigsd': '3.925e-020', 'nigc': '1', 'poxedge': '1', 'pigcd': '2.171', 'ntox': '1', 'xrcrg1': '12', 'xrcrg2': '1', 'cgso': 'cgon', 'cgdo': 'cgon', 'cgbo': '0', 'cgdl': 'cgln', 'cgsl': 'cgln', 'clc': '1e-007', 'cle': '0.6', 'cf': 'cfn', 'ckappas': '0.6', 'ckappad': '0.6', 'acde': '0.4', 'moin': '5.346', 'noff': '1.973', 'voffcv': '-0.0904', 'kt1': '-0.24355302', 'pkt1': '0', 'wkt1': '0', 'lkt1': '-2.5456989e-08', 'kt1l': '0', 'kt2': '-0.055236684', 'pkt2': '0', 'wkt2': '0', 'lkt2': '4.48417e-10', 'ute': '-1.8758', 'lute': '6.3679863e-007', 'ua1': '2.2474837e-09', 'pua1': '0', 'wua1': '0', 'lua1': '9.3422973e-16', 'ub1': '-4.4202733e-018', 'lub1': '-9.5370005e-026', 'uc1': '-7.421409e-11', 'puc1': '0', 'wuc1': '0', 'luc1': '-6.442474e-17', 'prt': '0', 'at': '122782.95', 'pat': '0', 'wat': '0', 'lat': '-0.049014274', 'jss': '2.85e-07', 'jsd': '2.85e-07', 'jsws': '6.9e-13', 'jswd': '6.9e-13', 'jswgs': '6.9e-13', 'jswgd': '6.9e-13', 'njs': '1', 'njd': '1', 'ijthsfwd': '0.01', 'ijthdfwd': '0.01', 'ijthsrev': '0.01', 'ijthdrev': '0.01', 'bvs': '11.25', 'bvd': '11.25', 'xjbvs': '1', 'xjbvd': '1', 'pbs': '0.6882682', 'pbd': '0.6882682', 'cjs': 'cjn', 'cjd': 'cjn', 'mjs': '0.359', 'mjd': '0.359', 'pbsws': '0.32', 'pbswd': '0.32', 'cjsws': 'cjswn', 'cjswd': 'cjswn', 'mjsws': '0.202', 'mjswd': '0.202', 'pbswgs': '0.952', 'pbswgd': '0.952', 'cjswgs': 'cjswgn', 'cjswgd': 'cjswgn', 'mjswgs': '0.541', 'mjswgd': '0.541', 'tpb': '1.49e-3', 'tcj': '9.05e-4', 'tpbsw': '8.94e-04', 'tcjsw': '8.09e-04', 'tpbswg': '0.00133', 'tcjswg': '0.00088', 'xtis': '3', 'xtid': '3', 'jtsswgs': '1.09e-009', 'jtsswgd': '1.09e-009', 'njtsswg': '11.6', 'xtsswgs': '0.2886', 'xtsswgd': '0.2886', 'tnjtsswg': '1.08', 'vtsswgs': '10', 'vtsswgd': '10', 'dmcg': '2.05e-007', 'dmci': '3.15e-007', 'dmdg': '0', 'dmcgt': '0', 'dwj': '0', 'xgw': '0', 'xgl': '-3.1e-008', 'rshg': '8.23', 'gbmin': '1e-012', 'rbpb': '50', 'rbpd': '50', 'rbps': '50', 'rbdb': '50', 'saref': '1.00e-05', 'sbref': '1.00e-05', 'rbsb': '50', 'ngcon': '1', 'wlod': '5e-007', 'kvth0': '2.2e-009', 'lkvth0': '-1e-008', 'wkvth0': '2.2e-006', 'pkvth0': '-5e-014', 'llodvth': '1', 'wlodvth': '1', 'stk2': '2.5e-009', 'lodk2': '1', 'lodeta0': '2', 'ku0': '-3.2e-008', 'lku0': '2e-007', 'wku0': '7e-007', 'pku0': '-5e-014', 'llodku0': '1', 'wlodku0': '1', 'kvsat': '0.4', 'steta0': '-1.1e-010', 'tku0': '0.03', 'wvth0': '0', 'pvth0': '0', 'pcit': '0', 'pvoff': '0+dpvoffn', 'peta0': '0+dpeta0n', 'pu0': '0+dpu0n_opt1', 'pvsat': '0+dpvsatn_opt1', 'pa0': '0+dpa0n', 'ppclm': '0+dppclmn', 'ppdiblc2': '0+dppdiblc2n', 'fnoimod': '1', 'noia': 'noian', 'noib': 'noibn', 'noic': 'noicn', 'em': '3.00e7', 'ef': '0.904', 'minr': '1e-3'}

    pattern = r"\bl\w*\b"
    pattern_w=r"\bw\w*\b"
    pattern_p=r"\bp\w*\b"




    l_term=[]
    w_term=[]
    p_term=[]


    all_key=[]

    for key, value in df.items():
        print(key)
        print(value)

        x=re.findall(pattern, key)
        y = re.findall(pattern_w, key)
        z = re.findall(pattern_p, key)
        all_key.append(key)

        if x:
            l_term.append(x[0])
        if y:
            w_term.append(y[0])
        if z:
            p_term.append(z[0])


        print(re.findall(pattern, key))



    print(l_term)
    print(w_term)
    print(p_term)


    print(all_key)
    reExp = re.compile("\s*(^l)\s*=\s*([+-.\w]+)\s*", flags=re.S)

    third_min_l=[]
    third_min_w=[]
    third_min_p=[]


    for item in l_term:
        third_min_l.append(item[1:])

    for item in w_term:
        third_min_w.append(item[1:])

    for item in p_term:
        third_min_p.append(item[1:])

    third=l_term[0]

    third_min=third[1:]

    print(third_min)

    print(third_min_l)
    print(third_min_w)
    print(third_min_p)


    def getList(dict):
        return dict.keys()

    original_key_list=list(df.keys())


    third_min_vo_l_overlap=list(set(original_key_list).intersection(third_min_l))
    third_min_vo_w_overlap=list(set(original_key_list).intersection(third_min_w))
    third_min_vo_p_overlap=list(set(original_key_list).intersection(third_min_p))



    third_min_l_w_overlap=list(set(third_min_l).intersection(third_min_w))


    third_min_l_w_p_overlap=list(set(third_min_l).intersection(third_min_w).intersection(third_min_p))
    print(list(set(third_min_l).intersection(third_min_w).intersection(third_min_p)))

    removable_list=['l','wl','int','ln','wc','w','lodvth','wn','wlc','lc','min','lodku0','max']

    pure_l_w_overlap=[]

    for item in removable_list:
        third_min_l_w_overlap.remove(item)
        #pure_l_w_overlap.append(pure_l_w)


    #pure_l_w_overlap=third_min_l_w_overlap.remove('l',	'wl',	'int',	'ln',	'wc',	'w',	'lodvth',	'wn',	'wlc',	'lc',	'min',	'lodku0',	'max')

    print(list(set(third_min_l).intersection(third_min_w)))
    print(third_min_l_w_overlap)

    print(third_min_vo_l_overlap)

    print(third_min_vo_w_overlap)
    print(third_min_vo_p_overlap)

    binned_items=list(set().union(third_min_vo_l_overlap,third_min_vo_w_overlap,third_min_vo_p_overlap))

    print(sorted(binned_items))
    print(sorted(original_key_list))
    #   reExp = re.compile("\s*([+-.\w]+)\s*=\s*([+-.\w]+)\s*", flags=re.S)


    removable_nonbin_list=['wl','wlc']

    for item in removable_nonbin_list:
        binned_items.remove(item)



    print(sorted(binned_items))
    return (binned_items)