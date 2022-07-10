from queue import PriorityQueue
from face_recognition import face_distance

def searchKNN(Query, k, data_vectors):
    result = []
    priority = PriorityQueue()
    for vector in data_vectors:
        dist = face_distance(Query, vector[1:])
        priority.put(dist)
    for i in range(k):
        result.append(priority.get())
    return result


def Rangesearch(Query, radio, data_vectors):
    result = []
    for vector in data_vectors:
        dist = face_distance(Query, vector[1:])
        if (dist < radio):
            result.append(dist)
    return result
