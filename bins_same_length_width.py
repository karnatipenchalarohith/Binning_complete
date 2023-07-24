import os
import re
import itertools as it

from collections import defaultdict


from split_bins_intermediate import splitbins_intermediate as splitbins_intermediate

def bins_same_length_width():


    words = ['lmin', 'lmax', 'wmin', 'wmax']

    all_list=[]
    final_list=[]
    current_location=os.getcwd()
    print(current_location)

    for root, _, files in os.walk(current_location):
        for path in filter(lambda p: p.endswith('modified.txt'), files):
            with open(os.path.join(root, path)) as f:
                for i, line in enumerate(f.readlines()):
                    for word in filter(lambda w: w in line, words):
                        print(f'{path}, {i+1}, {word}, {line.strip()}')
                        print(f' {line.strip()}')
                        reExp = re.compile("\s*([+-.\w]+)\s*=\s*([+-.\w]+)\s*", flags=re.S)
                        extLst = dict(reExp.findall(line.strip()))
                        print(extLst)
                        all_list=[path,extLst]
                        final_list.append(all_list)

    #                    all_list.append(path)
    #                    all_list.append(line.strip())
                        print(f'{path}')
                        keys = sorted(extLst.keys(), key=lambda k: extLst[k])
                        print(keys)
                        # Make sure `objs` with the same value be arranged next to each other
    #                    groups = it.groupby(keys, lambda k: d[k])  # so that we can group them by value
    #                    match_list = [list(keys) for v, keys in groups]
    #                    print(match_list)

    print(all_list)
    print(final_list)

    print(len(all_list))
    print(len(final_list))

    print(final_list[0])
    print(final_list[1])
    print(final_list[2])
    print(final_list[3])

    reExp = re.compile("\s*([+-.\w]+)\s*=\s*([+-.\w]+)\s*", flags=re.S)
    b = [el[1] for el in final_list]
    print(b)

    final_list_fin=[]

    print(final_list)

    bb={}
    bb_dummy={}

    cc=[]
    final_bb=[]
    your_blacklisted_set=['lmin','lmax','wmin','wmax']
    print(sorted(final_list))

    print(final_list[0])
    print(final_list[1])
    print(final_list[2])
    print(final_list[3])

    for el in final_list:
        print(el[0])
        print(el[1])
        for key in list(el[1].keys()):
            if key not in your_blacklisted_set:
                el[1].pop(key, None)


    #        print(el[1].pop('version', None))

    print(final_list)

    print(final_list[0])
    print(final_list[2])

    print(final_list[2][0])
    print(final_list[2][1])

    print(list(final_list[2][1]))

    print(final_list)
    print(list(final_list))

    old_dict={}



    for j in final_list:
        print (j[0])
        print (j[1])
        print(j[1].items())
        print(j[1])

        for i in list(j[1]):
            if i == 'lmin':
                j[1].update({'length': j[1].pop('lmin')})
            if i == 'lmax':
                j[1].update({'length': j[1].pop('lmax')})
            if i ==  'wmin':
                j[1].update({'width': j[1].pop('wmin')})
            if i ==  'wmax':
                j[1].update({'width': j[1].pop('wmax')})



    '''  
        for i in j[1]:
            print (i,j[1][i])
    '''



    '''
        if j[1].keys()=='lmin':
            j[1].update({'length': j[1].pop('lmin')})
    
    
        j[1].update({'length': j[1].pop('lmin', None)})
        j[1].update({'length': j[1].pop('lmax', None)})
        j[1].update({'width': j[1].pop('wmin', None)})
        j[1].update({'width': j[1].pop('wmax', None)})
    '''
    #    j[1]=dict(zip(['length'], my_dict.values()))

         #    old_dict.append(j[1])


    print(old_dict)
    print(final_list)


    '''
    print(final_list[0])
    print(final_list[1])
    print(final_list[2])
    
    print(final_list[3])
    
    print(final_list[4])
    
    '''


    '''
    final_dict={}
    
    for el in final_list:
        dumbo=el[1]
        for key in your_blacklisted_set:
            if key not in dumbo:
                del dumbo[key]
        print(dumbo)
    
    
    
    '''

    my_dict = {'old_key': 'old_value'}

    # Change the key name from 'old_key' to 'new_key'
    my_dict.update({'new_key': my_dict.pop('old_key')})

    # Print the updated dictionary
    print(my_dict)


    print(final_list)


    #    final_dict = {key: dumbo[key] for key, value in dumbo if key in your_blacklisted_set}

    '''
    for el in final_list:
        for key, value in el[1].items():
            bb={}
    #        print(el[1].items)
            if key in your_blacklisted_set:
                print(key,value)
                bb[key] = value
                print(bb)
                bb_dummy=bb
                cc.append(bb_dummy)
                continue
                
                
    '''
    #    final_bb.append(cc)
    #    print(cc)
    #print(final_bb)
    #       print(key)
    #        print(bb)
    #        print(el[0])
    #    cc=[el[0] bb]
    #    final_bb.append(cc)



    #            bb=dict(key:value)
    #            print(bb)
    #    final_list_fin=[el[0] ]



    #print(bb)
    #print(final_bb)



    '''
    b = [el[1] for el in final_list]
    reExp = re.compile("\s*([+-.\w]+)\s*=\s*([+-.\w]+)\s*", flags=re.S)
    extLst = dict(reExp.el[1])
    print(b)
    print(extLst)
    print(len(b))
    
    c = [el[0] for el in final_list]
    print(c)
    
    print(len(c))
    
    '''


    for j in final_list:
        print(j[0])
        print(j[1])
        print(j)

    #sorted(final_list.items(), key=lambda e: e[1][2])




    x = dict(a=1, b=2)
    y = dict(a=2, b=2)
    shared_items = {k: x[k] for k in x if k in y and x[k] == y[k]}

    print(shared_items)



    for l in final_list:
        print(l)



    totals = {}
    for k,v in final_list:
        totals[k] = totals.get(k, v)




    print(totals)

    print(len(totals))

    bbb=list(totals.values())

    print(bbb)
    for l in totals:
        print(l)
        print(totals[l])



    for n in bbb:
        print(n)


    i=0

    '''
    pp={}
    for n in bbb:
        for k in totals.keys() :
            if totals[k]==n:
                pp[n]=k
        i=i+1
    
    print(pp)
    
    
    '''


    #    d[n] = [k for k in totals.keys() if totals[k] == n]

    #    d[n] = [k for k in totals.keys() if totals[k] == n]


    # store the names (the keys of the new dict) as a set (keeps elements unique)
    #names = dict(totals.values())

    #print(names)

    '''
    # use a list comprehension, iterating through keys and checking the values match each n
    d = {}
    
    for n in bbb:
        d[n] = [k for k in totals.keys() if totals[k] == n]
    
    '''
    #print(d)
    # totals = {'a': 2, 'c': 2, 'b': 7}

    '''
    for k in x :
        if k in y and x[k] == y[k] :
            shared_items2 = {k: x[k]}
    
    print(shared_items2)
    '''

    '''
    out = {}
    for dct in lst:
        if "tier" in dct["data"]:
            out.setdefault(dct["platform"], {}).setdefault(dct["region"], {}).setdefault("tier", {}).setdefault((n := list(dct["data"]["tier"])[0]), {}).update(dct["data"]["tier"][n])
        else:
            out.setdefault(dct["platform"], {}).setdefault(
                dct["region"], {}
            ).setdefault((n := list(dct["data"])[0]), {}).update(dct["data"][n])
    
    print(out)
    
    '''

    print(totals)


    v = defaultdict(list)

    print(v)
    z=0
    for p in (totals.values()):
        z = z + 1
        for key, value in sorted(totals.items()):
            print(key)
            print(value)
            if totals[key] == p:
                v[z].append(key)



    print (v)


    print(totals)

    print(len(totals))


    mylist = list(dict.fromkeys(v))

    print(mylist)


    temp = []
    res = dict()
    for key, val in v.items():
        if val not in temp:
            temp.append(val)
            res[key] = val


    print(res)

    return (res)



    #    v[value].append(key)

