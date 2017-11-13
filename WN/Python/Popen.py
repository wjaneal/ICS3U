from subprocess import *

p = Popen('/usr/bin/python /home/william/LIA/SPH4U/Python/SphereFly.py',shell=True)
wait1 = raw_input()
print p

