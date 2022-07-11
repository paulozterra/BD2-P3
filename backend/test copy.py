import face_recognition
import searchLineal
from searchAll import parseBasicEncode
import csv
import rtree
from pathlib import Path


def test_searchLineal():
    data_vectors = []
    dic = {}
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for data in csv_reader:
            datos = [float(x) for x in data[1:]]
            dic[data[0]] = datos
            data_vectors.append(data)
    filename = "lfw\Aaron_Pena\Aaron_Pena_0001.jpg"
    parsedQuery = parseBasicEncode(filename)

    # CODE SERACH ALL
    something = searchLineal.searchKNN(parsedQuery, 3, dic)
    # PARSE
    names = [x[1] for x in something]
    print(names)


def test_rtree():
    dic = {}
    dic2 = {}
    prop = rtree.index.Property()
    prop.dimension = 128
    prop.buffering_capacity = 10
    prop.dat_extension = 'data'
    prop.idx_extension = 'index'
    ind = rtree.index.Index(f"indiceTEST", properties=prop)
    print("\ngaaaaa\n")
    aux = 0
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for data in csv_reader:
            datos = [float(x) for x in data[1:]]
            dic[data[0]] = datos
            dic2[aux] = data[0]
            aux += 1
        # INDEX BUILD
    for i in dic2:
        ind.insert(i, tuple(dic[dic2[i]]))
    filename = "lfw\Aaron_Pena\Aaron_Pena_0001.jpg"
    parsedQuery = parseBasicEncode(filename)
    print(ind)
    # CODE SERACH ALL
    query = tuple(parsedQuery)
    result = list(ind.nearest(coordinates=query, num_results=3))
    resultparser = [dic2[x] for x in result]
    print(resultparser)
    return result
    # PARSE


def test_rtree_2():
    return 0


test_rtree()
