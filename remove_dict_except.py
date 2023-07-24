



import re

def remove_dict_except(df):
    words = ['lmin', 'lmax', 'wmin', 'wmax']


    for item in words:
        if item=='lmin':
            lmin_value = df['lmin']
        if item=='lmax':
            lmax_value = df['lmax']
        if item=='wmin':
            wmin_value = df['wmin']
        if item=='wmax':
            wmax_value = df['wmax']

    df.clear()

    df['lmin']=lmin_value
    df['lmax'] = lmax_value
    df['wmin'] = wmin_value
    df['wmax'] = wmax_value




    return df




