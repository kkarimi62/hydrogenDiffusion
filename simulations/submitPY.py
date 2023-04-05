if __name__ == '__main__':
	import sys
	import os
	import numpy as np
	#---
	lnums = [ 36, 116  ]
	string=open('simulations.py').readlines() #--- python script
#	lnums = [ 33, 97   ]
#	string=open('simulations-ncbj.py').readlines() #--- python script
	#---
	Temps=			{
				0:1200,
				1:1400,
				2:1600,
				3:1800,
				4:2000,
			}
	#---
	count = 0
	for keys_t in Temps:
				temp = Temps[keys_t]
			#---	densities
				inums = lnums[ 0 ] - 1
				string[ inums ] = "\t6:\'hydrogenDiffusionInAlBigMultipleTemps/temp%s\',\n"%(keys_t) #--- change job name
			#---
				inums = lnums[ 1 ] - 1
				string[ inums ] = "\t\'p3\':\' data_minimized.txt init_xyz.conf %%s %s\'%%(os.getcwd()+\'/lmpScripts\'),\n"%temp
#				string[ inums ] = "\t\'p21\':\' %%s 3.52 %s 18.0 26.0 data_init.txt 2 2 1.0 0.0\'%%(os.getcwd()+\'/lmpScripts\'),\n"%temp
#				string[ inums ] = "\t\'p7\':\' sortieproc.0 %s Topo_ignore\',\n"%(temp)
				
#				string[ inums ] = "\t72:\' -var buff 0.0 -var T %s -var nevery 10 -var ParseData 1 -var DataFile data_minimized.txt -var DumpFile dumpThermalized.xyz -var WriteData Equilibrated_%s.dat\',\n"%(temp,temp)
			#---
				sfile=open('junk%s.py'%count,'w');sfile.writelines(string);sfile.close()
				os.system( 'python junk%s.py'%count )
				os.system( 'rm junk%s.py'%count )
				count += 1
