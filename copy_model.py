#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 10:10:32 2023

@author: rkar
"""




def copy_model(filename):
    
    #filename='modn.sp'
    filename_copy='modn_copy.sp'
    
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    
    with open(filename_copy, "w") as f:
        f.write("simulator lang=spectre insensitive=yes \n")
        for line in lines:
            f.write(line)
        f.write("}")