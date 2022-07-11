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
    resultparser = [x[1] for x in result]
    return resultparser


def rangeSearch(Query, dic_vectors, radio):
    result = []
    for file in dic_vectors:
        dist = face_distance([Query], np.array(dic_vectors[file]))
        if (dist < radio):
            result.append(dist)
    return result
