import csv
import json
from flask import Flask, request, redirect, send_file
from searchAll import search_all, parseBasicEncode
import preprocessingrtree


app = Flask(__name__)

answers = []
data_vectors = {}
with open('data_vector.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for data in csv_reader:
        datos = [float(x) for x in data[1:]]
        data_vectors[data[0]] = datos

RTREE = preprocessingrtree.create_rtree_index("max")
DIC = preprocessingrtree.readJson("max")
parsedQuery = None
nameimg = None


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api', methods=['POST'])
def index():
    return {'name': 'Hello World'}


@app.route('/api_consult_img', methods=['POST'])
def consultImg():
    global nameQuery, parsedQuery
    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        nameQuery = file.filename
        parsedQuery = parseBasicEncode(file)
    return {"isOK": "200"}


@app.route('/api_consult_topk', methods=['POST'])
def consultTopk():
    global answers
    request_data = json.loads(request.data)
    topk = int(request_data['topk'])
    testing = search_all(parsedQuery, topk, data_vectors, RTREE, DIC)
    answers = testing
    # print(consult)
    return {"isOk": "200"}


@app.route('/api_answers', methods=['POST'])
def sendanswer():
    request_data = json.loads(request.data)
    pos = int(request_data['pos'])
    type = int(request_data['type'])
    return send_file(answers[type][pos], mimetype='image/jpeg')
