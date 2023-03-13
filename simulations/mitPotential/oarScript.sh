#!/bin/bash

#EXEC_DIR=/mnt/home/kkarimi/Project/git/hydrogenDiffusion/simulations/hydrogenDiffusionInAlMultipleTemp/Temp1000K
EXEC_DIR=/mnt/home/kkarimi/Project/git/lammps-27May2021/src 


MEAM_library_DIR=/mnt/home/kkarimi/Project/git/lammps-27May2021/src/../potentials

source /mnt/opt/spack-0.17/share/spack/setup-env.sh
spack load openmpi@4.0.5 %gcc@9.3.0
spack load openblas@0.3.18%gcc@9.3.0
spack load python@3.8.12%gcc@8.3.0

export LD_LIBRARY_PATH=/mnt/opt/tools/cc7/lapack/3.5.0-x86_64-gcc46/lib:${LD_LIBRARY_PATH}

#python3 --version
#python3 DislocateEdge.py  /mnt/home/kkarimi/Project/git/hydrogenDiffusion/simulations/lmpScripts 3.52 26.0 18.0 26.0 data_init.txt 4 2 1.0 0.0

#python3 --version
#python3 addAtom.py  /mnt/home/kkarimi/Project/git/hydrogenDiffusion/simulations/lmpScripts data_atom_added.txt 30

#srun $EXEC_DIR/lmp_g++_openmpi < in.minimization -echo screen -var OUT_PATH '.' -var PathEam ${MEAM_library_DIR} -var INC '/mnt/home/kkarimi/Project/git/hydrogenDiffusion/simulations/lmpScripts'  -var buff 0.0 -var nevery 1000 -var ParseData 1 -var DataFile data_atom_added.txt -var DumpFile dumpMin.xyz -var WriteData data_minimized.txt

srun $EXEC_DIR/lmp_g++_openmpi < in.relax -echo screen -var OUT_PATH '.' -var PathEam ${MEAM_library_DIR} -var INC '/mnt/home/kkarimi/Project/git/hydrogenDiffusion/simulations/lmpScripts'  -var buff 0.0 -var T 1000 -var nevery 10 -var ParseData 1 -var DataFile data_minimized.txt -var DumpFile dumpThermalized.xyz -var WriteData Equilibrated_1000.dat

