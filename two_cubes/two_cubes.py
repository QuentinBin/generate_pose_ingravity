'''
Description: None
Author: Bin Peng
Email: ustb_pengbin@163.com
Date: 2023-05-29 14:16:56
LastEditTime: 2023-05-29 19:20:46
'''
import pybullet as p
import time
p.connect(p.GUI)
cubes = p.loadSDF("/home/pengbin/code/pybullet/two_cubes/data/two_cubes.sdf")
print("cubes=",cubes)
while p.isConnected():
	p.stepSimulation()
	time.sleep(1./240.)
