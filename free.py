"""
    @ code by ---( Younis john )---
    @ Github : https://github.com/YounisXyz
    @ WhatsApp : https://wa.me/923194999455
    
"""
import os, sys, platform
 
os.system('rm -rf WEHSHI.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf WEHSHI.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('WEHSHI.so'):
        os.system('curl -L https://github.com/YounisXyz/executables/blob/main/WEHSHI.cpython-312.so?raw=true -o WEHSHI.so') 
        import WEHSHI
    else:
        import WEHSHI
elif bit == '32bit':
    print("\033[0m\033[91m Sorry Your Device Is 32bit, This Tool 32bit Not Sported, Only For \033[92m64Bit\033[0m ]");exit() 
