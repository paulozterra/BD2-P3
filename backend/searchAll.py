import searchIndex
import searchLineal
import face_recognition


def search_all(query, k, vector):
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
