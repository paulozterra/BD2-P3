
import searchIndex
import searchLineal
import face_recognition


def search_all(query, k, vector, ind, dic):
    knn = searchLineal.searchKNN(query, k, vector)
    rtree = searchIndex.searchRtree(query, k, dic, ind)
    knnv2 = searchLineal.searchKNNV2(query, k, vector)

    knd = "searchKNND"
    parseNew = parseToDirections(knnv2)
    parseKNN = parseToDirections(knn)
    parseRtree = parseToDirections(rtree)

    print(parseRtree)
    print(parseKNN)

    return [parseNew, parseRtree]


def parseBasicEncode(file_stream):

    # Pre-calculated face encoding of Obama generated with face_recognition.face_encodings(img)
    picture = face_recognition.load_image_file(
        file_stream)
    encode = face_recognition.face_encodings(picture)[
        0]
    return encode


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
