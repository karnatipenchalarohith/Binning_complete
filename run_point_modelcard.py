
import os
from split_bins_intermediate import splitbins_intermediate as splitbins_intermediate
from create_netlist import createnetlist_pointmodel as createnetlist_pointmodel

#path = r'C:\Users\rkar\PycharmProjects\Binning'

current_location=os.getcwd()

files = []
for i in os.listdir(current_location):
    if os.path.isfile(os.path.join(current_location ,i)) and 'ZZ' in i:
        files.append(i)

print(files)




#path = r'C:\Users\rkar\PycharmProjects\Binning'
pointcard_files = []
for i in os.listdir(current_location):
    if os.path.isfile(os.path.join(current_location ,i)) and '_point_modelcard.scs' in i:
        pointcard_files.append(i)

print(pointcard_files)



filename='ZZ_Width_0.22_length_0.18_after_bins_joined.txt'
new_filename='Width_0.22_length_0.18_point_modelcard.scs'




lib_path =current_location + '/bin_reconstructed.scs'
corner =''

modelname ='modn'
m= 1


lmin='0.18e-6'
lmax='20e-6'

wmin='0.22e-6'
wmax='900e-6'


vgsMax ='3.3'
vgsStep='0.1'
vgsStart='0'


vdsMax ='3.3'
vdsStep='0.1'
vdsStart='0'


vdLin='0.1'
vdSat='3.3'

temp =25
terminals =4
nf1=1

wn='900e-6'
ln='19.99e-6'
m1=1

netlist_filename='netlist_scaling.sp'

netlist_filename_return=createnetlist_pointmodel(wn, ln, nf1, m1, vgsStart, vgsMax, vgsStep, vdsStart, vdsMax, vdsStep,vdSat, vdLin, temp, terminals,
                  lib_path, corner, modelname)


cmd = r'spectre ' + netlist_filename_return + ' +aps =log netlist_point1.log'
os.system(cmd)


