import searchIndex
import searchLineal


def search_all(query, k, vector):
    rtree = searchIndex.searchRtree(query, k)
    knn = searchLineal.searchKNN(query, k, vector)
    knd = "searchKNND"
    return [rtree, knn, knd]
