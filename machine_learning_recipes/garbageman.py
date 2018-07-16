# The purpose of this script is to clean a directory
# of useless images

import argparse
import os
from os import listdir
from subprocess import Popen, PIPE, STDOUT
from typing import List

PARSER = argparse.ArgumentParser()
PARSER.add_argument("year", help="Designates the year of the vehicle")
PARSER.add_argument("make", help="Designates the make of the vehicle")
PARSER.add_argument("model", help="Designates the model of the vehicle")
PARSER.add_argument("trim", help="Designates the trim of the vehicle")
PARSER.add_argument(
    "env", help="Designates whether to use the local or external harddisk")
ARGS = PARSER.parse_args()


def is_good(raw_output) -> List[str]:
    """Checks whether or not an image has been classified as `good`"""
    label_data = list(filter(lambda x: 'LABEL:' in x,
                             str(raw_output).split('\\n')))
    intermediate = list(map(lambda x: x.split('"'), label_data))
    return 'good' in intermediate[0][1]


EXTERNAL_HARDDRIVE = '/Volumes/TriveStorage/ml_data'
ROOT = '/Users/jo/Desktop/data_science/support_vector_machine/machine_learning_recipes'
YEAR = ARGS.year
MAKE = ARGS.make
MODEL = ARGS.model
TRIM = ARGS.trim
ENV = ARGS.env
DIRECTORY_NAME = f'{YEAR}_{MAKE}_{MODEL}_{TRIM}'

# THIS NEEDS TO BE SWAPPED FOR USE ON LOCAL/EXTERNAL HARDDISK
if ENV == 'local':
    FILE_PATH = f'/Users/jo/Desktop/data_science/support_vector_machine/machine_learning_recipes/tf_files/flower_photos/{DIRECTORY_NAME}'
elif ENV == 'external':
    FILE_PATH = f'{EXTERNAL_HARDDRIVE}/{DIRECTORY_NAME}'

for path in listdir(FILE_PATH):
    # make sure you don't check good images again
    if 'good-' in path:
        continue
    graph = f'--graph={ROOT}/tf_files2/retrained_graph.pb'
    layers = f'--labels={ROOT}/tf_files2/retrained_labels.txt'
    input_layer = f'--input_layer=Placeholder'
    output = f'--output_layer=final_result'
    image = f'--image={FILE_PATH}/{path}'
    cmd = f'python label_image.py {graph} {layers} {input_layer} {output} {image}'
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
              stderr=STDOUT, close_fds=True)
    try:
        if is_good(p.stdout.read()):
            # make sure you mark a good image as such so you do not
            # end up checking it again
            os.system(f'mv {FILE_PATH}/{path} {FILE_PATH}/good-{path}')
        else:
            # THIS NEEDS TO BE SWAPPED FOR USE ON LOCAL/EXTERNAL HARDDISK
            os.system(f'rm {FILE_PATH}/{path}')
    except Exception as err:
        print(err)
