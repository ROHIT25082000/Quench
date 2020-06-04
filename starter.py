import subprocess as sp
import os 
import platform
if platform.system() == 'Windows':
	sp.run("pythonw .\main.py",shell=True)
else:
	sp.run("python3 main.py &",shell= True)
	
