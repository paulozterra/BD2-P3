from flask import Flask
from processingrtree import ind, data_vectors
from queue import PriorityQueue
from scipy.spatial import distance

app = Flask(__name__)


@app.route('/')
def hello():
    return 'hola mongol'

def KNNsearch(Query, k):
    result = []
    priority = PriorityQueue()
    for vector in data_vectors:
        dist = distance.euclidean(Query, vector[1:])
        priority.put(dist)
    for i in range(k):
        result.append(priority.get())
    return result

def Rtree(Query, k):
    result = []
    for p in ind.nearest(Query, num_results=k):
        result.append(p)
    return result

def Rangesearch(Query, radio):
    result = []
    for vector in data_vectors:
        dist = distance.euclidean(Query, vector[1:])
        if (dist < radio):
            result.append(dist)
    return result
