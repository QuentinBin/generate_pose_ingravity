'''
Description: object to urdf 
Author: Bin Peng
Email: ustb_pengbin@163.com
Date: 2023-06-26 21:23:13
LastEditTime: 2023-06-26 22:20:03
'''
import os
import sys
import glob
from object2urdf import ObjectUrdfBuilder


# # build URDFs
# obj_file_path = '/home/pengbin/code/pybullet/generate_objects_sim/model_data'
# obj_path_list = glob.glob(os.path.join(obj_file_path, '*.obj'))
# # print(os.path.basename(obj_path_list[0]).replace('.obj', '.urdf'))


# if __name__ == '__main__':
#     for i, obj_path in enumerate(obj_path_list):
#         urdf_path = os.path.basename(obj_path).replace('.obj', '.urdf')
#         print(urdf_path)
#         builder = ObjectUrdfBuilder(obj_file_path, urdf_prototype=urdf_path)
#         builder.build_urdf(filename=obj_path,  force_overwrite=True, decompose_concave=True, force_decompose=False, center = 'mass')


# Build entire libraries of URDFs
object_folder = "/home/pengbin/code/pybullet/generate_objects_sim/model_data"
builder = ObjectUrdfBuilder(object_folder)
builder.build_library(force_overwrite=True, decompose_concave=True, force_decompose=False, center = 'mass')