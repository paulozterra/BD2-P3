import csv
from flask import Flask
from searchAll import search_all

app = Flask(__name__)

data_vectors = []
with open('data_vector.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for data in csv_reader:
        data = [float(x) for x in data[1:]]
        data_vectors.append(data)
print("khomo")


@app.route('/api', methods=['POST'])
def index():
    return {'name': 'Hello World'}


@app.route('/api/consult', methods=['POST'])
def consult():
    answers = search_all(1,2,3)
    return answers
