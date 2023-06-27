import numpy as np
import pandas as pd
import pdb
import sys
import os
import pdb

def GetDim():
    os.system('atomsk Al_supercell.cfg -center com final.cfg')
    os.system('atomsk final.cfg lmp')

    
    lmpData = lp.ReadDumpFile( 'final.lmp' )
    lmpData.ReadData()
    atoms = lmpData.coord_atoms_broken[0]
    box = lp.Box( BoxBounds = lmpData.BoxBounds[0],AddMissing = np.array([0.0,0.0,0.0] ) )

    return atoms, box
    
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
		
        dff=pd.DataFrame(atoms.__dict__)
        itype = 1
        dff['type']=itype
        indices = dff.index
        ntype=len(mass)
        sizeTot = len(dff)

		#--- add up to one!
        sizes = (ratios * sizeTot).astype(int)
        sizes[-1] = sizeTot - np.sum(sizes[:-1])
        sizes=dict(zip(range(1,ntype+1),sizes))
		
#        assert size * ntype <= sizeTot
        indxxx = {}
        for itype in range(2,ntype+1):
            size = sizes[itype]
            indxxx[itype] = np.random.choice(indices, size=size, replace=None)
#            dff.iloc[indxxx[itype]]['type'] = ntype - itype
            row_indexer = indxxx[itype]
            col_indexer = 'type'
            dff.loc[row_indexer,col_indexer] = itype 
            indices = list(set(indices)-set(indxxx[itype]))
            sizeTot -= size		
        atoms = lp.Atoms( **dff.to_dict(orient='series') )
#        pdb.set_trace()	
    #--- write data file
    lp.WriteDataFile(atoms,box,mass).Write(LmpInput)

pathlib = sys.argv[1]
sys.path.append(pathlib)
import LammpsPostProcess2nd as lp


#--- modify atom types and associated masses 
ntype = int(sys.argv[9])
mass=dict(zip(range(1,ntype+1),np.random.random(size=ntype)))
ratio = np.array(list(map(float,sys.argv[10:])))
#
a = float(sys.argv[2])
lx, ly, lz = float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
method = sys.argv[7]
radius = float(sys.argv[8])
m,n,k = int(lx/a*4.0**(1.0/3)), int(ly/a), int(lz/a)
#
var1=int(n/2)
var2=m+1
#
bmag = a / 2.0 ** 0.5
os.system('rm *.cfg *.lmp *.xyz *.xsf')
#--- Crystallographic orientation of the system
os.system('atomsk --create fcc %s Al orient 110 -111 1-12 Al_unitcell.cfg'%a) #--- atomask example
#os.system('atomsk --create fcc %s Al orient 11-2 111 -110 Al_unitcell.cfg'%a)
#os.system('atomsk --create fcc 4.046 Al orient [11-2] [111] [-110] -duplicate 28 14 30 Al_supercell.xsf')
os.system('atomsk Al_unitcell.cfg -duplicate %s %s %s Al_supercell.cfg'%(m,n,k))

#--- Introduce an edge dislocation at constant number of atoms
if method == '0':
    #--- no dislocation
    os.system('mv Al_supercell.cfg data.cfg')
if method == '6':
#    radius = 5.0 #* bmag
#    os.system('atomsk Al_supercell.cfg -disloc loop  0.501*box 0.501*box 0.501*box Y %s %s 0.0 0.0 0.33 data.cfg'%(radius,bmag)) #--- glide loop
#    os.system('atomsk Al_supercell.cfg -dislocation loop  0.5*box 0.5*box 0.5*box Y %s 0.0 -%s 0.0 0.33 data.cfg'%(radius,bmag)) #--- frank loop

    atoms, box = GetDim() #--- parse coords
#    pdb.set_trace() 
    h = a/3**.5 #--- spacing in y
    rc = np.matmul(box.CellVector,0.5*np.array([1,1,1]))+box.CellOrigin #--- box center
    #--- bounds for center plane
    ymin = rc[1]-0.5*h
    ymax = rc[1]+0.5*h
    #--- mask atoms
    filtr = np.all([atoms.y >= ymin, atoms.y < ymax,
		    (atoms.x-rc[0])**2+(atoms.z-rc[2])**2 < radius ** 2],axis=0)
    #--- print
    atoms = lp.Atoms( **atoms[~filtr].to_dict(orient='series') )
    lp.WriteDataFile(atoms,box,{1:1.0}).Write('final.lmp')
#    os.system('atomsk Al_supercell.cfg -select in cylinder Y 0.5*box 0.5*box %s -select rm below %s Y -select rm above %s Y -remove-atoms select data.cfg'%(radius,ymin,ymax))
#    os.system('atomsk Al_supercell.cfg -select in cylinder Y 0.5*box 0.5*box %s -select rm below 0.45*box Y -select rm above 0.55*box Y -remove-atoms select data.cfg'%(radius))

    #--- check that only one plane is selected!!!

#    os.system('atomsk Al_supercell.xsf -dislocation loop 0.5*box 0.5*box 0.5*box Y 7 0 0 2.336 0.33 data.cfg')

#os.system('atomsk data.cfg -center com final.cfg')
if method != '6':
    os.system('atomsk data.cfg final.cfg')
    os.system('atomsk final.cfg lmp')
#
if ntype == 1:
    os.system('mv final.lmp %s'%sys.argv[6])
else:
    WriteDataFile('final.lmp',mass, ratio, sys.argv[6])
os.system('rm *.cfg *.xsf *.lmp')



