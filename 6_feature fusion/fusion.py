
import os, glob
import numpy as np




vgg16_features='/media/administrator/b11512ec-3b41-4ff9-8ab9-b048dc11432b/hongyanjin/shiyan/vgg16_features'
vgg16_features_flow='/media/administrator/b11512ec-3b41-4ff9-8ab9-b048dc11432b/hongyanjin/shiyan/vgg16_features_flow'
vgg16_flow_fusion='/media/administrator/b11512ec-3b41-4ff9-8ab9-b048dc11432b/hongyanjin/shiyan/vgg16_flow_fusion'


train_path = os.path.join(vgg16_flow_fusion, 'training')
if not os.path.exists(train_path):
        os.makedirs(train_path)
test_path = os.path.join(vgg16_flow_fusion, 'testing')
if not os.path.exists(test_path):
        os.makedirs(test_path)






phase='testing'
vgg16_features_path = os.path.join(vgg16_features, phase)
vgg16_features_path_list = sorted(os.listdir(vgg16_features_path))
vgg16_features_flow_path = os.path.join(vgg16_features_flow, phase)
vgg16_features_flow_path_list = sorted(os.listdir(vgg16_features_path))

for num in range(0,len(vgg16_features_path_list)):
        print(num)
        vgg16_features_data = np.load(os.path.join(vgg16_features_path, vgg16_features_path_list[num]))
        #print(vgg16_features_data.files)
        vgg16_feature = vgg16_features_data['data']
        # features = all_data['data']  # 10 x 100 x 20 x 4096
        labels = vgg16_features_data['labels']  # 10 x 2
        detections = vgg16_features_data['det']  # 10 x 100 x 19 x 6
        videos = vgg16_features_data['ID']  # 10

        vgg16_features_flow_data = np.load(os.path.join(vgg16_features_flow_path, vgg16_features_flow_path_list[num]))
        vgg16_flow_feature = vgg16_features_flow_data['data']
        fusion_data = vgg16_feature + vgg16_flow_feature

        new_name = os.path.join(vgg16_flow_fusion, phase, vgg16_features_path_list[num])
        np.savez_compressed(new_name, data=fusion_data, det=detections, labels=labels, ID=videos)


print('testing_over')



phase='training'
vgg16_features_path = os.path.join(vgg16_features, phase)
vgg16_features_path_list = sorted(os.listdir(vgg16_features_path))
vgg16_features_flow_path = os.path.join(vgg16_features_flow, phase)
vgg16_features_flow_path_list = sorted(os.listdir(vgg16_features_path))

for num in range(0,len(vgg16_features_path_list)):
        print(num)
        vgg16_features_data = np.load(os.path.join(vgg16_features_path, vgg16_features_path_list[num]))
        #print(vgg16_features_data.files)
        vgg16_feature = vgg16_features_data['data']
        # features = all_data['data']  # 10 x 100 x 20 x 4096
        labels = vgg16_features_data['labels']  # 10 x 2
        detections = vgg16_features_data['det']  # 10 x 100 x 19 x 6
        videos = vgg16_features_data['ID']  # 10

        vgg16_features_flow_data = np.load(os.path.join(vgg16_features_flow_path, vgg16_features_flow_path_list[num]))
        vgg16_flow_feature = vgg16_features_flow_data['data']
        fusion_data = vgg16_feature + vgg16_flow_feature

        new_name = os.path.join(vgg16_flow_fusion, phase, vgg16_features_path_list[num])
        np.savez_compressed(new_name, data=fusion_data, det=detections, labels=labels, ID=videos)



print('training_over')


