文章的思想是用投影的方法，将3D点云转成2D格式，之后backbone在这上面做语义分割

准备工作：
1.从git上下载代码；
2.数据集设置: dataset/kitti/sequences/00 01 02 03 04 05 08 11 12（与kitti.yaml对应）
每个00 01……文件夹下，包括labels和velodyne，测试集只有velodyne

使用步骤：
1.从头开始训练，结果保存到log2中，生成两个yaml参数文件、3个zip训练文件（没有train后缀）
./train.py -d ../../tasks/semantic/dataset/ -ac ../../tasks/semantic/config/arch/3dmininet-tiny.yaml -l ../../tasks/semantic/log2/
参数文件都保存在zip的bin中。

2.预测点云的语义，保存带label的点云到prediction中，利用log2中训练完的模型
./infer.py -d dataset/ -l prediction/ -m log2/

3.在验证集上评估MOU
./evaluate_iou.py -d dataset/kitti/ -p prediction/ --split valid

4.可视化：回到base主环境，在测试集11上进行分割
./visualize.py -d dataset/kitti/ -p prediction/ -s 11