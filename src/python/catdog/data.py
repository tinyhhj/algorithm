from glob import glob
import os
import numpy as np
import shutil

for i,num in [('train',1000),('val',500),('test',500)]:
    dog_path = os.path.join('data', i, 'dog')
    cat_path = os.path.join('data', i , 'cat')
    os.makedirs(dog_path,exist_ok=True)
    os.makedirs(cat_path,exist_ok=True)

    src = os.path.join('dogs-vs-cats/train')
    dogs = glob(os.path.join(src,'dog*'))
    cats = glob(os.path.join(src,'cat*'))

    np.random.shuffle(dogs)
    np.random.shuffle(cats)
    if num != len(os.listdir(dog_path)):
        for f in dogs[:num]:
            shutil.move(f, os.path.join(dog_path,os.path.basename(f)))
    for ff in cats[:num]:
        shutil.move(ff, os.path.join(cat_path, os.path.basename(ff)))


assert len(os.listdir('data/train/dog')) == 1000
assert len(os.listdir('data/train/cat')) == 1000
assert len(os.listdir('data/val/dog')) == 500
assert len(os.listdir('data/val/cat')) == 500
assert len(os.listdir('data/test/dog')) == 500
assert len(os.listdir('data/test/cat')) == 500

