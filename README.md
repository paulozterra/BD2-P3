# BD2-P3

## Introducción

En este proyecto, se busco recrear el reconocimiento de rostros, en base a mas de 13 mil datos que se encuentran en la carpeta lfw, se implementó diferentes versiones del algoritmo de busqueda KNN, Secuencial, indexado con Rtree, y HighD (PCA) en el caso de nuestro grupo.

## Front end
La vista del front end esta conformada por
* El front end se desarrollo con angular
* Input que permite ingresar la img que se quiere buscar dentro de la base datos
* Input tipo texto que permite ingresar el topk de elementos que se quieren buscar.
* Cuatro columnos en donde se asigna los elementos encontrados respectivamente 
![WhatsApp Image 2022-07-10 at 11 43 56 PM](https://user-images.githubusercontent.com/66433825/178191198-3df65a7e-ddae-4835-9544-06ae251b666d.jpeg)

Guia del Front end, codigo:
* Primero se debe ingresar la imagen, que hara un fetch para cargar la imagen y parsearla en el backend
* Se debe ingresar el topk, y al dar a submit, se mandara a backend y ejectura los algoritmos de busqueda,

## Back end
El back end se desarrollo con flask, el proc

## Parser imagen

## Preprocesamiento

## Datos 

## Librearias Usadas

 Se utilizaron las siguientes librerias:
 * face_recognition: Se utilizó las funciones face_encodings y face_distance. Se utilizo para obtener los vectores caracteristicos de cada imagen
 * pickle: Se utilizó las funciones load y dump
 * pandas: Se utilizo para el manejo de nuestro dataset
 * sklearn: Libreria importante para la realización del PCA. Se utilizó el PCA para reducir la dimensionalidad de los vectores caracteristicos que fueron pasados a traves de nuestro data_vector.csv
 * flask: Permite levantar la pagina web en localhost
 * rtree: Libreria usada para indexar los vectores caracteristicos.
 
## Eexperimentación

### Lineal Search by Range Algoritm 

### Knn-Secuencial vs Knn-Rtree vs Knn-HighD(Rtree) vs Knn-HighD(Secuencial)

### Video 
https://youtu.be/zSO5gA5PM2g
