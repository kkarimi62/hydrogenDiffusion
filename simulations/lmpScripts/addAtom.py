import sys
import os


lib_path = sys.argv[1]
inputt = sys.argv[2]
outpt = sys.argv[3]
natom = int(sys.argv[4])

sys.path.append(lib_path)
#import LammpsPostProcess2nd as lp

os.system('atomsk %s -add-atom H random %s final.cfg'%(inputt,natom))
os.system('atomsk final.cfg lmp')
os.system('mv final.lmp %s'%outpt)
os.system('rm *.cfg')

