from searchAll import search_all, parseBasicEncode
import preprocessingrtree
import csv
data_vectors = {}
with open('data_vector_pca.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for data in csv_reader:
        datos = [float(x) for x in data[1:]]
        data_vectors[data[0]] = datos
TYPE = "pca"
CANTITY = "max"
RTREE = preprocessingrtree.create_rtree_index(CANTITY, TYPE)
DIC = preprocessingrtree.readJson(CANTITY, TYPE)
parsedQuery = None
nameimg = None
img = "lfw\Aaron_Eckhart\Aaron_Eckhart_0001.jpg"
[imgparsed, imgparsedpca] = parseBasicEncode(img)

# BUSQUEDA ALGORITHMS
search_all(parsedQuery, imgparsedpca, 5, data_vectors, RTREE, DIC)
