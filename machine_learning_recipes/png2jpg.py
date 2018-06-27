from PIL import Image
import os
from os import listdir
import string
import random

year = 2015
file_path = f'/Users/jo/Desktop/data_science/support_vector_machine/machine_learning_recipes/tf_files/flower_photos/{year}_volkswagen_tiguan_4motion-auto-r-line'
count = 0
for path in listdir(file_path):
    if str(year) in path:
        continue
    if '.png' in path or '.jpg' in path:
        im = Image.open(f'{file_path}/{path}')
        rgb_im = im.convert('RGB')
        random_name = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=20))
        rgb_im.save(f'{file_path}/{year}_{random_name}.jpg')
        os.remove(f'{file_path}/{path}')
# print(count)
