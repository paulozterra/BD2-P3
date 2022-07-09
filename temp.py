from processingrtree import ind


def KNNsearch(Query, k):
    result = []
    priority = PriorityQueue()
    for vector in data_vectors:
        dist = ED(Query, vector[1:])
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
    for vector in data_vectors:
        dist = ED(Query, vector[1:])
        if (dist < radio):
            result.append(i)
    return result