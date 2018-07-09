# The purpose of this script is to count the number of images
# in any give vehicle model directory, determine whether or not
# that directory has be completely cleaned of useless images,
# and then upload that data to a remote database
from os import listdir
from pprint import pprint

ROOT = '/Users/jo/Desktop/data_science/support_vector_machine/machine_learning_recipes/tf_files/flower_photos'
data = {}
for path in listdir(ROOT):
    if path == '.DS_Store':
        continue
    FOLDER_PATH = f'{ROOT}/{path}'
    file_names = listdir(FOLDER_PATH)
    split_path = path.split('_')
    # count up the files in each directory
    make = split_path[1]
    model = split_path[2]
    trim = split_path[3]
    year = split_path[0]
    total = len(file_names)
    checked = len(list(filter(lambda f: 'good' in f, file_names)))
    unchecked = total - checked
    if unchecked > 0:
        print(
            f'{make}/{model}/{trim}/{year} >>> total:{total}, checked:{checked}, unchecked:{unchecked}')
        print(f'python garbageman.py {year} {make} {model} {trim}')
        print('=================================================')
