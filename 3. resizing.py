from google.colab import drive
drive.mount('/content/drive')

## change path once location is changed
FACES_DIR= '/content/drive/MyDrive/newtrial/train'
TFACES_DIR ='/content/drive/MyDrive/newtrial/test'

def createdataframe(dir):
    image_paths = []
    labels = []
    for label in os.listdir(dir):
        for imagename in os.listdir(os.path.join(dir, label)):
            image_paths.append(os.path.join(dir, label, imagename))
            labels.append(label)
        print(label, "completed")
    return image_paths, labels

train= pd.DataFrame()
train['image'], train['label'] = createdataframe(FACES_DIR)
print(train)

test =pd.DataFrame()
test['image'],test['label']= createdataframe(TFACES_DIR)
print (test)



import os
from PIL import Image

f = r'drive/MyDrive/newtrial/train/sober'      #Enter the location of your Image Folder

new_d = 256

for file in os.listdir(f):
    f_img = f+'/'+file
    try:
        img = Image.open(f_img)
        img = img.resize((new_d, new_d))
        img.save(f_img)
    except IOError:
        pass

k = r'drive/MyDrive/newtrial/train/drunk'      #Enter the location of your Image Folder

new_d = 256

for file in os.listdir(k):
    ks_img = k+'/'+file
    try:
        img = Image.open(ks_img)
        img = img.resize((new_d, new_d))
        img.save(ks_img)
    except IOError:
        pass

f = r'drive/MyDrive/newtrial/test/sober'      #Enter the location of your Image Folder

new_d = 256

for file in os.listdir(f):
    f_img = f+'/'+file
    try:
        img = Image.open(f_img)
        img = img.resize((new_d, new_d))
        img.save(f_img)
    except IOError:
        pass

import os
from PIL import Image

f = r'drive/MyDrive/newtrial/test/drunk'      #Enter the location of your Image Folder

new_d = 256

for file in os.listdir(f):
    f_img = f+'/'+file
    try:
        img = Image.open(f_img)
        img = img.resize((new_d, new_d))
        img.save(f_img)
    except IOError:
        pass    