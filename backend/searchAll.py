import searchIndex
import searchLineal
import face_recognition
import pickle
import pandas as pd

scaler = pickle.load(open("datos/scaler.dat", "rb"))
pca = pickle.load(open("datos/pca.dat", "rb"))


def search_all(query, vector, ind, dic, querypca, vectorpca, indpca, dicpca, k):
    knn = searchLineal.searchKNN(query, k, vector)
    rtree = searchIndex.searchRtree(query, k, dic, ind)
    knnv2 = searchLineal.searchKNNV2(query, k, vector)

    knnpca = searchLineal.searchKNN(querypca, k, vectorpca)
    rtreepca = searchIndex.searchRtree(querypca, k, dicpca, indpca)

    knd = "searchKNND"
    #parseNew = parseToDirections(knnv2)
    parseKNN = parseToDirections(knn)
    parseRtree = parseToDirections(rtree)
    parseKNNPca = parseToDirections(knnpca)
    parseRtreePca = parseToDirections(rtreepca)
    print(parseRtree)
    print(parseKNN)

    return [parseKNN, parseRtree, parseKNNPca, parseRtreePca]


def parseBasicEncode(file_stream):
    picture = face_recognition.load_image_file(
        file_stream)
    encode = face_recognition.face_encodings(picture)
    x_df = pd.DataFrame(data=encode, columns=[str(i) for i in range(1, 129)])
    x_scaled = scaler.transform(x_df)
    x_pca = pca.transform(x_scaled)
    return [encode[0], x_pca[0]]


def parseToDirections(lista):
    list2 = []
    str = "lfw\\"
    listr = []
    for i in lista:
        result = ""
        for j in i:
            if j.isnumeric() == False:
                result += j
            else:
                result = result[:-1]+"\\"
                list2.append(str+result)
                break
    for x in range(len(lista)):
        listr.append(list2[x]+lista[x])
    return listr
