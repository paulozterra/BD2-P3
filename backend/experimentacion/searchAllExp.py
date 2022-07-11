import searchIndex
import searchLineal
import face_recognition
import pickle
import pandas as pd
from timer import Timer
scaler = pickle.load(open("datos/scaler.dat", "rb"))
pca = pickle.load(open("datos/pca.dat", "rb"))


def search_all(query, dicvector, ind, dic, querypca, vectorpca, indpca, dicpca, k):
    t = Timer(text="You waited {:.1f} seconds")
    t2 = Timer(text="You waited {:.1f} seconds")
    t3 = Timer(text="You waited {:.1f} seconds")
    t4 = Timer(text="You waited {:.1f} seconds")
    t.start()
    knn = searchLineal.searchKNN(query, k, dicvector)
    t.stop()
    t2.start()
    rtree = searchIndex.searchRtree(query, k, dic, ind)
    t2.stop()
    t3.start()
    knnpca = searchLineal.searchKNN(querypca, k, vectorpca)
    t3.stop()
    t4.start()
    rtreepca = searchIndex.searchRtree(querypca, k, dicpca, indpca)
    t4.stop()


def range_Search(query, dicvector, querypca, dicvectorpca, radio):
    t = Timer(text="You waited {:.1f} seconds")
    t2 = Timer(text="You waited {:.1f} seconds")
    t.start()
    knn = searchLineal.rangeSearch(query, dicvector, radio)
    t.stop()
    t2.start()
    knnpca = searchLineal.rangeSearch(querypca, dicvectorpca, radio)
    t2.stop()

def parseBasicEncode(file_stream):
    picture = face_recognition.load_image_file(
        file_stream)
    encode = face_recognition.face_encodings(picture)
    x_df = pd.DataFrame(data=encode, columns=[str(i) for i in range(1, 129)])
    x_scaled = scaler.transform(x_df)
    x_pca = pca.transform(x_scaled)
    return [encode[0], x_pca[0]]

