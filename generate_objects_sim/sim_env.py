'''
Description: simulated environment
Author: Bin Peng
Email: ustb_pengbin@163.com
Date: 2023-06-22 16:12:05
LastEditTime: 2023-06-26 22:25:00
'''
import pybullet as p
import pybullet_data
import math
import numpy as np
import glob, os, random
import utils

class SimEnv(object):
    def __init__(self, bullet_client, obj_filepath=None) -> None:
        self.p = bullet_client
        self.p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.p.loadURDF("plane.urdf", [0, 0, 0])  # load the plane
        self.p.setGravity(0, 0, -9.8) # set gravity
        self.p.setPhysicsEngineParameter(numSolverIterations=10)
        self.p.setTimeStep(1. / 120.)
        # #disable rendering during creation.
        # self.p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 0)
        # self.p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
        # #disable tinyrenderer, software (CPU) renderer, we don't use it here
        self.p.configureDebugVisualizer(p.COV_ENABLE_TINY_RENDERER, 0)

        self.p.setRealTimeSimulation(1)

    def load_single_obj(self, obj_path, meshScale=[1,1,1], shift=[0,0,0]):
        # self.p.loadURDF("cube.urdf", [0,3,2],useMaximalCoordinates = True)
        self.p.loadURDF("/home/pengbin/code/pybullet/generate_objects_sim/model_data/036_wood_block.urdf", [0,1,0.5], flags=p.URDF_USE_SELF_COLLISION)
        # visual_shape_ID = p.createVisualShape(shapeType=p.GEOM_MESH,
        #                             fileName=obj_path,
        #                             rgbaColor=[1, 1, 1, 1],
        #                             specularColor=[0.4, .4, 0],
        #                             visualFramePosition=shift,
        #                             meshScale=meshScale)
        
        # collision_shape_ID = p.createCollisionShape(shapeType=p.GEOM_MESH,
        #                                   fileName=obj_path,
        #                                   collisionFramePosition=shift,
        #                                   meshScale=meshScale)
        
        # # random orientation
        # baseEuler = [random.uniform(0, 2*math.pi), random.uniform(0, 2*math.pi), random.uniform(0, 2*math.pi)]
        # baseOrientation = self.p.getQuaternionFromEuler(baseEuler)
        
        # uid = p.createMultiBody(baseMass=1,
        #               baseInertialFramePosition=[0, 0, 0],
        #               baseCollisionShapeIndex=collision_shape_ID,
        #               baseVisualShapeIndex=visual_shape_ID,
        #               basePosition=[0 * meshScale[0] * 2,
        #                             0 * meshScale[1] * 2, 1],
        #               baseOrientation=baseOrientation,
        #               useMaximalCoordinates=True)