
## 基于虫情测报仪的昆虫计数项目

## 所需环境
tensorflow-gpu==2.2.0

1.将需要预测的图片放入img文件夹

2.运行predict文件，获取带标注的图像和每张图片对应的昆虫坐标的txt文件，图片保存在img_out文件夹，txt坐标文件map_out/image_locations保存在中

3.运行insect_count文件，获取每张图中昆虫总数目并写入txt，保存在count_file文件夹中

