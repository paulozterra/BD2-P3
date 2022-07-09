import csv
import rtree
from pathlib import Path


def rtree_ind(dato):

    prop = rtree.index.Property()
    prop.dimension = 128
    prop.buffering_capacity = 10
    prop.dat_extension = 'data'
    prop.idx_extension = 'index'
    ind = rtree.index.Index(f"indices/indice{dato}", properties=prop)

    f = r"indices/indice6400.index"
    fileObj = Path(f)
    if(fileObj.is_file() == False):
        data_vectors = []
        with open('data_vector.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for data in csv_reader:
                data = [float(x) for x in data[1:]]
                data_vectors.append(data)

        # INDEX BUILD
        if (dato == "max"):
            dato = range(data_vectors)
        for i in range(dato):
            ind.insert(i, tuple(data_vectors[i]))
    return ind
