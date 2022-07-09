import csv
import rtree
from rtree import index
from pathlib import Path

prop = index.Property()
prop.dimension = 128
prop.buffering_capacity = 10

f =  r"indices/indice6400.index"
fileObj = Path(f)

if(fileObj.is_file()==False):
    prop.dat_extension = "data"
    prop.idx_extension = "index"
    ind = rtree.index.Index("indices/indice6400", properties=prop)
    ##
    #DATA

    data_vectors = []
    with open('data_vector.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for data in csv_reader:
            data = [float(x) for x in data[1:]]
            data_vectors.append(data)

    #INDEX BUILD
    for i in range(6400):
        ind.insert(i, tuple(data_vectors[i]))
else:
    print("ya existe")

