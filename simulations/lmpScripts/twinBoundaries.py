import numpy as np
import pandas as pd
import pdb
import sys
import os
import pdb

def WriteDataFile(AtomskOutpt, mass, ratios, LmpInput):
    #--- read data file
    lmpData = lp.ReadDumpFile( AtomskOutpt )
    lmpData.ReadData()
    #--- atom obj
    atoms = lp.Atoms( **lmpData.coord_atoms_broken[0].to_dict(orient='series') )
    #--- box
    box = lp.Box( BoxBounds = lmpData.BoxBounds[0],AddMissing = np.array([0.0,0.0,0.0] ) )
    #--- wrap
    wrap = lp.Wrap( atoms, box )
    wrap.WrapCoord()
    wrap.Set( atoms )
    #--- center
    #--- add box bounds
#    rcent = np.matmul(box.CellVector,np.array([.5,.5,.5]))
#    box.CellOrigin -= rcent
#    loo=box.CellOrigin
#    hii=box.CellOrigin+np.matmul(box.CellVector,np.array([1,1,1]))
#    box.BoxBounds=np.c_[loo,hii,np.array([0,0,0])]

#    atoms.x -= rcent[0]
#    atoms.y -= rcent[1]
#    atoms.z -= rcent[2]

    if len(mass) > 1: #--- multi-component alloy: assign random types
        types = list(mass.keys())
        types.sort()		

        dff=pd.DataFrame(atoms.__dict__)
        itype = 0#1
        typei = types[itype]
        dff['type']=typei
        indices = dff.index
        ntype=len(mass)
        sizeTot = len(dff)

		#--- add up to one!
        sizes = (ratios * sizeTot).astype(int)
        sizes[-1] = sizeTot - np.sum(sizes[:-1])
        sizes=dict(zip(types,sizes))
		
#        assert size * ntype <= sizeTot
        indxxx = {}
        for itype in range(1,ntype):
            typei = types[itype]
            size = sizes[typei]
            indxxx[typei] = np.random.choice(indices, size=size, replace=None)
#            dff.iloc[indxxx[itype]]['type'] = ntype - itype
            row_indexer = indxxx[typei]
            col_indexer = 'type'
            dff.loc[row_indexer,col_indexer] = typei 
            indices = list(set(indices)-set(indxxx[typei]))
            sizeTot -= size		
        atoms = lp.Atoms( **dff.to_dict(orient='series') )
#        pdb.set_trace()	
    #--- write data file
    lp.WriteDataFile(atoms,box,mass).Write(LmpInput)

pathlib = sys.argv[1]
sys.path.append(pathlib)
import LammpsPostProcess as lp


#--- modify atom types and associated masses 
if __name__ == '__main__':
#--- modify atom types and associated masses 
    ntype = int(sys.argv[7])
    types = np.array(list(map(int,sys.argv[8:8+ntype])))
    mass=dict(zip(types,np.random.random(size=ntype))) #{1:58.693, # Ni
    ratio = np.array(list(map(float,sys.argv[8+ntype:])))
#        2:58.933195, # Co

#    mass={#1:63.55, #cu
#		1:58.693, # Ni
 #       2:58.933195, # Co
  #      3:51.9961 #Cr,
   #    } 
	#
    a = float(sys.argv[2]) #3.52
    lx, ly, lz = float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]) #40.0, 20.0, 40.0 Angstrom
    m,n,k = int(lx/a*4.0**(1.0/3)), int(ly/a), int(lz/a)
    #
    var1=int(n/2)
    var2=m+1
    #
    bmag = a / 2.0 ** 0.5
    os.system('rm *.cfg *.lmp *.xyz *.xsf')
    #--- Crystallographic orientation of the system
	#--- construct unit cell
    os.system('atomsk --create fcc %s Al orient 11-2 111 -110 Al_unitcell.cfg'%a)
#    os.system('atomsk --create fcc %s Ni orient 111 11-2 -110 Al_unitcell.cfg'%a)
#    os.system('atomsk --create fcc %s Al orient 110 -111 1-12 Al_unitcell.cfg'%a)
	#--- duplicate
    os.system('atomsk Al_unitcell.cfg -duplicate %s %s %s Al_supercell.cfg'%(m,n,k))
	#--- build twin boundary
    for i in range(1):
        os.system('atomsk Al_supercell.cfg -mirror 0 Y -wrap Al_supercell_mirror.cfg')
        os.system('atomsk --merge Y 2 Al_supercell.cfg Al_supercell_mirror.cfg data.cfg')
        os.system('mv data.cfg Al_supercell.cfg;rm Al_supercell_mirror.cfg')
    os.system('mv Al_supercell.cfg data.cfg')
	#--- output
    os.system('atomsk data.cfg -center com final.cfg')
    os.system('atomsk final.cfg lmp')
    #

if ntype == 1:
    os.system('mv final.lmp %s'%sys.argv[6])
else:
    WriteDataFile('final.lmp',mass, ratio, sys.argv[6])
os.system('rm *.cfg *.xsf *.lmp')

