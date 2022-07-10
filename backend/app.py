import csv
import json
from flask import Flask, request, redirect, send_file
from searchAll import search_all, parseBasicEncode

app = Flask(__name__)

data_vectors = []
answers = []
with open('data_vector.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for data in csv_reader:
        data = [float(x) for x in data[1:]]
        data_vectors.append(data)
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
    #answers = search_all(parsedQuery, topk, 3)
    filename = "lfw\Aaron_Peirsol\Aaron_Peirsol_0001.jpg"
    filename2 = "lfw\Aaron_Guiel\Aaron_Guiel_0001.jpg"
    # print(consult)
    #answers = search_all(consult, 2, 3)
    answers = [[filename, filename2, filename], [
        filename, filename2, filename]]
    return {"isOk": "200"}


@app.route('/api_answers', methods=['POST'])
def sendanswer():
    request_data = json.loads(request.data)
    pos = int(request_data['pos'])
    type = int(request_data['type'])
    return send_file(answers[type][pos], mimetype='image/jpeg')
