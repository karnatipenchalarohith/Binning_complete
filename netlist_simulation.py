import shutil

import os
from create_netlist_scaling import createnetlist_scaling as createnetlist_scaling
from readOutputNetlistScaling import readOutputNetlistScaling as readOutputNetlistScaling
from readOutputNetlistCompare import readOutputNetlistCompare as readOutputNetlistCompare
from copy_model import copy_model as copy_model

current_location=os.getcwd()

print(current_location)

constructed_file='bin_reconstructed.scs'

constructed_file_path=str(current_location + '/' + constructed_file)

print(constructed_file_path)

first_constructed_file='bin_reconstructed_first.scs'

target_file=str(current_location + '/' + first_constructed_file)

shutil.copy(constructed_file_path, target_file)
originalFileName='modn.sp'
copy_model(originalFileName)


lib_path = str(current_location + '/' + 'modn_copy.sp')
#lib_path ='/user/rkar/data_from_tp/Binning/formed_files/bin_reconstructed.scs'


corner =''

modelname ='modn'
m= 1


lmin='0.18e-6'
lmax='20e-6'

wmin='0.22e-6'
wmax='900e-6'


vgsMax ='1.8'
vgsStep='0.1'
vgsStart='0'


vdsMax ='1.8'
vdsStep='0.1'
vdsStart='0'


vdLin='0.1'
vdSat='1.8'

temp =25
terminals =4
nf1=1

w=['900e-6','10e-6','1.23e-6','0.53e-6','0.22e-6']
l=['19.99e-6','10e-6','1.2e-6','0.5e-6','0.18e-6']

netlist_filename='netlist_scaling.sp'

netlist_filename_return=createnetlist_scaling(lmin, lmax, wmin, wmax,m, vdLin, vdSat, vgsStart,vgsStep,vgsMax,vdsStart,vdsStep,vdsMax, temp, terminals, lib_path,corner, modelname,w,l,nf1,netlist_filename)

# createnetlist(w,l,nf.)


cmd = r'spectre ' + netlist_filename_return + ' +aps =log netlist1.log'
os.system(cmd)


readOutputNetlistScaling('netlist_scaling.measure',w,l)

lib_path_updated=target_file
#lib_path_updated='/user/rkar/data_from_tp/Binning/formed_files/bin_recons_new.scs'

netlist_filename_new='netlist_scaling_new.sp'

netlist_filename_return_new=createnetlist_scaling(lmin, lmax, wmin, wmax,m, vdLin, vdSat, vgsStart,vgsStep,vgsMax,vdsStart,vdsStep,vdsMax, temp, terminals, lib_path_updated,corner, modelname,w,l,nf1,netlist_filename_new)



cmd = r'spectre ' + netlist_filename_return_new + ' +aps =log netlist1.log'
os.system(cmd)



readOutputNetlistScaling('netlist_scaling_new.measure',w,l)



readOutputNetlistCompare('netlist_scaling.measure','netlist_scaling_new.measure',w,l)





