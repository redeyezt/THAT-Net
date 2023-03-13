import os, glob

def write_sh(fl):
    sh_file = 'flownet_dad_train_nega_3.sh'
    image_path = fl
    flow_path = str(fl)[0:-6]+'flow_out'
    if not os.path.exists(flow_path):###如果不存在flow_path，则创建flow_path
        os.mkdir(flow_path)
    content=\
        'CUDA_VISIBLE_DEVICES=3 python main.py --inference --model FlowNet2 --number_gpu 1\
        --inference_dataset_iext jpg \
        --save_flow --inference_dataset ImagesFromFolder \
        --resume /media/administrator/b11512ec-3b41-4ff9-8ab9-b048dc11432b/hongyanjin/flownet2-pytorch-master/checkpoints/FlowNet2_checkpoint.pth.tar \
        --save {} \
        --inference_dataset_root {}'.format(flow_path, image_path)


    '''
    content = 'CUDA_VISIBLE_DEVICES=2 python main.py --inference --model FlowNet2 \
        --save_flow --inference_dataset ImagesFromFolder \
        --resume /media/administrator/b11512ec-3b41-4ff9-8ab9-b048dc11432b/hongyanjin/flownet2-pytorch-master/checkpoints/FlowNet2_checkpoint.pth.tar \
        --save /media/administrator/b11512ec-3b41-4ff9-8ab9-b048dc11432b/hongyanjin/flownet2-pytorch-master/output \
        --inference_dataset_root /media/administrator/b11512ec-3b41-4ff9-8ab9-b048dc11432b/hongyanjin/flownet2-pytorch-master/data/000821 \
        --inference_dataset_iext jpg \
        --number_gpus 1
    '''

    with open(sh_file, 'a') as f:
        f.write(content + '\n')

if __name__=="__main__":

    root_path = '/media/administrator/My Passport/video_jpg/training/negative/'
    file_list = sorted(os.listdir(root_path))###sorted返回重新排序的列表。os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
    for fl in file_list:
        write_sh(root_path+fl)
