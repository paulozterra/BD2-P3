import pickle
import face_recognition
from processingrtree import ind
import pandas as pd

scaler = pickle.load(open("scaler.dat","rb"))
pca = pickle.load(open("pca.dat","rb"))

while(True):
    a=int(input())
    if a == 0:
        break
    else:
        picture = face_recognition.load_image_file("lfw\Aaron_Peirsol\Aaron_Peirsol_0001.jpg")
        q = face_recognition.face_encodings(picture)
        x_df = pd.DataFrame(data=q,columns=[str(i) for i in range(1,129)])
        x_scaled = scaler.transform(x_df)
        x_pca = pca.transform(x_scaled)
        lres = list(ind.nearest(coordinates=tuple(x_pca[0]), num_results=a))
        print("El vecino mas cercano de Aaron_Peirsol: ", lres)
