import os, glob

def write_sh(fl):
    sh_file = 'flow2png2mp4.sh'
    image_path = fl


    content1='python -m flowiz demo/flo/{}/*.flo -o demo/png -v demo/mp4/{} --framerate 20'.format(str(image_path)[-6:], str(image_path)[-6:])
    





    with open(sh_file, 'a') as f:
        f.write(content1 + '\n')

if __name__=="__main__":

    root_path = '/media/administrator/18071801533/flowiz/demo/flo/'
    file_list = sorted(os.listdir(root_path))###sorted返回重新排序的列表。os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
    for fl in file_list:
        write_sh(root_path+fl)


####cd ../000002\cp 000098.flo.png ./000099.flo.png
