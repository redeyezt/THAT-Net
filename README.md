
#THAT-Net
Chinese

本项目主要是通过车载监控视频（仪表盘视频）（第一人称视频）来预测驾驶场景未来发生交通事故的概率。
关于代码的一切问题，如果有疑问，请与2453354394@qq.com联系，或者与zhangt725@foxmail.com联系。


# The latest research progress of traffic accident prediction.

#DSA

DSA, <a href="https://link.springer.com/chapter/10.1007/978-3-319-54190-7_9">. Chan, Fu-Hsiang, et al. "Anticipating accidents in dashcam videos." Computer Vision–ACCV 2016: 13th Asian Conference on Computer Vision, Taipei, Taiwan, November 20-24, 2016, Revised Selected Papers, Part IV 13. Springer International Publishing, 2017.

#UString
 
UString, <a href="https://dl.acm.org/doi/abs/10.1145/3394171.3413827">. Bao, Wentao, Qi Yu, and Yu Kong. "Uncertainty-based traffic accident anticipation with spatio-temporal relational learning." Proceedings of the 28th ACM International Conference on Multimedia. 2020.
#FA
 
FA, <a href="https://ieeexplore.ieee.org/abstract/document/9412338">. Fatima, Mishal, Muhammad Umar Karim Khan, and Chong-Min Kyung. "Global feature aggregation for accident anticipation." 2020 25th International Conference on Pattern Recognition (ICPR). IEEE, 2021.

#DSTA
 
DSTA, <a href="https://ieeexplore.ieee.org/document/9732278">. Karim, Muhammad Monjurul, et al. "A dynamic Spatial-temporal attention network for early anticipation of traffic accidents." IEEE Transactions on Intelligent Transportation Systems 23.7 (2022): 9590-9600.
 
#Comparative Performance Analysis of Accident Anticipation with Deep Learning Extractors
 
Comparative Performance Analysis of Accident Anticipation with Deep Learning Extractors, <a href="https://ieeexplore.ieee.org/abstract/document/10054736">. Mostak, Alfi Mashab, et al. "Comparative Performance Analysis of Accident Anticipation with Deep Learning Extractors." 2022 25th International Conference on Computer and Information Technology (ICCIT). IEEE, 2022.
 










我们方法的代码将在论文通过后第一时间发布。



本项目部分代码来自[UString](https://github.com/Cogito2012/UString)与[DSTA](https://github.com/redeyezt/DSTA),非常感谢这些存储库的贡献者，希望每日快乐。


English

This project is mainly to predict the probability of future traffic accidents in driving scenarios through vehicle surveillance video (dashboard video) (first-person video). For any questions about the code, please contact 2453354394@qq.com or zhangt725@foxmail.com.

The code of our method will be published as soon as the paper is approved.

Part of the code for this project comes from [UString](https://github.com/Cogito2012/UString) and [DSTA](https://github.com/redeyezt/DSTA). Many thanks to the contributors to these repositories. Happy daily.


这是我们提出的THAT-Net网络，主要针对车载监控设备拍摄的视频进行交通事故预测。

一，	准备数据集
我们在论文中的数据集有DAD数据集与CCD数据集，如果您想使用A3D数据集也可以。

下面给出各个数据集的下载连接：

DAD: https://github.com/smallcorgi/Anticipating-Accidents

CCD: https://github.com/Cogito2012/CarCrashDataset

A3D: https://github.com/MoonBlvd/tad-IROS2019。

由于A3D的部分视频丢失，您可以使用Bao等人整理后的A3D特征与视频帧图像，地址为：https://github.com/Cogito2012/UString

二，	进行提取光流
提取光流需要用到flownet2网络。地址为https://github.com/NVIDIA/flownet2-pytorch

（1）	创建环境

conda create -n flownet2 python=3.6.9

（2）	进入虚拟环境

conda activae flownet2

（3）	安装gcc7,g++7

sudo add-apt-repository ppa:ubuntu-toolchain-r/test

sudo apt-get update

sudo apt-get install gcc-7

sudo apt-get install g++-7

（4）	将gcc7，g++7作为默认选项

sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 100

sudo update-alternatives --config gcc
 
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-7 100

sudo update-alternatives --config g++

sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 50

（5）	查看所有gcc版本

ls /usr/bin/gcc*

（6）	查看当前gcc版本

gcc -v

（7）	安装pytorch

conda install pytorch==1.5.1 torchvision==0.6.1 cudatoolkit=10.1 -c pytorch

（8）	安装依赖包

pip install numpy

pip install tensorboardX

pip install setproctitle

pip install colorama

pip install tqdm

pip install scipy

pip install matplotlib

pip install pytz

pip install opencv-python

（9）	下载flownet代码

git clone https://github.com/NVIDIA/flownet2-pytorch.git

cd flownet2-pytorch

（10）	对以下文件进行修改

networks/channelnorm_package/setup.py

networks/resample2d_package/setup.py

networks/correlation_package/setup.py

将这三个文件中的{cxx_args = ['-std=c++11']}改为{cxx_args = ['-std=c++14']}

（11）	对以下文件进行修改

flownet2-pytorch/utils/frame_utils.py

将{from scipy.misc import imread}修改为{from imageio import imread}

（12）	对以下文件进行修改

flownet2-pytorch/datasets.py

将{ from scipy.misc import imread, imresize}修改为{ from imageio import imread}

（13）	对以下文件进行修改

flownet2-pytorch/networks/channelnorm_package/channelnorm.py

在第9行添加

input1 = input1.contiguous()

修改后的代码如下:


class ChannelNormFunction(Function):

      @staticmethod
      
      def forward(ctx, input1, norm_deg=2):
      
          input1 = input1.contiguous() # 新添加的代码
          
          assert input1.is_contiguous()
       
          
（14）	进入install.sh所在文件夹后输入如下命令

./install.sh

（15）	输入以下命令进行测试

python main.py -h

（16）	添加缺失的pip包

pip install modules_needed

（17）	inference测试，下载checkpoint文件

https://drive.google.com/file/d/1hF8vS6YeHkx3j2pfCeQqqZGwA_PJq_Da/view

（18）	inference测试

python main.py --inference \

    --model FlowNet2 \
    
    --save_flow \
    
    --inference_dataset MpiSintelClean \
    
    --inference_dataset_root ./datasets/MPI-Sintel/training \
    
    --inference_visualize \
    
--resume ./pre_train/FlowNet2_checkpoint.pth.tar

（19）	由视频数据集得到视频帧，即.mp4->.jpg

Python get_mp42jpg_sh.py

(这一步需要更改文件路径)

（20）	由视频帧图片得到光流图片，即.jpg->.flo

1.	python get_ jpg2flo _sh.py

2.	bash jpg2flo.sh

(这一步需要更改文件路径)

（21）	进入对应的flo文件夹，将一个空白光流图像放置于文件的首位。

（22）	由光流图片得到png图片，即.flo ->.png->mp4

这一步需要使用flowiz,代码地址为: https://github.com/georgegach/flowiz

git clone https://github.com/georgegach/flowiz.git

cd flowiz

python -m flowiz demo/flo/*.flo -o demo/png -v demo/mp4 --framerate 20

将步骤(21)得到的flo文件全部转化为MP4文件

（23）
cd VGG16 features from video

python extract_vgg16_dad.py

bash extract_vgg16_dad.sh

(这一步需要更改文件路径)

[![Page Views Count](https://badges.toozhao.com/badges/01GVG6QH0S1BY8TMGHYEXF63KW/blue.svg)](https://badges.toozhao.com/stats/01GVG6QH0S1BY8TMGHYEXF63KW "Get your own page views count badge on badges.toozhao.com")
