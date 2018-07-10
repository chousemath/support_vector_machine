# The purpose of this script is to count the number of images
# in any give vehicle model directory, determine whether or not
# that directory has be completely cleaned of useless images,
# and then upload that data to a remote database
from os import listdir


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


ROOT = '/Users/jo/Desktop/data_science/support_vector_machine/machine_learning_recipes/tf_files/flower_photos'
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
            f'{bcolors.WARNING}Unchecked directory{bcolors.ENDC}, total: {total}, checked: {checked}, unchecked: {unchecked}')
        print(
            f'{bcolors.OKGREEN}python garbageman.py {year} {make} {model} {trim}{bcolors.ENDC} &')
        print('=================================================')
    elif total < 1000:
        print(f'{bcolors.OKBLUE}Less than 1,000 images ({total}): {path}{bcolors.ENDC}')
        print('=================================================')
