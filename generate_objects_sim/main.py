'''
Description: Noney
Author: Bin Peng
Email: ustb_pengbin@163.com
Date: 2023-06-26 14:10:43
LastEditTime: 2023-06-26 22:24:52
'''
import pybullet as p
import pybullet_data
import time


from sim_env import SimEnv

def run():
    data_path = '/home/pengbin/code/pybullet/generate_objects_sim/model_data'
    
    cid = p.connect(p.GUI)
    env = SimEnv(p, data_path)

    env.load_single_obj(data_path+'/036_wood_block.obj')
    while True:
        time.sleep(1./240.)



if __name__ == '__main__':
    run()


