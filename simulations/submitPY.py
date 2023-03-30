if __name__ == '__main__':
	import sys
	import os
	import numpy as np
	#---
	lnums = [ 36, 114  ]
	string=open('simulations.py').readlines() #--- python script
#	lnums = [ 33, 97   ]
#	string=open('simulations-ncbj.py').readlines() #--- python script
	#---
	n=6
	Temps  = dict(zip(range(2,n),range(2,n)))
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
				string[ inums ] = "\t6:\'hydrogenDiffusionInAlMultipleDisl/topo%s\',\n"%(temp) #--- change job name
			#---
				inums = lnums[ 1 ] - 1
				string[ inums ] = "\t\'p2\':\' %s 3.52 26.0 18.0 26.0 data_init.txt %temp 1 1.0\'%%(os.getcwd()+\'/lmpScripts\'),\n"%temp
#				string[ inums ] = "\t\'p7\':\' sortieproc.0 %s Topo_ignore\',\n"%(temp)
				
#				string[ inums ] = "\t72:\' -var buff 0.0 -var T %s -var nevery 10 -var ParseData 1 -var DataFile data_minimized.txt -var DumpFile dumpThermalized.xyz -var WriteData Equilibrated_%s.dat\',\n"%(temp,temp)
			#---
				sfile=open('junk%s.py'%count,'w');sfile.writelines(string);sfile.close()
				os.system( 'python junk%s.py'%count )
				os.system( 'rm junk%s.py'%count )
				count += 1
