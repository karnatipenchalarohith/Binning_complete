#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 15:04:54 2022

@author: rkar
"""


#class createnetlist:
    
#createnetlist_scaling(lmin, lmax, wmin, wmax,m, vdLin, vdSat, vgsStart,vgsStep,vgsMax,vdsStart,vdsStep,vdsMax, temp, terminals, lib_path,corner, modelname)

# create Netlist
def createnetlist_scaling(lmin, lmax, wmin, wmax,m, vdLin, vdSat, vgsStart, vgsStep,vgsMax,vdsStart,vdsStep,vdsMax, temp, terminals, lib_path,corner, modelname,w,l,nf1,filename):
    
    #filename = "netlist_scaling.sp"
    
    # Open the file with writing permission
    myfile = open(filename, 'w')
    
    # Write a line to the file
    
    vss=0
    '''
    myfile.write('* Creating Netlist\n')
    
    myfile.write('.option brief\n')
    
    myfile.write('.option ingold=2\n')
    myfile.write('.option brief\n')
    myfile.write('.option brief\n')
    
   
    
    vdd = 1
    
    vgs_start = -0.5
    vgs_stop = 1.8
    vgs_step = 0.1
    vbs_start = 0
    vbs_stop = -0.8
    vbs_step = -0.2
    vdlin = 0.1
    vss = 0
    vbb = 0
    wn=1e-6
    ln=1e-6
    nf=1
    m=1
    temp=25
    terminals=4

     '''
    
    
    
    
    with open(filename, 'w') as f:
        f.write("* Creating ID-VG Netlist\n")
        f.write('.option brief \n')
        f.write('.option ingold=2\n')
        f.write('.option gmindc=1e-15\n')
        f.write('.param vdlin=' + str(vdLin) + '\n')
        
        f.write('.param vdSat=' + str(vdSat) + '\n')
        f.write('.param VGmax=' + str(vgsMax) + '\n')
        f.write('.param GG=0 \n')
    
        if terminals==5:
            f.write('m1  d g s b 0 ' + modelname + ' w=wn l=ln m=m1  nf=nf1 \n\n')
            f.write('m2  d0 g s b 0 ' + modelname + ' w=wn l=ln m=m1  nf=nf1 \n\n')

        elif terminals==6:
            f.write('m1  d g s b 0 0 ' + modelname + ' w=wn l=ln m=m1  nf=nf1 \n\n')
            f.write('m2  d0 g s b 0 0 ' + modelname + ' w=wn l=ln m=m1  nf=nf1 \n\n')

        else:
            f.write('m1  d g s b ' + modelname + ' w=wn l=ln m=m1  nf=nf1 \n\n')
            f.write('m2  d0 g s b ' + modelname + ' w=wn l=ln m=m1  nf=nf1 \n\n')
    
        f.write('vd d 0 vdlin \n')
        f.write('vd1 d0 0 vdSat \n')
        f.write('vs s 0 0 \n')
        f.write('vg g 0 GG \n')
        f.write('vb b 0 0 \n')

        f.write('.data device_size wn ln m1 nf1 \n')

        for item1 in w:
            for item2 in l:
                f.write(f' + {item1} {item2} {m} {nf1}\n')

        f.write(f'.enddata \n\n')


    
        f.write('.DC GG ' + str(vgsStart) + ' ' + str(vgsMax) +
                ' ' + str(vgsStep) + ' sweep ' + 'data=device_size ' + '\n')
    
        f.write('.temp ' + str(temp) + '\n')
        f.write('.meas dc vtlin find par(\'GG\') when par(\'(abs(i(vd)))\') = \'1e-7*(wn/ln)\' \n\n' )
        f.write('.meas dc vtsat find par(\'GG\') when par(\'(abs(i(vd1)))\') = \'1e-7*(wn/ln)\' \n\n' )
        f.write('.meas dc Idlin_nom find par(\'(abs(i(vd))/(wn))\') when par(\'GG\')=VGmax \n\n')
        f.write('.meas dc Idsat_nom find par(\'(abs(i(vd1))/(wn))\') when par(\'GG\')=VGmax \n\n')

        f.write('.inc ' + '\'' + lib_path + '\'  ' + corner + ' \n\n' )
        f.write('.end')
        
        return (filename)
    
    
    
    
    


def createnetlist_id_vd(wn,ln,nf,m,vds_start,vds_stop,vds_step,vgs_start,vgs_stop,vgs_step,vb,temp,terminals,lib_path,corner,modelname):
    
    filename = "netlist_id_vd.sp"
    
    # Open the file with writing permission
    myfile = open(filename, 'w')
    
    # Write a line to the file
    
    vss=0
    
    '''
    myfile.write('* Creating Netlist\n')
    
    myfile.write('.option brief\n')
    
    myfile.write('.option ingold=2\n')
    myfile.write('.option brief\n')
    myfile.write('.option brief\n')
    
   
    
    vdd = 1
    
    vgs_start = -0.5
    vgs_stop = 1.8
    vgs_step = 0.1
    vbs_start = 0
    vbs_stop = -0.8
    vbs_step = -0.2
    vdlin = 0.1
    vss = 0
    vbb = 0
    wn=1e-6
    ln=1e-6
    nf=1
    m=1
    temp=25
    terminals=4

     '''
    
    
    
    
    with open(filename, 'w') as f:
        f.write("* Creating ID-VG Netlist\n")
        f.write('.option brief \n')
        f.write('.option ingold=2\n')
        f.write('.param vdd=' + str(vds_start) + '\n')
        f.write('.param vgg=0 \n')
        f.write('.param vbb=' + str(vb) +  '\n')
        f.write('.param vss=' + str(vss) + '\n')
        f.write('.param VGmax=' + str(vgs_stop) + '\n')
    
        f.write('.param wn=' + str(wn) + '\n')
        f.write('.param ln=' + str(ln) + '\n')
        f.write('.param nf1=' + str(nf) + '\n')
        f.write('.param m1=' + str(m) + '\n\n')
    
        if terminals==5:
            f.write('m1  d g s b 0 ' + modelname + ' w=wn l=ln m=m1  nf=nf1 \n\n')
        elif terminals==6:
            f.write('m1  d g s b 0 0 ' + modelname + ' w=wn l=ln m=m1  nf=nf1 \n\n')
        else:
            f.write('m1  d g s b ' + modelname + ' w=wn l=ln m=m1  nf=nf1 \n\n')
    
        f.write('vd d 0 vdd \n')
        f.write('vs s 0 vss \n')
        f.write('vg g 0 vgg \n')
        f.write('vb b 0 vbb \n')
    
        f.write('.DC vdd ' + str(vds_start) + ' ' + str(vds_stop) +
                ' ' + str(vds_step) + ' sweep ' + 'vgg ' + str(vgs_start) +
                ' ' + str(vgs_stop) + ' ' + str(vgs_step) +   '\n')
    
        f.write('.temp ' + str(temp) + '\n')
        f.write('.meas dc vtlin find par(\'vgg\') when par(\'(abs(i(vd)))\') = \'1e-7*(wn/ln)\' \n\n' )
        f.write('.meas dc Idsat_abs find par(\'(abs(i(vd)))\') when par(\'vgg\')=VGmax \n\n')
        f.write('.meas dc Idsat_nom find par(\'(abs(i(vd))/(wn))\') when par(\'vgg\')=VGmax \n\n')
    
        f.write('.print par(\'-1*i(vd)\')\n\n' )
        f.write('.lib ' + '\'' + lib_path + '\'  ' + corner + ' \n\n' )
        f.write('.end')
    
    
    
    
    
    
    
    
    
















