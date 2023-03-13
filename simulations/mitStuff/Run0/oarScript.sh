#!/bin/bash

EXEC_DIR=/mnt/home/kkarimi/Project/git/hydrogenDiffusion/simulations/mitStuff

MEAM_library_DIR=/mnt/home/kkarimi/Project/git/lammps-27May2021/src/../potentials

source /mnt/opt/spack-0.17/share/spack/setup-env.sh
spack load openmpi@4.0.5 %gcc@9.3.0
spack load openblas@0.3.18%gcc@9.3.0
spack load python@3.8.12%gcc@8.3.0

export LD_LIBRARY_PATH=/mnt/opt/tools/cc7/lapack/3.5.0-x86_64-gcc46/lib:${LD_LIBRARY_PATH}

srun $EXEC_DIR/lmp_g++_openmpi < in.relax -echo screen -var OUT_PATH '.' -var PathEam ${MEAM_library_DIR} -var INC '/mnt/home/kkarimi/Project/git/hydrogenDiffusion/simulations/lmpScripts'  

