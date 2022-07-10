import csv
import json
from flask import Flask, request, redirect
from searchAll import search_all, parseBasicEncode

app = Flask(__name__)

data_vectors = []
with open('data_vector.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for data in csv_reader:
        data = [float(x) for x in data[1:]]
        data_vectors.append(data)
print("khomo")
vector = None
nameimg = None

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api', methods=['POST'])
def index():
    return {'name': 'Hello World'}


@app.route('/api/consult/img', methods=['POST'])
def consultImg():
    global vector, nameimg
    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        nameimg = file.filename
        vector = parseBasicEncode(file)
    #request_data = json.loads(request.data)
    #consult = request_data['consult']

    # print(consult)
    #answers = search_all(consult, 2, 3)
    return {'yara': "pe"}


@app.route('/api/consult/topk', methods=['POST'])
def consultTopk():
    request_data = json.loads(request.data)
    topk = int(request_data['topk'])
    answers = search_all(consult, 2, 3)
    return {'201': "isOk"}
