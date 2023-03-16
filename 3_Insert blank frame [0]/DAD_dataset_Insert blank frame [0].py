import os, glob

def write_sh(fl):
    sh_file = 'DAD_dataset_Insert blank frame [0].sh'
    image_path = fl


    content1  ='cd ../{}'.format(str(image_path)[-6:])
    content2  = 'mv 000098.flo 000099.flo'
    content3  = 'mv 000097.flo 000098.flo'
    content4  = 'mv 000096.flo 000097.flo'
    content5  = 'mv 000095.flo 000096.flo'
    content6  = 'mv 000094.flo 000095.flo'
    content7  = 'mv 000093.flo 000094.flo'
    content8  = 'mv 000092.flo 000093.flo'
    content9  = 'mv 000091.flo 000092.flo'
    content10 = 'mv 000090.flo 000091.flo'
    content11 = 'mv 000089.flo 000090.flo'
    content12 = 'mv 000088.flo 000089.flo'
    content13 = 'mv 000087.flo 000088.flo'
    content14 = 'mv 000086.flo 000087.flo'
    content15 = 'mv 000085.flo 000086.flo'
    content16 = 'mv 000084.flo 000085.flo'
    content17 = 'mv 000083.flo 000084.flo'
    content18 = 'mv 000082.flo 000083.flo'
    content19 = 'mv 000081.flo 000082.flo'
    content20 = 'mv 000080.flo 000081.flo'
    content21 = 'mv 000079.flo 000080.flo'
    content22 = 'mv 000078.flo 000079.flo'
    content23 = 'mv 000077.flo 000078.flo'
    content24 = 'mv 000076.flo 000077.flo'
    content25 = 'mv 000075.flo 000076.flo'
    content26 = 'mv 000074.flo 000075.flo'
    content27 = 'mv 000073.flo 000074.flo'
    content28 = 'mv 000072.flo 000073.flo'
    content29 = 'mv 000071.flo 000072.flo'
    content30 = 'mv 000070.flo 000071.flo'
    content31 = 'mv 000069.flo 000070.flo'
    content32 = 'mv 000068.flo 000069.flo'
    content33 = 'mv 000067.flo 000068.flo'
    content34 = 'mv 000066.flo 000067.flo'
    content35 = 'mv 000065.flo 000066.flo'
    content36 = 'mv 000064.flo 000065.flo'
    content37 = 'mv 000063.flo 000064.flo'
    content38 = 'mv 000062.flo 000063.flo'
    content39 = 'mv 000061.flo 000062.flo'
    content40 = 'mv 000060.flo 000061.flo'
    content41 = 'mv 000059.flo 000060.flo'
    content42 = 'mv 000058.flo 000059.flo'
    content43 = 'mv 000057.flo 000058.flo'
    content44 = 'mv 000056.flo 000057.flo'
    content45 = 'mv 000055.flo 000056.flo'
    content46 = 'mv 000054.flo 000055.flo'
    content47 = 'mv 000053.flo 000054.flo'
    content48 = 'mv 000052.flo 000053.flo'
    content49 = 'mv 000051.flo 000052.flo'
    content50 = 'mv 000050.flo 000051.flo'
    content51 = 'mv 000049.flo 000050.flo'
    content52 = 'mv 000048.flo 000049.flo'
    content53 = 'mv 000047.flo 000048.flo'
    content54 = 'mv 000046.flo 000047.flo'
    content55 = 'mv 000045.flo 000046.flo'
    content56 = 'mv 000044.flo 000045.flo'
    content57 = 'mv 000043.flo 000044.flo'
    content58 = 'mv 000042.flo 000043.flo'
    content59 = 'mv 000041.flo 000042.flo'
    content60 = 'mv 000040.flo 000041.flo'
    content61 = 'mv 000039.flo 000040.flo'
    content62 = 'mv 000038.flo 000039.flo'
    content63 = 'mv 000037.flo 000038.flo'
    content64 = 'mv 000036.flo 000037.flo'
    content65 = 'mv 000035.flo 000036.flo'
    content66 = 'mv 000034.flo 000035.flo'
    content67 = 'mv 000033.flo 000034.flo'
    content68 = 'mv 000032.flo 000033.flo'
    content69 = 'mv 000031.flo 000032.flo'
    content70 = 'mv 000030.flo 000031.flo'
    content71 = 'mv 000029.flo 000030.flo'
    content72 = 'mv 000028.flo 000029.flo'
    content73 = 'mv 000027.flo 000028.flo'
    content74 = 'mv 000026.flo 000027.flo'
    content75 = 'mv 000025.flo 000026.flo'
    content76 = 'mv 000024.flo 000025.flo'
    content77 = 'mv 000023.flo 000024.flo'
    content78 = 'mv 000022.flo 000023.flo'
    content79 = 'mv 000021.flo 000022.flo'
    content80 = 'mv 000020.flo 000021.flo'
    content81 = 'mv 000019.flo 000020.flo'
    content82 = 'mv 000018.flo 000019.flo'
    content83 = 'mv 000017.flo 000018.flo'
    content84 = 'mv 000016.flo 000017.flo'
    content85 = 'mv 000015.flo 000016.flo'
    content86 = 'mv 000014.flo 000015.flo'
    content87 = 'mv 000013.flo 000014.flo'
    content88 = 'mv 000012.flo 000013.flo'
    content89 = 'mv 000011.flo 000012.flo'
    content90 = 'mv 000010.flo 000011.flo'
    content91 = 'mv 000009.flo 000010.flo'
    content92 = 'mv 000008.flo 000009.flo'
    content93 = 'mv 000007.flo 000008.flo'
    content94 = 'mv 000006.flo 000007.flo'
    content95 = 'mv 000005.flo 000006.flo'
    content96 = 'mv 000004.flo 000005.flo'
    content97 = 'mv 000003.flo 000004.flo'
    content98 = 'mv 000002.flo 000003.flo'
    content99 = 'mv 000001.flo 000002.flo'
    content100 = 'mv 000000.flo 000001.flo'
    content101='cp 111111.flo ./000000.flo'




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
        f.write(content52 + '\n')
        f.write(content53 + '\n')
        f.write(content54 + '\n')
        f.write(content55 + '\n')
        f.write(content56 + '\n')
        f.write(content57 + '\n')
        f.write(content58 + '\n')
        f.write(content59 + '\n')
        f.write(content60 + '\n')
        f.write(content61 + '\n')
        f.write(content62 + '\n')
        f.write(content63 + '\n')
        f.write(content64 + '\n')
        f.write(content65 + '\n')
        f.write(content66 + '\n')
        f.write(content67 + '\n')
        f.write(content68 + '\n')
        f.write(content69 + '\n')
        f.write(content70 + '\n')
        f.write(content71 + '\n')
        f.write(content72 + '\n')
        f.write(content73 + '\n')
        f.write(content74 + '\n')
        f.write(content75 + '\n')
        f.write(content76 + '\n')
        f.write(content77 + '\n')
        f.write(content78 + '\n')
        f.write(content79 + '\n')
        f.write(content80 + '\n')
        f.write(content81 + '\n')
        f.write(content82 + '\n')
        f.write(content83 + '\n')
        f.write(content84 + '\n')
        f.write(content85 + '\n')
        f.write(content86 + '\n')
        f.write(content87 + '\n')
        f.write(content88 + '\n')
        f.write(content89 + '\n')
        f.write(content90 + '\n')
        f.write(content91 + '\n')
        f.write(content92 + '\n')
        f.write(content93 + '\n')
        f.write(content94 + '\n')
        f.write(content95 + '\n')
        f.write(content96 + '\n')
        f.write(content97 + '\n')
        f.write(content98 + '\n')
        f.write(content99 + '\n')
        f.write(content100 + '\n')
        f.write(content101 + '\n')


if __name__=="__main__":

    root_path = '/media/administrator/My Passport/video_jpg/testing/negative/flow_out'
    file_list = sorted(os.listdir(root_path))###sorted返回重新排序的列表。os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
    for fl in file_list:
        write_sh(root_path+fl)


####cd ../000002\cp 000098.flo.png ./000099.flo.png
