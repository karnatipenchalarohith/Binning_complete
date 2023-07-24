


import json

def join_bins(binnum,suffix,cal_l1w1,binned_parameters,all_parameters):

#    binnum='bin1'
#    suffix='_l1w1'
#    cal_l1w1= {'final_a0': 1.0723391265, 'final_ags': 0.500533758, 'final_at': 117881.5226, 'final_cit': 0.0008292963399999999, 'final_eta0': 0.227658475, 'final_k2': 0.04434252273, 'final_k2we': 0.0038, 'final_keta': -0.0513291258, 'final_kt1': -0.2460987189, 'final_kt2': -0.0551918423, 'final_ku0': 0.020772164482339473, 'final_ku0we': 0.0, 'final_kvth0': 0.0014388097953023792, 'final_kvth0we': 0.003492815935, 'final_nfactor': 0.9497086523, 'final_pclm': 0.7189464720000001, 'final_pdiblc2': 0.0009740607200000001, 'final_u0': 0.03053015454, 'final_ua': -1.1112875800000002e-09, 'final_ua1': 2.3409066730000002e-09, 'final_ub': 2.3258717650000002e-18, 'final_ub1': -4.4298103005e-18, 'final_uc': 1.917133105e-10, 'final_uc1': -8.0656564e-11, 'final_ud': 0.0, 'final_ute': -1.812120137, 'final_voff': -0.13055224013, 'final_vsat': 73328.26456, 'final_vth0': 0.43953315717999997}

#    binned_parameters=['a0', 'ags', 'at', 'cit', 'eta0', 'k2', 'k2we', 'keta', 'kt1', 'kt2', 'ku0', 'ku0we', 'kvth0', 'kvth0we', 'nfactor', 'pclm', 'pdiblc2', 'u0', 'ua', 'ua1', 'ub', 'ub1', 'uc', 'uc1', 'ud', 'ute', 'voff', 'vsat', 'vth0']

#    all_parameters = {'lmin': '1.2e-006', 'lmax': '1e-005', 'wmin': '1.003e-005', 'wmax': '90.003e-05', 'version': '4.5', 'rgeomod': '1', 'binunit': '2', 'paramchk': '1', 'mobmod': '0', 'capmod': '2', 'igcmod': '0', 'igbmod': '0', 'diomod': '1', 'rdsmod': '1', 'rbodymod': '0', 'rgatemod': '0', 'permod': '1', 'acnqsmod': '0', 'trnqsmod': '0', 'tempmod': '0', 'wpemod': '1', 'tnom': '25', 'toxe': '3.981e-09', 'toxm': '3.981e-09', 'dtox': '5.958e-010', 'epsrox': '3.9', 'wint': '1.02e-008', 'lint': '2.595e-008', 'll': '0', 'wl': '0', 'lln': '1', 'wln': '1', 'lw': '0', 'ww': '0', 'lwn': '1', 'wwn': '1', 'lwl': '0', 'wwl': '0', 'llc': '0', 'wlc': '0', 'lwc': '0', 'wwc': '0', 'lwlc': '0', 'wwlc': '0', 'xl': '-1.5e-08', 'xw': '0', 'dlc': '2.595e-008', 'dwc': '0', 'xpart': '1', 'toxref': '3e-009', 'dlcig': '2.5e-009', 'vth0': '0.44000255', 'lvth0': '-4.6939282e-009', 'k1': '0.448', 'k2': '0.044420158', 'lk2': '-7.763527e-010', 'k3': '-3.7', 'k3b': '1.2', 'w0': '0', 'dvt0': '0.09708', 'dvt1': '0.3053', 'dvt2': '-0.6939', 'dvt0w': '0', 'dvt1w': '0', 'dvt2w': '0', 'dsub': '0.633', 'minv': '-0.34', 'voffl': '-1.22e-009', 'dvtp0': '1.46e-006', 'dvtp1': '0', 'lpe0': '9.921e-009', 'lpeb': '2.178e-008', 'web': '0', 'wec': '0', 'scref': '1e-006', 'kvth0we': '0.0035080237', 'lkvth0we': '-1.5207765e-010', 'wkvth0we': '0', 'pkvth0we': '0', 'k2we': '0.0038', 'lk2we': '0', 'wk2we': '0', 'pk2we': '0', 'xj': '1.6e-007', 'ngate': '9e+019', 'ndep': '5.8e+017', 'nsd': '1e+020', 'phin': '0', 'cdsc': '0', 'cdscb': '0', 'cdscd': '0', 'cit': '0.00094159467', 'lcit': '-1.1229833e-009', 'voff': '-0.13088478', 'tvoff': '1.500000e-03', 'lvoff': '3.3253987e-009', 'nfactor': '0.94802421', 'lnfactor': '1.6844423e-008', 'eta0': '0.2200075', 'leta0': '7.650975e-008', 'etab': '-0.308', 'ud': '0', 'lud': '0', 'wud': '0', 'pud': '0', 'ku0we': '0', 'lku0we': '0', 'wku0we': '0', 'pku0we': '0', 'u0': '0.031147016', 'lu0': '-6.1686146e-009', 'ua': '-1.0351999e-009', 'lua': '-7.608768e-016', 'ub': '2.2622927e-018', 'lub': '6.3579065e-025', 'uc': '1.9814412e-010', 'luc': '-6.4308095e-017', 'vsat': '73219.038', 'lvsat': '0.0010922656', 'a0': '1.0632966', 'la0': '9.0425265e-008', 'ags': '0.47288051', 'lags': '2.7653248e-007', 'a1': '0', 'a2': '0.995', 'b0': '0', 'b1': '0', 'keta': '-0.044517814', 'lketa': '-6.8113118e-008', 'dwg': '0', 'dwb': '0', 'pclm': '0.73030143', 'lpclm': '-1.1354958e-007', 'pdiblc1': '0', 'pdiblc2': '0.00083459861', 'lpdiblc2': '1.3946211e-009', 'pdiblcb': '0', 'drout': '0.5', 'pvag': '0.6279', 'delta': '0.005', 'pscbe1': '4.5e+008', 'pscbe2': '1e-020', 'fprout': '0', 'pdits': '0', 'pditsd': '0', 'pditsl': '0', 'rsh': '7.28', 'rdsw': '200', 'rsw': '90.88', 'rdw': '90.88', 'prwg': '0', 'prwb': '0', 'wr': '1', 'alpha0': '1.454e-007', 'alpha1': '2.295', 'beta0': '17.8', 'agidl': '2.593e-009', 'bgidl': '1.8508e+009', 'cgidl': '0.25', 'egidl': '0.2624', 'aigbacc': '0.01213', 'bigbacc': '0.006537', 'cigbacc': '0.2809', 'nigbacc': '4.05', 'aigbinv': '0.35', 'bigbinv': '0.03', 'cigbinv': '0.006', 'eigbinv': '1.1', 'nigbinv': '1', 'aigc': '0.01', 'bigc': '0.00144', 'cigc': '1.515e-005', 'aigsd': '0.008379', 'bigsd': '0.0002699', 'cigsd': '3.925e-020', 'nigc': '1', 'poxedge': '1', 'pigcd': '2.171', 'ntox': '1', 'xrcrg1': '12', 'xrcrg2': '1', 'cgso': 'cgon', 'cgdo': 'cgon', 'cgbo': '0', 'cgdl': 'cgln', 'cgsl': 'cgln', 'clc': '1e-007', 'cle': '0.6', 'cf': 'cfn', 'ckappas': '0.6', 'ckappad': '0.6', 'acde': '0.4', 'moin': '5.346', 'noff': '1.973', 'voffcv': '-0.0904', 'kt1': '-0.24355302', 'pkt1': '0', 'wkt1': '0', 'lkt1': '-2.5456989e-08', 'kt1l': '0', 'kt2': '-0.055236684', 'pkt2': '0', 'wkt2': '0', 'lkt2': '4.48417e-10', 'ute': '-1.8758', 'lute': '6.3679863e-007', 'ua1': '2.2474837e-09', 'pua1': '0', 'wua1': '0', 'lua1': '9.3422973e-16', 'ub1': '-4.4202733e-018', 'lub1': '-9.5370005e-026', 'uc1': '-7.421409e-11', 'puc1': '0', 'wuc1': '0', 'luc1': '-6.442474e-17', 'prt': '0', 'at': '122782.95', 'pat': '0', 'wat': '0', 'lat': '-0.049014274', 'jss': '2.85e-07', 'jsd': '2.85e-07', 'jsws': '6.9e-13', 'jswd': '6.9e-13', 'jswgs': '6.9e-13', 'jswgd': '6.9e-13', 'njs': '1', 'njd': '1', 'ijthsfwd': '0.01', 'ijthdfwd': '0.01', 'ijthsrev': '0.01', 'ijthdrev': '0.01', 'bvs': '11.25', 'bvd': '11.25', 'xjbvs': '1', 'xjbvd': '1', 'pbs': '0.6882682', 'pbd': '0.6882682', 'cjs': 'cjn', 'cjd': 'cjn', 'mjs': '0.359', 'mjd': '0.359', 'pbsws': '0.32', 'pbswd': '0.32', 'cjsws': '1.185e-10', 'cjswd': '1.185e-10', 'mjsws': '0.202', 'mjswd': '0.202', 'pbswgs': '0.952', 'pbswgd': '0.952', 'cjswgs': '3.82e-10', 'cjswgd': '3.82e-10', 'mjswgs': '0.541', 'mjswgd': '0.541', 'tpb': '1.49e-3', 'tcj': '9.05e-4', 'tpbsw': '8.94e-04', 'tcjsw': '8.09e-04', 'tpbswg': '0.00133', 'tcjswg': '0.00088', 'xtis': '3', 'xtid': '3', 'jtsswgs': '1.09e-009', 'jtsswgd': '1.09e-009', 'njtsswg': '11.6', 'xtsswgs': '0.2886', 'xtsswgd': '0.2886', 'tnjtsswg': '1.08', 'vtsswgs': '10', 'vtsswgd': '10', 'dmcg': '2.05e-007', 'dmci': '3.15e-007', 'dmdg': '0', 'dmcgt': '0', 'dwj': '0', 'xgw': '0', 'xgl': '-3.1e-008', 'rshg': '8.23', 'gbmin': '1e-012', 'rbpb': '50', 'rbpd': '50', 'rbps': '50', 'rbdb': '50', 'saref': '1.00e-05', 'sbref': '1.00e-05', 'rbsb': '50', 'ngcon': '1', 'wlod': '5e-007', 'kvth0': '2.2e-009', 'lkvth0': '-1e-008', 'wkvth0': '2.2e-006', 'pkvth0': '-5e-014', 'llodvth': '1', 'wlodvth': '1', 'stk2': '2.5e-009', 'lodk2': '1', 'lodeta0': '2', 'ku0': '-3.2e-008', 'lku0': '2e-007', 'wku0': '7e-007', 'pku0': '-5e-014', 'llodku0': '1', 'wlodku0': '1', 'kvsat': '0.4', 'steta0': '-1.1e-010', 'tku0': '0.03', 'wvth0': '0', 'pvth0': '0', 'pcit': '0', 'pvoff': '0', 'peta0': '0', 'pu0': '0', 'pvsat': '0', 'pa0': '0', 'ppclm': '0', 'ppdiblc2': '0', 'fnoimod': '1', 'noia': '1.250e+42', 'noib': '7.000e+23', 'noic': '6.080e+7', 'em': '3.00e7', 'ef': '0.904', 'minr': '1e-3'}


    prefix='final_'
    cal_l1w1_new={}
    for key, value in cal_l1w1.items():
        print(key)
        print(value)
        if key.startswith(prefix):
            new_key = key[len(prefix):]
            cal_l1w1_new[new_key] = cal_l1w1[key]

    print(cal_l1w1_new)

    print(all_parameters)

    pattern_l = r"\bl\w*\b"
    pattern_w = r"\bw\w*\b"
    pattern_p = r"\bp\w*\b"

    for par in binned_parameters:

        l_par ='l' + par
        w_par ='w' + par
        p_par ='p' + par

    #    print(l_par,w_par,p_par)

        if l_par in all_parameters:
            all_parameters.pop(l_par)

        if w_par in all_parameters:
            all_parameters.pop(w_par)

        if p_par in all_parameters:
            all_parameters.pop(p_par)



    #    print (par)

        value = cal_l1w1_new[par]
    #    print(value)
        all_parameters[par]=value

    print(cal_l1w1_new)

    print(all_parameters)



    filename=binnum+'_'+suffix + '.txt'
    with open(filename, "w") as f:
        count=0

        for key, value in all_parameters.items():
#            f.write(f"+ ")
            f.write(f"{key}= {value}")
            count += 1

            if count % 3 ==0 :
                f.write("\n")
            else :
                f.write("  ")



    #    json_string = json.dumps(all_parameters)
    #    f.write(json_string)



