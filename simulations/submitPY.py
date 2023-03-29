if __name__ == '__main__':
	import sys
	import os
	import numpy as np
	#---
	lnums = [ 36  ]
	string=open('simulations.py').readlines() #--- python script
#	lnums = [ 33, 97   ]
#	string=open('simulations-ncbj.py').readlines() #--- python script
	#---
	topo_ids = list(map(int,open('Topo_ignore_original').readlines()))
	Topo = dict(zip(range(len(topo_ids)),topo_ids))

	Temps  = {
#				0:300,
#				1:600,
#				2:700,
#				3:800,
#				4:900,
				5:1000,
			}
	#---
	count = 0
	for keys_t in Topo:
				temp = Topo[keys_t]
				
				#--- remove
				with open('Topo_ignore','w') as sfile:
					np.savetxt(sfile,np.c_[topo_ids - [temp]],fmt='%d')
				

			#---	densities
				inums = lnums[ 0 ] - 1
				string[ inums ] = "\t6:\'hydrogenDiffusionInAlMultipleTopo/Topo%s\',\n"%(keys_t) #--- change job name
			#---
#				inums = lnums[ 1 ] - 1
#				string[ inums ] = "\t72:\' -var buff 0.0 -var T %s -var nevery 10 -var ParseData 1 -var DataFile data_minimized.txt -var DumpFile dumpThermalized.xyz -var WriteData Equilibrated_%s.dat\',\n"%(temp,temp)
			#---
				sfile=open('junk%s.py'%count,'w');sfile.writelines(string);sfile.close()
				os.system( 'python junk%s.py'%count )
				os.system( 'rm junk%s.py'%count )
				count += 1
