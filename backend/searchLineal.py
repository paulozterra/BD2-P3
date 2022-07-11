from queue import PriorityQueue
from face_recognition import face_distance
import heapq
import numpy as np


def searchKNN(Query, k, dic_vectors):
    result = []
    for file in dic_vectors:
        dist = face_distance([Query], np.array(dic_vectors[file]))
        heapq.heappush(result, (-dist, file))
        if (len(result) > k):
            heapq.heappop(result)
    result.sort(key=lambda tup: tup[1])

    # SE NECESITA TODA LA DIRECCION DE LOS ARCHIVOS
    resultparser = [x[1] for x in result]
    return resultparser


def Rangesearch(Query, radio, data_vectors):
    result = []
    for vector in data_vectors:
        dist = face_distance(Query, vector[1:])
        if (dist < radio):
            result.append(dist)
    return result


def ED(v1, v2):
    return np.linalg.norm(v1-v2)


def searchKNNV2(query, k, dic_vectors):
    priority = PriorityQueue()
    for i in dic_vectors:
        dist = ED(np.array(dic_vectors[i]), query) * (-1)
        if(priority.qsize() < k):
            priority.put((dist, i))
        else:
            top = priority.get()
            if(dist > top[0]):
                priority.put((dist, i))
            else:
                priority.put(top)
    result = [0] * k
    i = k - 1
    while not priority.empty():
        data = priority.get()
        result[i] = data[1]
        i -= 1
    return result
