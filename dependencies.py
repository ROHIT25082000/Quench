import subprocess as sp 
import os , platform
if platform.system() == 'Windows':
    sp.run('pip install plyer', shell=True)
if platform.system() == 'Linux':
    sp.run('pip3 install plyer',shell=True)


