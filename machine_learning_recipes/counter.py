# The purpose of this script is to count the number of images
# in any give vehicle model directory, determine whether or not
# that directory has be completely cleaned of useless images,
# and then upload that data to a remote database
import argparse
from os import listdir, system
from colors import bcolors
from operator import itemgetter
import csv

PARSER = argparse.ArgumentParser()
PARSER.add_argument(
    "env", help="Determines whether you want to run this script on local or external harddisk")
ARGS = PARSER.parse_args()

# ENV should either be 'local' or 'external', garbageman.py depends on this exact distinction
ENV = ARGS.env

if ENV == 'local':
    ROOT = '/Users/jo/Desktop/data_science/support_vector_machine/machine_learning_recipes/tf_files/flower_photos'
elif ENV == 'external':
    ROOT = '/Volumes/TriveStorage/ml_data'


def assemble_html_row(vehicle) -> str:
    row_class = ''
    if vehicle[6] == 0 and vehicle[5] >= 1000:
        row_class = 'class="table-success"'
    elif vehicle[6] == 0 and vehicle[5] < 1000:
        row_class = 'class="table-warning"'

    return f"""
        <tr {row_class}>
          <td>{vehicle[1]}</td>
          <td>{vehicle[2]}</td>
          <td>{vehicle[3]}</td>
          <td>{vehicle[0]}</td>
          <td>{vehicle[4]}</td>
          <td>{vehicle[5]}</td>
          <td>{vehicle[6]}</td>
        </tr>
    """.replace('\n', '')


list_of_vehicles = []
unified_command = ''
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
        unchecked_msg = (
            f'{bcolors.WARNING}Unchecked directory{bcolors.ENDC}, '
            f'total: {total}, checked: {checked}, unchecked: {unchecked}'
        )
        command_msg = (
            f'{bcolors.FAIL}python garbageman.py '
            f'{year} {make} {model} {trim} {ENV}{bcolors.ENDC}'
        )
        unified_command += f'{command_msg} && '
        print(f'{unchecked_msg}\n{command_msg}\n====================')
    elif total < 1000:
        print(f'{bcolors.OKBLUE}Less than 1,000 images ({total}): {path}{bcolors.ENDC}')
        print('====================')
    list_of_vehicles.append(
        (year, make, model, trim, total, checked, unchecked))

list_of_vehicles.sort(key=itemgetter(1, 2, 3))

html_string = ''
total_count = 0
with open('count.csv', 'w', newline='') as f:
    WRITER = csv.writer(f, delimiter=',', quotechar='|',
                        quoting=csv.QUOTE_MINIMAL)
    # WRITER.writerow(['MAKE', 'MODEL', 'TRIM', 'YEAR',
    #                  'TOTAL', 'GOOD', 'UNCHECKED'])
    for vehicle in list_of_vehicles:
        total_count += vehicle[4]
        WRITER.writerow([
            vehicle[1],  # make of the vehicle
            vehicle[2],  # model of the vehicle
            vehicle[3],  # trim of the vehicle
            vehicle[0],  # year of the vehicle
            vehicle[4],  # total number of image files in directory
            vehicle[5],  # total number of good image files in directory
            vehicle[6]   # total number of unchecked image files in directory
        ])
        html_string += assemble_html_row(vehicle)

filename = '../rows.js'
system(f'rm {filename}')
with open(filename, mode='a') as file:
    js_data = f'var html = \'{html_string}\';'
    js_data += f'document.getElementById(\'tableBody\').innerHTML = html;'
    js_data += f'document.getElementById(\'total-count\').innerHTML = \'<a class="nav-link">Images Scraped: {total_count}</a>\';'
    file.write(js_data)

print(unified_command[0:(len(unified_command) - 3)])
