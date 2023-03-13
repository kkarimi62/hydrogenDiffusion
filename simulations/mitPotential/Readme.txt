1. Two versions of the potential files are provided:
   a) frozen_model.pb is the raw potential file from DeepMD-kit.
   b) compressed_model.pb is the compressed model of 'frozen_model.pb'. This one is more efficient in running MD, but may reduce a little bit of accuracy (usually it is negligible).

2. in.relax is an example input file for LAMMPS.

3. init.lmp is an example input configuration to run in.relax.

4. Hydrogen element is included due to the interest on H embrittlement on our side. No need to change the potential and mass related part in in.relax, to run a Co-Cr-Fe-Mn system.
