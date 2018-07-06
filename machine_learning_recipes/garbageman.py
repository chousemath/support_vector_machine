import os
from os import listdir
import string
import random
from subprocess import Popen, PIPE, STDOUT
from pprint import pprint
from typing import Dict, List


def is_good(raw_output) -> List[str]:
    output = list(filter(lambda x: 'LABEL:' in x,
                         str(raw_output).split('\\n')))
    intermediate = list(map(lambda x: x.split('"'), output))
    print(f'MAIN PREDICTION: {intermediate[0][1]}')
    return 'good' in intermediate[0][1]


ROOT = '/Users/jo/Desktop/data_science/support_vector_machine/machine_learning_recipes'
YEAR = '2016'
MAKE = 'hyundai'
MODEL = 'sonata'
TRIM = 'limited'
DIRECTORY_NAME = f'{YEAR}_{MAKE}_{MODEL}_{TRIM}'
FILE_PATH = f'/Users/jo/Desktop/data_science/support_vector_machine/machine_learning_recipes/tf_files/flower_photos/{DIRECTORY_NAME}'
for path in listdir(FILE_PATH):
    graph = f'--graph={ROOT}/tf_files2/retrained_graph.pb'
    layers = f'--labels={ROOT}/tf_files2/retrained_labels.txt'
    input_layer = f'--input_layer=Placeholder'
    output = f'--output_layer=final_result'
    image = f'--image={FILE_PATH}/{path}'
    cmd = f'python label_image.py {graph} {layers} {input_layer} {output} {image}'
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
              stderr=STDOUT, close_fds=True)
    try:
        cmd = f'good-{path}' if is_good(p.stdout.read()) else f'bad-{path}'
        os.system(f'mv {FILE_PATH}/{path} {FILE_PATH}/{cmd}')
    except Exception as err:
        print('there was an error...')
        print(err)
