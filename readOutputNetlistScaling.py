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

def readOutputNetlistScaling(filename,w,l):
    vtsat_all_values = []
    vtlin_all_values = []
    idsat_all_values = []
    idlin_all_values = []
    
    #w=['900e-6','10e-6','1.23e-6','0.53e-6','0.22e-6']
    #l=['19.99e-6','10e-6','1.2e-6','0.5e-6','0.18e-6']
    
    reExp = re.compile("\s*([+-.\w]+)\s*=\s*([+-.\w]+)\s*", flags=re.S)
    c = 0
    with open(filename) as file:
        file = file.readlines()
        for item in file:
            if item.strip().startswith('vtsat'):
                print(item)
                print(file[c + 3])
                vtsat_value = reExp.findall(file[c + 3])
                print(vtsat_value)
                print(vtsat_value[0][1])
                vtsat_single = vtsat_value[0][1]
                vtsat_all_values.append(vtsat_single)
            if item.strip().startswith('vtlin'):
                print(item)
                print(file[c + 3])
                vtlin_value = reExp.findall(file[c + 3])
                print(vtlin_value)
                print(vtlin_value[0][1])
                vtlin_single = vtlin_value[0][1]
                vtlin_all_values.append(vtlin_single)
            if item.strip().startswith('idlin_nom'):
                print(item)
                print(file[c + 3])
                idlin_value = reExp.findall(file[c + 3])
                print(idlin_value)
                print(idlin_value[0][1])
                idlin_single = idlin_value[0][1]
                idlin_all_values.append(idlin_single)
            if item.strip().startswith('idsat_nom'):
                print(item)
                print(file[c + 3])
                idsat_value = reExp.findall(file[c + 3])
                print(idsat_value)
                print(idsat_value[0][1])
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
    
    
    item2 = ''
    for item in totalWL['w']:
    
        if item!=item2:
            plt.subplot(2, 2, 1)
            #fig, ax = plt.subplots()
            plt.plot(pd.to_numeric(totalWL[totalWL.w == item]['l']), pd.to_numeric(totalWL[totalWL.w == item]['vtsat']),color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=4,label=item)
            leg = plt.legend(loc='lower right', prop={'size': 5.5});
            plt.tight_layout()
            plt.xscale("log")
            plt.xlabel('Length(um)')
            plt.ylabel('vtsat(V)')
    
        if item!=item2:
            plt.subplot(2, 2, 2)
            #fig, ax = plt.subplots()
            plt.plot(pd.to_numeric(totalWL[totalWL.w == item]['l']), pd.to_numeric(totalWL[totalWL.w == item]['vtlin']),color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=4,label=item)
            leg = plt.legend(loc='lower right', prop={'size': 5.5});
            plt.xscale("log")
            plt.xlabel('Length(um)')
            plt.ylabel('vtlin(V)')
        if item!=item2:
            plt.subplot(2, 2, 3)
            #fig, ax = plt.subplots()
            plt.plot(pd.to_numeric(totalWL[totalWL.w == item]['l']), pd.to_numeric(totalWL[totalWL.w == item]['idlin']),color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=4,label=item)
            leg = plt.legend(loc='lower right', prop={'size': 5.5});
            plt.xscale("log")
            plt.xlabel('Length(um)')
            plt.ylabel('idlin(uA/um)')
    
        if item!=item2:
            plt.subplot(2, 2, 4)
            #fig, ax = plt.subplots()
            plt.plot(pd.to_numeric(totalWL[totalWL.w == item]['l']), pd.to_numeric(totalWL[totalWL.w == item]['idsat']),color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=4,label=item)
            leg = plt.legend(loc='lower right', prop={'size': 5.5});
            plt.xscale("log")
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
            leg = plt.legend(loc='lower right', prop={'size': 5.5});
            plt.xscale("log")
            plt.tight_layout()
            plt.xlabel('Width(um)')
            plt.ylabel('vtsat(V)')
    
        if item!=item2:
            plt.subplot(2, 2, 2)
            #fig, ax = plt.subplots()
            plt.plot(pd.to_numeric(totalWL[totalWL.l == item]['w']), pd.to_numeric(totalWL[totalWL.l == item]['vtlin']), color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=4,label=item)
            leg = plt.legend(loc='lower right', prop={'size': 5.5});
            plt.xscale("log")
            plt.xlabel('Width(um)')
            plt.ylabel('vtlin(V)')
        if item!=item2:
            plt.subplot(2, 2, 3)
            #fig, ax = plt.subplots()
            plt.plot(pd.to_numeric(totalWL[totalWL.l == item]['w']), pd.to_numeric(totalWL[totalWL.l == item]['idlin']), color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=4,label=item)
            leg = plt.legend(loc='lower right', prop={'size': 5.5});
            plt.xscale("log")
            plt.xlabel('Width(um)')
            plt.ylabel('idlin(uA/um)')
    
        if item!=item2:
            plt.subplot(2, 2, 4)
            #fig, ax = plt.subplots()
            plt.plot(pd.to_numeric(totalWL[totalWL.l == item]['w']), pd.to_numeric(totalWL[totalWL.l == item]['idsat']), color='green', linestyle='-', marker='o', markerfacecolor='blue', markersize=4,label=item)
            leg = plt.legend(loc='lower right', prop={'size': 5.5});
            plt.xscale("log")
            plt.xlabel('Width(um)')
            plt.ylabel('idsat(uA/um)')
    
        item2=item
    #    plt.legend(item)
    #    plt.scatter(X, Y2, color='g')
    plt.show()
    
    


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