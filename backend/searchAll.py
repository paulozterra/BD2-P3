import searchIndex
import searchLineal
import face_recognition


def search_all(query, k, vector):
    #data = face_recognition.face_encodings(Face_recognition.load_image_file(query))
    # print(data)
    picture = face_recognition.load_image_file(
        "lfw\Aaron_Peirsol\Aaron_Peirsol_0001.jpg")
    query = face_recognition.face_encodings(picture)[0]
    rtree = searchIndex.searchRtree(query, k)
    knn = "searchKNN"
    #knn = searchLineal.searchKNN(query, k, vector)
    knd = "searchKNND"
    return {
        'rtree': rtree,
        'knn': knn,
        'knd': knd,
    }


def parseBasicEncode(file_stream):

    # Pre-calculated face encoding of Obama generated with face_recognition.face_encodings(img)
    picture = face_recognition.load_image_file(
        file_stream)
    encode = face_recognition.face_encodings(picture)[
        0]
    return encode
    return {'yara': "pe"}
