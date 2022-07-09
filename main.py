import face_recognition
from processingrtree import ind

while(True):
    a=int(input())
    if a == 0:
        break
    else:
        picture = face_recognition.load_image_file("lfw\Aaron_Peirsol\Aaron_Peirsol_0001.jpg")
        q = tuple(face_recognition.face_encodings(picture)[0])
        lres = list(ind.nearest(coordinates=q, num_results=a))
        print("El vecino mas cercano de Aaron_Eckhart: ", lres)

