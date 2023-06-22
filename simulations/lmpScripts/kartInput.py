import pdb
import sys
import numpy as np


path = sys.argv[1]
output = sys.argv[2]
lib_path = sys.argv[3]
temp = sys.argv[4]

sys.path.append(lib_path)
import LammpsPostProcess2nd as lp

#--- read lammps data file
rd = lp.ReadDumpFile(path)
rd.ReadData()

#--- output readable format for kart 
[lx,ly,lz] = rd.BoxBounds[0].astype(float)[:,1]-rd.BoxBounds[0].astype(float)[:,0]
df = rd.coord_atoms_broken[ 0 ]
#pdb.set_trace()

(xlo,ylo,zlo) = rd.BoxBounds[0].astype(float)[:,0]
#--- output
sfile = open(output,'w')
sfile.write('run_id:            0\ntotal energy :    0.0000\n')
sfile.write('%s\t%s\t%s\n'%(lx,ly,lz))
np.savetxt(sfile,np.c_[df.type,df.x-xlo,df.y-ylo,df.z-zlo],fmt='%i %s %s %s')
sfile.close()

sfile = open('.natom.txt','w')
sfile.write( '%s\n'%(len(df)))
sfile.close()

sfile = open('.lx.txt','w')
sfile.write( '%s\n'%lx)
sfile.close()

sfile = open('.ly.txt','w')
sfile.write( '%s\n'%ly)
sfile.close()

sfile = open('.lz.txt','w')
sfile.write( '%s\n'%lz)
sfile.close()

sfile = open('.temp.txt','w')
sfile.write( '%s\n'%temp)
sfile.close()
