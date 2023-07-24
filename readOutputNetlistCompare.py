#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 08:18:31 2023

@author: rkar
"""
from itertools import product
import re
import pandas as pd
import matplotlib.pyplot as plt

def readOutputNetlistCompare(filename1,filename2,w,l):
    

    vtsat_all_values = []
    vtlin_all_values = []
    idsat_all_values = []
    idlin_all_values = []
    
    #w=['900e-6','10e-6','1.23e-6','0.53e-6','0.22e-6']
    #l=['19.99e-6','10e-6','1.2e-6','0.5e-6','0.18e-6']
    
    netlist_file=filename1
    netlist_file_update=filename2
    
    ### first file
    
    reExp = re.compile("\s*([+-.\w]+)\s*=\s*([+-.\w]+)\s*", flags=re.S)
    c = 0
    with open(netlist_file) as file:
        file = file.readlines()
        for item in file:
            if item.strip().startswith('vtsat'):
    
                vtsat_value = reExp.findall(file[c + 3])
    
                vtsat_single = vtsat_value[0][1]
                vtsat_all_values.append(vtsat_single)
            if item.strip().startswith('vtlin'):
    
                vtlin_value = reExp.findall(file[c + 3])
    
                vtlin_single = vtlin_value[0][1]
                vtlin_all_values.append(vtlin_single)
            if item.strip().startswith('idlin_nom'):
    
                idlin_value = reExp.findall(file[c + 3])
    
                idlin_single = idlin_value[0][1]
                idlin_all_values.append(idlin_single)
            if item.strip().startswith('idsat_nom'):
    
                idsat_value = reExp.findall(file[c + 3])
    
                idsat_single = idsat_value[0][1]
                idsat_all_values.append(idsat_single)
    
            c = c + 1
    
    print(vtsat_all_values)
    print(len(vtsat_all_values))
    
    totalWL = pd.DataFrame(list(product(w, l)), columns=['w', 'l'])
    
    totalWL['vtsat'] = vtsat_all_values
    totalWL['vtlin'] = vtlin_all_values
    totalWL['idlin'] = idlin_all_values
    totalWL['idsat'] = idsat_all_values
    
    print(totalWL)
    
    #########
    
    
    
    ####### Seconf file
    
    
    vtsat_all_values_update = []
    vtlin_all_values_update = []
    idsat_all_values_update = []
    idlin_all_values_update = []
    
    reExp = re.compile("\s*([+-.\w]+)\s*=\s*([+-.\w]+)\s*", flags=re.S)
    c = 0
    with open(netlist_file_update) as file:
        file = file.readlines()
        for item in file:
            if item.strip().startswith('vtsat'):
    
                vtsat_value_update = reExp.findall(file[c + 3])
    
                vtsat_single_update = vtsat_value_update[0][1]
                vtsat_all_values_update.append(vtsat_single_update)
    
            if item.strip().startswith('vtlin'):
    
                vtlin_value_update = reExp.findall(file[c + 3])
    
                vtlin_single_update = vtlin_value_update[0][1]
                vtlin_all_values_update.append(vtlin_single_update)
            if item.strip().startswith('idlin_nom'):
    
                idlin_value_update = reExp.findall(file[c + 3])
    
                idlin_single_update = idlin_value_update[0][1]
                idlin_all_values_update.append(idlin_single_update)
            if item.strip().startswith('idsat_nom'):
    
                idsat_value_update = reExp.findall(file[c + 3])
    
                idsat_single_update = idsat_value_update[0][1]
                idsat_all_values_update.append(idsat_single_update)
    
    
            c = c + 1
    
    
    
    totalWL_update = pd.DataFrame(list(product(w, l)), columns=['w', 'l'])
    
    totalWL_update['vtsat'] = vtsat_all_values_update
    totalWL_update['vtlin'] = vtlin_all_values_update
    totalWL_update['idlin'] = idlin_all_values_update
    totalWL_update['idsat'] = idsat_all_values_update
    
    print(totalWL_update)
    
    
    #############
    
        
    item2 = ''
    for item in totalWL['w']:
    
        if item!=item2:
            #fig, ax = plt.subplots(2, 2, figsize=(15, 15))
            plt.subplot(2, 2, 1)
            #fig, ax = plt.subplots()
            plt.plot(pd.to_numeric(totalWL[totalWL.w == item]['l']), pd.to_numeric(totalWL[totalWL.w == item]['vtsat']),color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=4,label=str(item+'_old'))
            plt.plot(pd.to_numeric(totalWL_update[totalWL_update.w == item]['l']), pd.to_numeric(totalWL_update[totalWL_update.w == item]['vtsat']),color='red', linestyle='--', marker='o', markerfacecolor='black', markersize=4,label=str(item+'_new'))
            plt.xscale("log")
            plt.tight_layout()
            leg = plt.legend(loc='lower right', prop={'size': 5.5});
            plt.xlabel('Length(um)')
            plt.ylabel('vtsat(V)')
    
        if item!=item2:
            plt.subplot(2, 2, 2)
            #fig, ax = plt.subplots()
            plt.plot(pd.to_numeric(totalWL[totalWL.w == item]['l']), pd.to_numeric(totalWL[totalWL.w == item]['vtlin']),color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=4,label=str(item + '_old'))
            plt.plot(pd.to_numeric(totalWL_update[totalWL_update.w == item]['l']), pd.to_numeric(totalWL_update[totalWL_update.w == item]['vtlin']),color='red', linestyle='--', marker='o', markerfacecolor='black', markersize=4,label=str(item+'_new'))
            plt.xscale("log")
            leg = plt.legend(loc='lower right', prop={'size': 5.5});
            plt.xlabel('Length(um)')
            plt.ylabel('vtlin(V)')
        if item!=item2:
            plt.subplot(2, 2, 3)
            #fig, ax = plt.subplots()
            plt.plot(pd.to_numeric(totalWL[totalWL.w == item]['l']), pd.to_numeric(totalWL[totalWL.w == item]['idlin']),color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=4,label=str(item+ '_old'))
            plt.plot(pd.to_numeric(totalWL_update[totalWL_update.w == item]['l']), pd.to_numeric(totalWL_update[totalWL_update.w == item]['idlin']),color='red', linestyle='--', marker='o', markerfacecolor='black', markersize=4,label=str(item+ '_new'))
            plt.xscale("log")
            leg = plt.legend(loc='lower right', prop={'size': 5.5});
            plt.xlabel('Length(um)')
            plt.ylabel('idlin(uA/um)')
    
        if item!=item2:
            plt.subplot(2, 2, 4)
            #fig, ax = plt.subplots()
            plt.plot(pd.to_numeric(totalWL[totalWL.w == item]['l']), pd.to_numeric(totalWL[totalWL.w == item]['idsat']),color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=4,label=str(item+'_old'))
            plt.plot(pd.to_numeric(totalWL_update[totalWL_update.w == item]['l']), pd.to_numeric(totalWL_update[totalWL_update.w == item]['idsat']),color='red', linestyle='--', marker='o', markerfacecolor='black', markersize=4,label=str(item+ '_new'))
            plt.xscale("log")
            leg = plt.legend(loc='lower right', prop={'size': 5.5});
            plt.xlabel('Length(um)')
            plt.ylabel('idsat(uA/um)')
    
        item2=item
    #    plt.legend(item)
    #    plt.scatter(X, Y2, color='g')
    
    picname = "oldModle_Vs_NewModel_vs_Length.png"
    #plt.title(picname)
    plt.grid()
    plt.savefig(picname)
    plt.show()
    
    
    
    totalWL.sort_values(by=['l','w'], inplace=True,ascending = [False, False])
    
    
    
    print(totalWL)
    
    
    item2 = ''
    for item in totalWL['l']:
    
    
        if item!=item2:
            print(item)
            plt.subplot(2, 2, 1)
            #fig, ax = plt.subplots()
            plt.plot(pd.to_numeric(totalWL[totalWL.l == item]['w']), pd.to_numeric(totalWL[totalWL.l == item]['vtsat']), color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=4,label=str(item+'_old'))
            plt.plot(pd.to_numeric(totalWL_update[totalWL_update.l == item]['w']), pd.to_numeric(totalWL_update[totalWL_update.l == item]['vtsat']), color='red', linestyle='--', marker='o', markerfacecolor='black', markersize=4,label=str(item+'_new'))
            plt.xscale("log")
            plt.tight_layout()
            leg = plt.legend(loc='lower right', prop={'size': 5.5});
            plt.xlabel('Width(um)')
            plt.ylabel('vtsat(V)')
    
        if item!=item2:
            plt.subplot(2, 2, 2)
            #fig, ax = plt.subplots()
            plt.plot(pd.to_numeric(totalWL[totalWL.l == item]['w']), pd.to_numeric(totalWL[totalWL.l == item]['vtlin']), color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=4,label=str(item+'_old'))
            plt.plot(pd.to_numeric(totalWL_update[totalWL_update.l == item]['w']), pd.to_numeric(totalWL_update[totalWL_update.l == item]['vtlin']), color='red', linestyle='--', marker='o', markerfacecolor='black', markersize=4,label=str(item+'_new'))
            plt.xscale("log")
            leg = plt.legend(loc='lower right', prop={'size': 5.5});
            plt.xlabel('Width(um)')
            plt.ylabel('vtlin(V)')
        if item!=item2:
            plt.subplot(2, 2, 3)
            #fig, ax = plt.subplots()
            plt.plot(pd.to_numeric(totalWL[totalWL.l == item]['w']), pd.to_numeric(totalWL[totalWL.l == item]['idlin']), color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=4,label=str(item+'_old'))
            plt.plot(pd.to_numeric(totalWL_update[totalWL_update.l == item]['w']), pd.to_numeric(totalWL_update[totalWL_update.l == item]['idlin']), color='red', linestyle='--', marker='o', markerfacecolor='black', markersize=4,label=str(item+'_new'))
            plt.xscale("log")
            leg = plt.legend(loc='lower right', prop={'size': 5.5});
            plt.xlabel('Width(um)')
            plt.ylabel('idlin(uA/um)')
    
        if item!=item2:
            plt.subplot(2, 2, 4)
            #fig, ax = plt.subplots()
            plt.plot(pd.to_numeric(totalWL[totalWL.l == item]['w']), pd.to_numeric(totalWL[totalWL.l == item]['idsat']), color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=4,label=str(item+'_old'))
            plt.plot(pd.to_numeric(totalWL_update[totalWL_update.l == item]['w']), pd.to_numeric(totalWL_update[totalWL_update.l == item]['idsat']), color='red', linestyle='--', marker='o', markerfacecolor='black', markersize=4,label=str(item+'_new'))
            plt.xscale("log")
            leg = plt.legend(loc='lower right', prop={'size': 5.5});
            plt.xlabel('Width(um)')
            plt.ylabel('idsat(uA/um)')
    
        item2=item
    #    plt.legend(item)
    #    plt.scatter(X, Y2, color='g')
    picname = "oldModle_Vs_NewModel_vs_Width.png"
    #plt.title(picname)
    plt.grid()
    plt.savefig(picname)
    plt.show()
    
    
'''    
    item2 = ''
    for item in totalWL['w']:
    
        if item!=item2:
            #fig, ax = plt.subplots(2, 2, figsize=(15, 15))
            plt.subplot(2, 2, 1)
            #fig, ax = plt.subplots()
            plt.plot(pd.to_numeric(totalWL[totalWL.w == item]['l']), pd.to_numeric(totalWL[totalWL.w == item]['vtsat']),color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=4,label=item)
            plt.plot(pd.to_numeric(totalWL_update[totalWL_update.w == item]['l']), pd.to_numeric(totalWL_update[totalWL_update.w == item]['vtsat']),color='red', linestyle='--', marker='o', markerfacecolor='black', markersize=4,label=item)
            plt.xscale("log")
            leg = plt.legend();
            plt.xlabel('Length(um)')
            plt.ylabel('vtsat(V)')
    
        if item!=item2:
            plt.subplot(2, 2, 2)
            #fig, ax = plt.subplots()
            plt.plot(pd.to_numeric(totalWL[totalWL.w == item]['l']), pd.to_numeric(totalWL[totalWL.w == item]['vtlin']),color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=4,label=item)
            plt.plot(pd.to_numeric(totalWL_update[totalWL_update.w == item]['l']), pd.to_numeric(totalWL_update[totalWL_update.w == item]['vtlin']),color='red', linestyle='--', marker='o', markerfacecolor='black', markersize=4,label=item)
            plt.xscale("log")
            leg = plt.legend();
            plt.xlabel('Length(um)')
            plt.ylabel('vtlin(V)')
        if item!=item2:
            plt.subplot(2, 2, 3)
            #fig, ax = plt.subplots()
            plt.plot(pd.to_numeric(totalWL[totalWL.w == item]['l']), pd.to_numeric(totalWL[totalWL.w == item]['idlin']),color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=4,label=item)
            plt.plot(pd.to_numeric(totalWL_update[totalWL_update.w == item]['l']), pd.to_numeric(totalWL_update[totalWL_update.w == item]['idlin']),color='red', linestyle='--', marker='o', markerfacecolor='black', markersize=4,label=item)
            plt.xscale("log")
            leg = plt.legend();
            plt.xlabel('Length(um)')
            plt.ylabel('idlin(uA/um)')
    
        if item!=item2:
            plt.subplot(2, 2, 4)
            #fig, ax = plt.subplots()
            plt.plot(pd.to_numeric(totalWL[totalWL.w == item]['l']), pd.to_numeric(totalWL[totalWL.w == item]['idsat']),color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=4,label=item)
            plt.plot(pd.to_numeric(totalWL_update[totalWL_update.w == item]['l']), pd.to_numeric(totalWL_update[totalWL_update.w == item]['idsat']),color='red', linestyle='--', marker='o', markerfacecolor='black', markersize=4,label=item)
            plt.xscale("log")
            leg = plt.legend();
            plt.xlabel('Length(um)')
            plt.ylabel('idsat(uA/um)')
    
        item2=item
    #    plt.legend(item)
    #    plt.scatter(X, Y2, color='g')
    plt.show()
    
    
    
    totalWL.sort_values(by=['l','w'], inplace=True,ascending = [False, False])
    
    
    
    print(totalWL)
    
    
    item2 = ''
    for item in totalWL['l']:
    
    
        if item!=item2:
            print(item)
            plt.subplot(2, 2, 1)
            #fig, ax = plt.subplots()
            plt.plot(pd.to_numeric(totalWL[totalWL.l == item]['w']), pd.to_numeric(totalWL[totalWL.l == item]['vtsat']), color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=4,label=item)
            plt.plot(pd.to_numeric(totalWL_update[totalWL_update.l == item]['w']), pd.to_numeric(totalWL_update[totalWL_update.l == item]['vtsat']), color='red', linestyle='--', marker='o', markerfacecolor='black', markersize=4,label=item)
            plt.xscale("log")
            leg = plt.legend();
            plt.xlabel('Width(um)')
            plt.ylabel('vtsat(V)')
    
        if item!=item2:
            plt.subplot(2, 2, 2)
            #fig, ax = plt.subplots()
            plt.plot(pd.to_numeric(totalWL[totalWL.l == item]['w']), pd.to_numeric(totalWL[totalWL.l == item]['vtlin']), color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=4,label=item)
            plt.plot(pd.to_numeric(totalWL_update[totalWL_update.l == item]['w']), pd.to_numeric(totalWL_update[totalWL_update.l == item]['vtlin']), color='red', linestyle='--', marker='o', markerfacecolor='black', markersize=4,label=item)
            plt.xscale("log")
            leg = plt.legend();
            plt.xlabel('Width(um)')
            plt.ylabel('vtlin(V)')
        if item!=item2:
            plt.subplot(2, 2, 3)
            #fig, ax = plt.subplots()
            plt.plot(pd.to_numeric(totalWL[totalWL.l == item]['w']), pd.to_numeric(totalWL[totalWL.l == item]['idlin']), color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=4,label=item)
            plt.plot(pd.to_numeric(totalWL_update[totalWL_update.l == item]['w']), pd.to_numeric(totalWL_update[totalWL_update.l == item]['idlin']), color='red', linestyle='--', marker='o', markerfacecolor='black', markersize=4,label=item)
            plt.xscale("log")
            leg = plt.legend();
            plt.xlabel('Width(um)')
            plt.ylabel('idlin(uA/um)')
    
        if item!=item2:
            plt.subplot(2, 2, 4)
            #fig, ax = plt.subplots()
            plt.plot(pd.to_numeric(totalWL[totalWL.l == item]['w']), pd.to_numeric(totalWL[totalWL.l == item]['idsat']), color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=4,label=item)
            plt.plot(pd.to_numeric(totalWL_update[totalWL_update.l == item]['w']), pd.to_numeric(totalWL_update[totalWL_update.l == item]['idsat']), color='red', linestyle='--', marker='o', markerfacecolor='black', markersize=4,label=item)
            plt.xscale("log")
            leg = plt.legend();
            plt.xlabel('Width(um)')
            plt.ylabel('idsat(uA/um)')
    
        item2=item
    #    plt.legend(item)
    #    plt.scatter(X, Y2, color='g')
    plt.show()
    
'''    
    
'''    
        if totalWL.w == item:
            plt.plot(pd.to_numeric(totalWL[totalWL.w == item]['l']),pd.to_numeric(totalWL[totalWL.w == item]['vtsat']))
            plt.show()
'''
    #    plt.plot(pd.to_numeric(totalWL[totalWL.w == item]['l']),pd.to_numeric(totalWL[totalWL.w == item]['vtsat']))
    #    plt.show()
    
    #    plt.scatter(float(totalWL[float(totalWL.w) == float(item)]['w']), float(totalWL[float(totalWL.w) == float(item)['vtsat']]))
    #    plt.show()
    
    
    #plt.scatter(totalWL[totalWL.reg==1]['vol'], totalWL[totalWL.reg==0]['vol'])
    
    #plt.show()