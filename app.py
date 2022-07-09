import csv

from processingrtree import ind
from queue import PriorityQueue
from scipy.spatial import distance
from flask import Flask



app = Flask(__name__)

data_vectors = []
with open('data_vector.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    for data in csv_reader:
        data = [float(x) for x in data[1:]]
        data_vectors.append(data)
@app.route('/')
def hello():
    return 'hola mongol'

@app.route('/1')
def KNNsearch(Query, k):
    result = []
    priority = PriorityQueue()
    for vector in data_vectors:
        dist = distance.euclidean(Query, vector[1:])
        priority.put(dist)
    for i in range(k):
        result.append(priority.get())
    return result
@app.route('/2')
def Rtree(Query, k):
    result = []
    for p in ind.nearest(Query, num_results=k):
        result.append(p)
    return result

@app.route('/3')
def Rangesearch(Query, radio):
    result = []
    for vector in data_vectors:
        dist = distance.euclidean(Query, vector[1:])
        if (dist < radio):
            result.append(dist)
    return result
