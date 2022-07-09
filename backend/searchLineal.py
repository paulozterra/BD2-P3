from queue import PriorityQueue
from scipy.spatial import distance


def searchKNN(Query, k, data_vectors):
    result = []
    priority = PriorityQueue()
    for vector in data_vectors:
        dist = distance.euclidean(Query, vector[1:])
        priority.put(dist)
    for i in range(k):
        result.append(priority.get())
    return result


def Rangesearch(Query, radio, data_vectors):
    result = []
    for vector in data_vectors:
        dist = distance.euclidean(Query, vector[1:])
        if (dist < radio):
            result.append(dist)
    return result
