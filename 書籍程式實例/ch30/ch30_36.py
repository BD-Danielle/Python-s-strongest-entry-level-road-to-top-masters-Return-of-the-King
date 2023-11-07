# ch30_36.py
import subprocess

#ret = subprocess.run('echo %date%', shell=True, stdout=subprocess.PIPE)
ret = subprocess.run('echo %date%', shell=True)
print("資料型態           = ", type(ret))
print("列印ret  = ", ret)
print("列印ret.stdout", ret.stdout)






