

def extractlminwmin(all_parameters):


  #  all_parameters={'lmin': '5e-007', 'lmax': '1.2e-006', 'wmin': '2.2e-07', 'wmax': '5.3e-007', 'version': '4.5', 'rgeomod': '1', 'binunit': '2', 'paramchk': '1', 'mobmod': '0', 'capmod': '2', 'igcmod': '0', 'igbmod': '0', 'diomod': '1', 'rdsmod': '1', 'rbodymod': '0', 'rgatemod': '0', 'permod': '1', 'acnqsmod': '0', 'trnqsmod': '0', 'tempmod': '0', 'wpemod': '1', 'tnom': '25', 'dtox': '5.958e-010', 'epsrox': '3.9', 'wint': '1.02e-008', 'lint': '2.595e-008', 'll': '0', 'wl': '0', 'lln': '1', 'wln': '1', 'lw': '0', 'ww': '0', 'lwn': '1', 'wwn': '1', 'lwl': '0', 'wwl': '0', 'llc': '0', 'wlc': '0', 'lwc': '0', 'wwc': '0', 'lwlc': '0', 'wwlc': '0', 'xl': '-1.5e-08', 'xw': '0', 'dlc': '2.595e-008', 'dwc': '0', 'xpart': '1', 'toxref': '3e-009', 'dlcig': '2.5e-009', 'vth0': '0.44828089', 'lvth0': '1.1393503e-008', 'wvth0': '4.181767e-010', 'pvth0': '-2.1691937e-015', 'k1': '0.448', 'k2': '0.048140709', 'lk2': '-3.1115533e-010', 'wk2': '-3.7122147e-009', 'pk2': '-9.1322366e-016', 'k3': '-3.7', 'k3b': '1.2', 'w0': '0', 'dvt0': '0.09708', 'dvt1': '0.3053', 'dvt2': '-0.6939', 'dvt0w': '0', 'dvt1w': '0', 'dvt2w': '0', 'dsub': '0.633', 'minv': '-0.34', 'voffl': '-1.22e-009', 'dvtp0': '1.46e-006', 'dvtp1': '0', 'lpe0': '9.921e-009', 'lpeb': '2.178e-008', 'web': '0', 'wec': '0', 'scref': '1e-006', 'kvth0we': '0.0035', 'lkvth0we': '-1.4299999e-010', 'wkvth0we': '-1.2000011e-011', 'pkvth0we': '1.5000009e-017', 'k2we': '0.0038', 'lk2we': '0', 'wk2we': '0', 'pk2we': '0', 'xj': '1.6e-007', 'ngate': '9e+019', 'ndep': '5.8e+017', 'nsd': '1e+020', 'phin': '0', 'cdsc': '0', 'cdscb': '0', 'cdscd': '0', 'cit': '0.00048769918', 'lcit': '1.4475774e-010', 'wcit': '8.8758178e-011', 'pcit': '-1.0949483e-016', 'voff': '-0.14850048', 'tvoff': '0.00095327882', 'ptvoff': '-1.0351402e-16', 'wtvoff': '9.32555e-12', 'ltvoff': '5.1860729e-10', 'lvoff': '-8.3937491e-009', 'wvoff': '-1.0682653e-009', 'pvoff': '1.6194193e-015', 'nfactor': '1.305933', 'lnfactor': '-1.6038562e-007', 'wnfactor': '-7.3413756e-008', 'pnfactor': '4.6006229e-014', 'eta0': '0.0092251498', 'leta0': '1.3110407e-007', 'weta0': '4.7248216e-008', 'peta0': '-2.7511725e-014', 'etab': '-0.308', 'ud': '0', 'lud': '0', 'wud': '0', 'pud': '0', 'ku0we': '0', 'lku0we': '0', 'wku0we': '0', 'pku0we': '0', 'u0': '0.020914402', 'lu0': '5.0764788e-009', 'wu0': '3.0151699e-009', 'pu0': '-1.0586033e-015', 'ua': '-4.7450936e-010', 'lua': '1.8421903e-017', 'wua': '6.3743975e-018', 'pua': '-6.1719657e-023', 'ub': '3.3755544e-019', 'lub': '7.394269e-025', 'wub': '2.2747064e-025', 'pub': '-6.2706491e-032', 'uc': '4.6796853e-011', 'luc': '7.9323958e-017', 'wuc': '1.8651644e-017', 'puc': '-2.3803623e-023', 'vsat': '77860.433', 'lvsat': '-0.00081878711', 'wvsat': '-0.0035518874', 'pvsat': '2.4125667e-009', 'a0': '-0.10275458', 'la0': '4.6730518e-007', 'wa0': '2.9650415e-007', 'pa0': '-1.4364985e-013', 'ags': '0.3065495', 'lags': '4.8480478e-007', 'wags': '1.0570427e-007', 'pags': '-7.7370976e-014', 'a1': '0', 'a2': '0.995', 'b0': '0', 'b1': '0', 'keta': '-0.044479894', 'lketa': '-1.8697001e-008', 'wketa': '-6.9594572e-009', 'pketa': '6.0268161e-015', 'dwg': '0', 'dwb': '0', 'pclm': '0.4744185', 'lpclm': '2.1458817e-007', 'wpclm': '3.7800547e-008', 'ppclm': '-4.28318e-014', 'pdiblc1': '0', 'pdiblc2': '0.0015597345', 'lpdiblc2': '-2.5589493e-010', 'wpdiblc2': '5.1804148e-011', 'ppdiblc2': '1.462308e-016', 'pdiblcb': '0', 'drout': '0.5', 'pvag': '0.6279', 'delta': '0.005', 'pscbe1': '4.5e+008', 'pscbe2': '1e-020', 'fprout': '0', 'pdits': '0', 'pditsd': '0', 'pditsl': '0', 'rsh': '7.28', 'rdsw': '200', 'rsw': '90.88', 'rdw': '90.88', 'prwg': '0', 'prwb': '0', 'wr': '1', 'alpha0': '1.454e-007', 'alpha1': '2.295', 'beta0': '17.8', 'agidl': '2.593e-009', 'bgidl': '1.8508e+009', 'cgidl': '0.25', 'egidl': '0.2624', 'aigbacc': '0.01213', 'bigbacc': '0.006537', 'cigbacc': '0.2809', 'nigbacc': '4.05', 'aigbinv': '0.35', 'bigbinv': '0.03', 'cigbinv': '0.006', 'eigbinv': '1.1', 'nigbinv': '1', 'aigc': '0.01', 'bigc': '0.00144', 'cigc': '1.515e-005', 'aigsd': '0.008379', 'bigsd': '0.0002699', 'cigsd': '3.925e-020', 'nigc': '1', 'poxedge': '1', 'pigcd': '2.171', 'ntox': '1', 'xrcrg1': '12', 'xrcrg2': '1', 'cgso': 'cgon', 'cgdo': 'cgon', 'cgbo': '0', 'cgdl': 'cgln', 'cgsl': 'cgln', 'clc': '1e-007', 'cle': '0.6', 'cf': 'cfn', 'ckappas': '0.6', 'ckappad': '0.6', 'acde': '0.4', 'moin': '5.346', 'noff': '1.973', 'voffcv': '-0.0904', 'kt1': '-0.27879193', 'lkt1': '1.4001673e-08', 'wkt1': '1.1098907e-08', 'pkt1': '-4.991675e-15', 'kt1l': '0', 'kt2': '-0.053872644', 'lkt2': '-5.638463e-10', 'wkt2': '-2.877297e-10', 'pkt2': '1.587215e-16', 'ute': '-1.3891561', 'lute': '1.4508792e-007', 'wute': '6.0707017e-008', 'pute': '-5.4287351e-014', 'ua1': '2.6364413e-09', 'lua1': '2.6732108e-16', 'wua1': '1.4264386e-16', 'pua1': '-2.1553916e-22', 'ub1': '-4.1547516e-018', 'lub1': '2.9650447e-025', 'wub1': '-7.1031093e-026', 'pub1': '1.6079175e-031', 'uc1': '-4.151591e-011', 'luc1': '4.6792241e-017', 'wuc1': '-1.519636e-018', 'puc1': '1.8490137e-024', 'prt': '0', 'at': '114195.88', 'lat': '-0.050081619', 'wat': '-0.0020196821', 'pat': '2.2959393e-09', 'jss': '2.85e-07', 'jsd': '2.85e-07', 'jsws': '6.9e-13', 'jswd': '6.9e-13', 'jswgs': '6.9e-13', 'jswgd': '6.9e-13', 'njs': '1', 'njd': '1', 'ijthsfwd': '0.01', 'ijthdfwd': '0.01', 'ijthsrev': '0.01', 'ijthdrev': '0.01', 'bvs': '11.25', 'bvd': '11.25', 'xjbvs': '1', 'xjbvd': '1', 'pbs': '0.6882682', 'pbd': '0.6882682', 'cjs': 'cjn', 'cjd': 'cjn', 'mjs': '0.359', 'mjd': '0.359', 'pbsws': '0.32', 'pbswd': '0.32', 'cjsws': 'cjswn', 'cjswd': 'cjswn', 'mjsws': '0.202', 'mjswd': '0.202', 'pbswgs': '0.952', 'pbswgd': '0.952', 'cjswgs': 'cjswgn', 'cjswgd': 'cjswgn', 'mjswgs': '0.541', 'mjswgd': '0.541', 'tpb': '1.49e-3', 'tcj': '9.05e-4', 'tpbsw': '8.94e-04', 'tcjsw': '8.09e-04', 'tpbswg': '0.00133', 'tcjswg': '0.00088', 'xtis': '3', 'xtid': '3', 'jtsswgs': '1.09e-009', 'jtsswgd': '1.09e-009', 'njtsswg': '11.6', 'xtsswgs': '0.2886', 'xtsswgd': '0.2886', 'tnjtsswg': '1.08', 'vtsswgs': '10', 'vtsswgd': '10', 'dmcg': '2.05e-007', 'dmci': '3.15e-007', 'dmdg': '0', 'dmcgt': '0', 'dwj': '0', 'xgw': '0', 'xgl': '-3.1e-008', 'rshg': '8.23', 'gbmin': '1e-012', 'rbpb': '50', 'rbpd': '50', 'rbps': '50', 'rbdb': '50', 'rbsb': '50', 'saref': '1.00e-05', 'sbref': '1.00e-05', 'ngcon': '1', 'wlod': '5e-007', 'kvth0': '2.2e-009', 'lkvth0': '-1e-008', 'wkvth0': '2.2e-006', 'pkvth0': '-5e-014', 'llodvth': '1', 'wlodvth': '1', 'stk2': '2.5e-009', 'lodk2': '1', 'lodeta0': '2', 'ku0': '-3.2e-008', 'lku0': '2e-007', 'wku0': '7e-007', 'pku0': '-5e-014', 'llodku0': '1', 'wlodku0': '1', 'kvsat': '0.4', 'steta0': '-1.1e-010', 'tku0': '0.03', 'fnoimod': '1', 'noia': 'noian', 'noib': 'noibn', 'noic': 'noicn', 'em': '3.00e7', 'ef': '0.904', 'minr': '1e-3'}

    par_lmin='lmin'
    par_wmin='wmin'
    par_lmax='lmax'
    par_wmax='wmax'



    for key, value in all_parameters.items():
        # print(key)
        if par_lmin == key:
            par_lmin_val = value

        if par_wmin == key:
            par_wmin_val = value

        if par_lmax == key:
            par_lmax_val = value

        if par_wmax == key:
            par_wmax_val = value



    print(par_lmin_val)

    print(par_wmin_val)
    print(par_lmax_val)
    print(par_wmax_val)
    return(par_lmin_val,par_wmin_val,par_lmax_val,par_wmax_val)


    print(float(par_lmin_val))
    print(float(par_wmin_val))
    print(float(par_lmax_val))
    print(float(par_wmax_val))



    print(type(par_lmin_val))
    print(type(par_wmin_val))
    print(type(par_lmax_val))
    print(type(par_wmax_val))





