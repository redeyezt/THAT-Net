cd /home/Workspace/yqs1995/DSTA-main/output/DSTA/vgg16/dad/snapshot
rm final_model.pth
mv bayesian_gcrnn_model_00.pth final_model.pth
cd /home/Workspace/yqs1995/DSTA-main
bash run_train_test.sh test 0 dad 10
cd /home/Workspace/yqs1995/DSTA-main/output/DSTA/vgg16/dad
rm -rf test
cd /home/Workspace/yqs1995/DSTA-main/output/DSTA/vgg16/dad/snapshot
rm final_model.pth
mv bayesian_gcrnn_model_01.pth final_model.pth
cd /home/Workspace/yqs1995/DSTA-main
bash run_train_test.sh test 0 dad 10
cd /home/Workspace/yqs1995/DSTA-main/output/DSTA/vgg16/dad
rm -rf test
