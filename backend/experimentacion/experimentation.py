from searchAllExp import search_all, parseBasicEncode, range_Search
import preprocessingrtree
import csv
answers = []
data_vectors = {}


def experiment_rangeSearch(radio):
    data_vectors = {}
    with open('datos/data_vector.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for data in csv_reader:
            datos = [float(x) for x in data[1:]]
            data_vectors[data[0]] = datos
    data_vectors_pca = {}
    with open('datos/data_vector_pca.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for data in csv_reader:
            datos = [float(x) for x in data[1:]]
            data_vectors_pca[data[0]] = datos
    parsedQuery = None
    parsedQueryPCA = None

    file = "experimentacion\Castillo.jpg"
    [parsedQuery, parsedQueryPCA] = parseBasicEncode(file)

    range_Search(parsedQuery, data_vectors,
                 parsedQueryPCA, data_vectors_pca, radio)


def range_Search_exp():
    radios = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
    for r in radios:
        experiment_rangeSearch(r)
        print(r)
        print("\n")


range_Search_exp()


def experiment_timer_vs(cantity):
    data_vectors = {}
    with open('datos/data_vector.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for data in csv_reader:
            datos = [float(x) for x in data[1:]]
            data_vectors[data[0]] = datos
    data_vectors_pca = {}
    with open('datos/data_vector_pca.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for data in csv_reader:
            datos = [float(x) for x in data[1:]]
            data_vectors_pca[data[0]] = datos
    TYPE1 = "standart"
    TYPE2 = "pca"
    CANTITY = cantity
    RTREE = preprocessingrtree.create_rtree_index(CANTITY, TYPE1)
    RTREEPCA = preprocessingrtree.create_rtree_index(CANTITY, TYPE2)
    DIC = preprocessingrtree.readJson(CANTITY, TYPE1)
    DICPCA = preprocessingrtree.readJson(CANTITY, TYPE2)
    parsedQuery = None
    parsedQueryPCA = None

    file = "experimentacion\Castillo.jpg"
    [parsedQuery, parsedQueryPCA] = parseBasicEncode(file)

    search_all(parsedQuery, data_vectors, RTREE, DIC,
               parsedQueryPCA, data_vectors_pca, RTREEPCA, DICPCA, 8)


def vs_experiment():
    cantidades = [100, 200, 400, 800, 1600, 3200, 6400, "max"]
    for i in cantidades:
        experiment_timer_vs(i)
        print("\n")
