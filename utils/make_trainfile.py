# -*- coding: utf-8 -*-
# @Time    : 2019/8/24 12:06
# @Author  : zhoujun
import os
import glob
import pathlib

# data_path = '/red_detection/DBNet/datasets/train'
data_path = '/red_detection/DBNet/data'
# data_path/img 存放图片
# data_path/gt 存放标签文件

f_w = open(os.path.join(data_path, 'code_train.txt'), 'w', encoding='utf8')
for img_path in glob.glob(data_path + '/code_train_img/*.jpg', recursive=True):
    d = pathlib.Path(img_path)
    label_path = os.path.join(data_path, 'code_train_gt', (str(d.stem) + '.txt'))
    if os.path.exists(img_path) and os.path.exists(label_path):
        print(img_path, label_path)
    else:
        print('不存在', img_path, label_path)
    f_w.write('{}\t{}\n'.format(img_path, label_path))
f_w.close()