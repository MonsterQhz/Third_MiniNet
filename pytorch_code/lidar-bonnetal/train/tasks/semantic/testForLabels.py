import open3d as o3d
import numpy as np
points = np.fromfile("/home/sci/project/Third_MiniNet/pytorch_code/lidar-bonnetal/train/tasks/semantic/dataset/kitti/sequences/08/velodyne/000037.bin", dtype=np.float32).reshape(-1, 4)
label = np.fromfile("/home/sci/project/Third_MiniNet/pytorch_code/lidar-bonnetal/train/tasks/semantic/prediction/sequences/08/predictions/000037.label", dtype=np.uint32).reshape((-1))
clouds=points[:,:3]
colors=np.zeros([len(label),3])
for cla in range(len(label)):
    #print(label[cla])
    # if label[cla] == 40 or label[cla] == 44 or label[cla] == 48 or label[cla] == 49:
    #     colors[cla][0]=1
    #     colors[cla][1]=0
    #     colors[cla][2]=0
    # else:
    #     colors[cla][0]=0
    #     colors[cla][1]=1
    #     colors[cla][2]=0
    if label[cla]!=10:
        colors[cla][0] = 1
        colors[cla][1] = 0
        colors[cla][2] = 0
        print("********************")
    print("label is %s" % label[cla])
test_pcd = o3d.geometry.PointCloud()
test_pcd.points = o3d.utility.Vector3dVector(clouds)
test_pcd.colors = o3d.utility.Vector3dVector(colors)

o3d.visualization.draw_geometries([test_pcd], window_name="Open3D2")

