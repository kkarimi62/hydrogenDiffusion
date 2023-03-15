import sys
import os


lib_path = sys.argv[1]
inputt = sys.argv[2]
outpt = sys.argv[3]
natom = int(sys.argv[4])

sys.path.append(lib_path)
#import LammpsPostProcess2nd as lp

os.system('atomsk %s -add-atom H random %s final2nd.cfg'%(inputt,natom))
os.system('atomsk final2nd.cfg lmp')
os.system('mv final2nd.lmp %s'%outpt)

