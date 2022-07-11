from asyncio.windows_events import INFINITE
import csv
import rtree
from pathlib import Path
import json


def create_rtree_index(size):
    ind = None
    dic = {}
    dic2 = {}
    path = f"indices/indice{size}"
    prop = rtree.index.Property()
    prop.dimension = 128
    prop.buffering_capacity = 10
    prop.dat_extension = 'data'
    prop.idx_extension = 'index'
    f = rf"{path}.index"
    fileObj = Path(f)
    ind = None
    if(fileObj.is_file() == False):
        ind = rtree.index.Index(path, properties=prop)
        aux = 0
        if type(size) == str:
            size = 50000
        with open('data_vector.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for data in csv_reader:
                datos = [float(x) for x in data[1:]]
                dic[data[0]] = datos
                dic2[aux] = data[0]
                aux += 1
                if (aux > size):
                    break

            # INDEX BUILD
        for i in dic2:
            ind.insert(i, tuple(dic[dic2[i]]))
        # Serializing json
        if (size == 50000):
            size = "max"
        with open(f"jsons/diccionary{size}.json", "w") as outfile:
            json.dump(dic2, outfile)
    else:
        ind = rtree.index.Index(path, properties=prop)

    return ind


def readJson(size):
    path = f"jsons/diccionary{size}.json"
    json_object = None
    with open(path, 'r') as openfile:
        json_object = json.load(openfile)
    openfile.close()
    return json_object
