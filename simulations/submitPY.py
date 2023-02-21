if __name__ == '__main__':
	import sys
	import os
	import numpy as np
	#---
#	lnums = [ 30, 90, 86   ]
#	string=open('simulations.py').readlines() #--- python script
	lnums = [ 33, 94   ]
	string=open('simulations-ncbj.py').readlines() #--- python script
	#---
	Temps  = {
				0:300,
				1:600,
				2:700,
				3:800,
				4:900,
				5:1200,
				6:1400,
#				7:1600,
			}
	Rates  = {
#				0:0.5e-4,
#				1:1e-4,
#				2:4e-4,
#				3:8e-4,
#				4:8e-3,
#				5:8e-2,
			}
	#---
	count = 0
	for keys_t in Temps:
		temp = Temps[keys_t]
		for keys_r in Rates:
			#---
				rate = Rates[keys_r]
			#---	densities
				inums = lnums[ 0 ] - 1
				string[ inums ] = "\t3:\'hydrogenDiffusionInAlMultipleTemp/Temp%sK\',\n"%(temp) #--- change job name
			#---
				inums = lnums[ 1 ] - 1
				string[ inums ] = "\t7:\' -var buff 0.0 -var T %s -var P 0.0 -var nevery 100 -var ParseData 1 -var DataFile data_minimized.txt -var DumpFile dumpThermalized.xyz -var WriteData Equilibrated_%s.dat\',\n"%(temp,temp)
			#---
				sfile=open('junk%s.py'%count,'w');sfile.writelines(string);sfile.close()
				os.system( 'python junk%s.py'%count )
				os.system( 'rm junk%s.py'%count )
				count += 1
