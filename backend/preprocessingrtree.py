from asyncio.windows_events import INFINITE
import csv
import rtree
from pathlib import Path
import json


def decide_paths(size, type):
    if (type == "standart"):
        data_path = "data_vector.csv"
        json_path = f"jsons/standart/diccionary{size}.json"
        indices_path = f"indices/standart/indice{size}"
    else:
        data_path = "data_vector_pca.csv"
        json_path = f"jsons/pca/diccionary{size}.json"
        indices_path = f"indices/pca/indice{size}"
    return [data_path, json_path, indices_path]


def decide_dimension(type):
    if (type == "standart"):
        return 128
    else:
        return 59


def create_rtree_index(size, type):
    [data_path, json_path, indices_path] = decide_paths(size, type)

    ind = None
    dic = {}
    dic2 = {}
    path = indices_path
    prop = rtree.index.Property()
    prop.dimension = decide_dimension(type)
    prop.buffering_capacity = 10
    prop.dat_extension = 'data'
    prop.idx_extension = 'index'
    f = rf"{path}.index"
    fileObj = Path(f)
    ind = None
    if(fileObj.is_file() == False):
        ind = rtree.index.Index(path, properties=prop)
        aux = 0
        if isinstance(size, str):
            size = 20000
        with open(data_path, 'r') as csv_file:
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
        if (size == 20000):
            size = "max"
        with open(json_path, "w") as outfile:
            json.dump(dic2, outfile)
    else:
        ind = rtree.index.Index(path, properties=prop)
    return ind


def readJson(size, type):
    path = ""
    if (type == "standart"):
        path = f"jsons/standart/diccionary{size}.json"
    else:
        path = f"jsons/pca/diccionary{size}.json"
    json_object = None
    with open(path, 'r') as openfile:
        json_object = json.load(openfile)
    openfile.close()
    return json_object
