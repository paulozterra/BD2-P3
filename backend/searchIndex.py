def searchRtree(Query, k, dic2, ind):
    query = tuple(Query)
    result = list(ind.nearest(coordinates=query, num_results=k))
    resultparser = [dic2[str(x)] for x in result]
    return resultparser
