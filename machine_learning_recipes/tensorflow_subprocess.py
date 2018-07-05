from pprint import pprint
from subprocess import Popen, PIPE, STDOUT
from typing import Dict, List
import os
import random
import requests
import string
import datetime
import json
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS

ROOT = '/Users/jo/Desktop/data_science/support_vector_machine/machine_learning_recipes'
# ROOT = '/home/contact/support_vector_machine/machine_learning_recipes'

application = Flask(__name__)
CORS(application)
api = Api(application)


def format_response(raw_output) -> List[str]:
    output = list(filter(lambda x: 'LABEL:' in x,
                         str(raw_output).split('\\n')))
    intermediate = list(map(lambda x: x.split('"'), output))
    return list(map(lambda x: {'label': x[1], 'confidence': float(x[3])}, intermediate))


class TensorFlowRequests(Resource):
    def post(self):
        """Send a single message to a singler user"""
        json_data = request.get_json(force=True)
        image_url = json_data['image_url']
        filename = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=20)) + '.jpg'
        f = open(f'{ROOT}/test_data/{filename}', 'wb')
        f.write(requests.get(image_url).content)
        f.close()
        cmd = f'python label_image.py --graph={ROOT}/tf_files/retrained_graph.pb --labels={ROOT}/tf_files/retrained_labels.txt --input_layer=Placeholder --output_layer=final_result --image={ROOT}/test_data/{filename}'
        p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
                  stderr=STDOUT, close_fds=True)
        predictions = format_response(p.stdout.read())
        os.remove(f'{ROOT}/test_data/{filename}')
        return jsonify(success=True, data=predictions)


api.add_resource(TensorFlowRequests, '/requests')

if __name__ == '__main__':
    application.run(debug=True)


# execute_tensorflow(
#     'https://www.cars.co.za/carimages_gen/Volkswagen-Tiguan/Volkswagen-Tiguan-2.0TDI-4Motion-Highline-R-Line_VolkTigu2e13l.jpg')
