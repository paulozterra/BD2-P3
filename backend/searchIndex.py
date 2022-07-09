import preprocessingimg


def searchRtree(Query, k):
    ind = preprocessingimg.rtree_ind(6400)
    result = []
    for p in ind.nearest(Query, num_results=k):
        result.append(p)
    return result
