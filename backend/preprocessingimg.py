import face_recognition
import os
import csv
# EXTRAER TODOS LOS VECTORES CARACTERISTICOS
# Y LOS GUARDAMOS EN UN CSV PARA PODER LEERLOS MAS FACILMENTE LUEGO


def preprocessimg():
    data_file = open("data_vector.csv", "w+", newline='')
    write = csv.writer(data_file)
    dir_path = "lfw/"
    for dir in os.listdir(dir_path):
        dir_imgs = os.listdir(dir_path + '/' + dir)
        for img in dir_imgs:
            data_vector = face_recognition.face_encodings(
                face_recognition.load_image_file(f"{dir_path}/{dir}/{img}"))
            try:
                data_arr = data_vector[0].tolist()
                data_arr2 = [img]
                data_arr2.extend(data_arr)
                write.writerow(data_arr2)
                # Segun https://medium.com/codex/face-recognition-25f7421a2268, face_encoding[0] nos arroga un vector de 128 elementos
            except:
                continue
    data_file.close()
