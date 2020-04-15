# Data from https://www.kaggle.com/jhoward/rsna-hemorrhage-jpg

import os
import pandas as pd

path = "./data/rsna-hemorrhage-jpg/meta/meta/"
meta_data = {} 
for file_path in os.listdir(path):
    f_split = file_path.split('.')
    #if f_split[1] == 'pkl':
    #    meta_data[f_split[0]] = pd.read_pickle(path+file_path)
    if f_split[1] == 'fth':
        meta_data[f_split[0]] = pd.read_feather(path+file_path)

for key in meta_data.keys():
    if key != 'labels':
        meta_data[key]['fname'] = [f.split('/')[-1].split('.')[0]+'.jpg' for f in meta_data[key]['fname']]

path = "./data/rsna-hemorrhage-jpg/train_jpg/train_jpg/"
img_files = set(os.listdir(path))

isImg = [f in img_files for f in meta_data['comb']['fname']]

data = meta_data['comb'][isImg]

path = "./data/rsna-hemorrhage-jpg/meta/meta/"
data.reset_index().to_feather(path+'img_data.fth') 








#%%

meta_data['comb'][meta_data['comb']['fname']=='ID_0000aee4b'].T
#%%
series = list(meta_data['comb']['fname'][meta_data['comb']['SeriesInstanceUID'] == 'ID_1e59488a44'])

#%%
from matplotlib import pyplot as plt

show_img(series[5], path)

#%%
def show_img(file, path):
    plt.figure(figsize=(9, 9))
    img = plt.imread(path+file)
    plt.imshow(img, cmap=plt.cm.bone)

def show_imgs(files, path):
    fig=plt.figure(figsize=(9, 9))
    columns = 3; rows = 3
    for i in range(len(files)):
        img = plt.imread(path+files[i])
        fig.add_subplot(rows, columns, i)
        plt.imshow(img, cmap=plt.cm.bone)
        fig.add_subplot

show_imgs(series, path)
