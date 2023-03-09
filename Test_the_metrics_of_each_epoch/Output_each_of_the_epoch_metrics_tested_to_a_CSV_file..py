import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import codecs
import linecache
import os
import csv
#测试每一个生成的模型，注意这里“DSTA”只是一个名称，不代表任何含义

file = open('test.csv', 'w+',newline="")
writer = csv.writer(file)
writer.writerow(('AP', 'MTTA'))
for dirpath, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        text = linecache.getline(filename, 60)
        a = text.split()
        AP = str(a[2:3])[2:-3]
        MTTA = str(a[7:8])[2:-2]
        print(AP,     MTTA)
        writer.writerow((AP, MTTA))

