if __name__ == '__main__':
	import sys
	import os
	import numpy as np
	#---
	lnums = [ 36, 120  ]
	string=open('simulations.py').readlines() #--- python script
#	lnums = [ 33, 97   ]
#	string=open('simulations-ncbj.py').readlines() #--- python script
	#---
	n=89
	Temps  = dict(zip(range(n),range(n)))
#			{
#				0:300,
#				1:600,
#				2:700,
#				3:800,
#				4:900,
#				5:1000,
#			}
	#---
	count = 0
	for keys_t in Temps:
				temp = Temps[keys_t]
			#---	densities
				inums = lnums[ 0 ] - 1
				string[ inums ] = "\t3:\'hydrogenDiffusionInAlMultipleTopo/topo%s\',\n"%(temp) #--- change job name
			#---
				inums = lnums[ 1 ] - 1
				string[ inums ] = "\t\'p7\':\' sortieproc.0 %s Topo_ignore\',\n"%(temp)
				
#				string[ inums ] = "\t72:\' -var buff 0.0 -var T %s -var nevery 10 -var ParseData 1 -var DataFile data_minimized.txt -var DumpFile dumpThermalized.xyz -var WriteData Equilibrated_%s.dat\',\n"%(temp,temp)
			#---
				sfile=open('junk%s.py'%count,'w');sfile.writelines(string);sfile.close()
				os.system( 'python junk%s.py'%count )
				os.system( 'rm junk%s.py'%count )
				count += 1
