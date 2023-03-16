import os, glob

def write_sh(fl):
    sh_file = 'CCD_dataset_Insert blank frame [0].sh'
    image_path = fl


    content1='cd ../{}'.format(str(image_path)[-6:])
    content2='mv 000048.flo 000049.flo'
    content3 = 'mv 000047.flo 000048.flo'
    content4 = 'mv 000046.flo 000047.flo'
    content5 = 'mv 000045.flo 000046.flo'
    content6 = 'mv 000044.flo 000045.flo'
    content7 = 'mv 000043.flo 000044.flo'
    content8 = 'mv 000042.flo 000043.flo'
    content9 = 'mv 000041.flo 000042.flo'
    content10 = 'mv 000040.flo 000041.flo'
    content11 = 'mv 000039.flo 000040.flo'
    content12 = 'mv 000038.flo 000039.flo'
    content13 = 'mv 000037.flo 000038.flo'
    content14 = 'mv 000036.flo 000037.flo'
    content15 = 'mv 000035.flo 000036.flo'
    content16 = 'mv 000034.flo 000035.flo'
    content17 = 'mv 000033.flo 000034.flo'
    content18 = 'mv 000032.flo 000033.flo'
    content19 = 'mv 000031.flo 000032.flo'
    content20 = 'mv 000030.flo 000031.flo'
    content21 = 'mv 000029.flo 000030.flo'
    content22 = 'mv 000028.flo 000029.flo'
    content23 = 'mv 000027.flo 000028.flo'
    content24 = 'mv 000026.flo 000027.flo'
    content25 = 'mv 000025.flo 000026.flo'
    content26 = 'mv 000024.flo 000025.flo'
    content27 = 'mv 000023.flo 000024.flo'
    content28 = 'mv 000022.flo 000023.flo'
    content29 = 'mv 000021.flo 000022.flo'
    content30 = 'mv 000020.flo 000021.flo'
    content31 = 'mv 000019.flo 000020.flo'
    content32 = 'mv 000018.flo 000019.flo'
    content33 = 'mv 000017.flo 000018.flo'
    content34 = 'mv 000016.flo 000017.flo'
    content35 = 'mv 000015.flo 000016.flo'
    content36 = 'mv 000014.flo 000015.flo'
    content37 = 'mv 000013.flo 000014.flo'
    content38 = 'mv 000012.flo 000013.flo'
    content39 = 'mv 000011.flo 000012.flo'
    content40 = 'mv 000010.flo 000011.flo'
    content41 = 'mv 000009.flo 000010.flo'
    content42 = 'mv 000008.flo 000009.flo'
    content43 = 'mv 000007.flo 000008.flo'
    content44 = 'mv 000006.flo 000007.flo'
    content45 = 'mv 000005.flo 000006.flo'
    content46 = 'mv 000004.flo 000005.flo'
    content47 = 'mv 000003.flo 000004.flo'
    content48 = 'mv 000002.flo 000003.flo'
    content49 = 'mv 000001.flo 000002.flo'
    content50 = 'mv 000000.flo 000001.flo'
    content51='cp 111111.flo ./000000.flo'




    with open(sh_file, 'a') as f:
    
        f.write(content1 + '\n')
        f.write(content2 + '\n')
        f.write(content3 + '\n')
        f.write(content4 + '\n')
        f.write(content5 + '\n')
        f.write(content6 + '\n')
        f.write(content7 + '\n')
        f.write(content8 + '\n')
        f.write(content9 + '\n')
        f.write(content10 + '\n')
        f.write(content11 + '\n')
        f.write(content12 + '\n')
        f.write(content13 + '\n')
        f.write(content14 + '\n')
        f.write(content15 + '\n')
        f.write(content16 + '\n')
        f.write(content17 + '\n')
        f.write(content18 + '\n')
        f.write(content19 + '\n')
        f.write(content20 + '\n')
        f.write(content21 + '\n')
        f.write(content22 + '\n')
        f.write(content23 + '\n')
        f.write(content24 + '\n')
        f.write(content25 + '\n')
        f.write(content26 + '\n')
        f.write(content27 + '\n')
        f.write(content28 + '\n')
        f.write(content29 + '\n')
        f.write(content30 + '\n')
        f.write(content31 + '\n')
        f.write(content32 + '\n')
        f.write(content33 + '\n')
        f.write(content34 + '\n')
        f.write(content35 + '\n')
        f.write(content36 + '\n')
        f.write(content37 + '\n')
        f.write(content38 + '\n')
        f.write(content39 + '\n')
        f.write(content40 + '\n')
        f.write(content41 + '\n')
        f.write(content42 + '\n')
        f.write(content43 + '\n')
        f.write(content44 + '\n')
        f.write(content45 + '\n')
        f.write(content46 + '\n')
        f.write(content47 + '\n')
        f.write(content48 + '\n')
        f.write(content49 + '\n')
        f.write(content50 + '\n')
        f.write(content51 + '\n')


if __name__=="__main__":

    root_path = '/media/administrator/My Passport/video_jpg/testing/negative/flow_out'
    file_list = sorted(os.listdir(root_path))###sorted返回重新排序的列表。os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
    for fl in file_list:
        write_sh(root_path+fl)


####cd ../000002\cp 000098.flo.png ./000099.flo.png
