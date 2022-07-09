import preprocessingrtree


def searchRtree(Query, k):
    query = tuple(Query)
    ind = preprocessingrtree.rtree_ind(6400)
    result = list(ind.nearest(query, num_results=k))
    return result
