from PIL import Image
import os
from os import listdir
import string
import random

file_path = '/Users/jo/Desktop/data_science/support_vector_machine/machine_learning_recipes/tf_files/flower_photos/2011_hyundai_accent_gl'

for path in listdir(file_path):
    im = Image.open(f'{file_path}/{path}')
    rgb_im = im.convert('RGB')
    random_name = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=20))
    rgb_im.save(f'{file_path}/{random_name}.jpg')
    os.remove(f'{file_path}/{path}')
