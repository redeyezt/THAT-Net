from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import cv2
import glob
import os

path = 'E:\\master\\cv2_video_fig\\shiyan/'

path_file_number = glob.glob('E:\\master\\cv2_video_fig\\shiyan/*.mp4')
file_number = glob.glob(pathname='*.mp4')


#print(path_file_number)
#print(len(path_file_number))
#print(path_file_number[0])
#print('----------------------------------------')
#print(str(path_file_number[0])[-10:-4])

def get_each_frame(video_path):
    # 读取视频文件
    videoCapture = cv2.VideoCapture(video_path)
    # 读帧
    success, frame = videoCapture.read()
    i = 0
    # 设置固定帧率
    timeF = 1  # 帧率,根据情况自行修改合适的帧率
    j = 0
    while success:
        i = i + 1
        if (i % timeF == 0):
            j = j + 1

            address = path + name+'/' + str(j) + '.jpg'
            #print(address)
            cv2.imwrite(address, frame)
            #print('save image:', i)
        success, frame = videoCapture.read()



# get_each_frame(r"E:\master\cv2_video_fig\dataset\000348\000348.mp4")



a=0
print(path_file_number)
while a<len(path_file_number):
    path = 'E:\\master\\cv2_video_fig\\shiyan/'
    name = str(path_file_number[a])[-10:-4]
    isexists = os.path.exists(path + name )
    if not isexists:
        os.makedirs(path + name)

    get_each_frame(path_file_number[a])
    a=a+1








