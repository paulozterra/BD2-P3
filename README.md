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
El back end se desarrollo con python, las librerias principales seran ahondadas dentro de la seccion Librerias Usadas

### Guia de implementación backend, codigo

* Al iniciar el programa se cargan diferentes archivos y datos que seran usados posteriormente, como el indice rtree, los vectores caracteristicas para la busqueda lineal, etc
* El primer fetch que se hace es el que recibe la imagen que se quiere buscar, 
 
* La imagen se parsea y se devuelven dos diferentes vectores, el primero se usa para los algoritmos KNN, Secuencial y Rtree, y el segundo para los algoritmos KNN High D, Secuencial y Rtree  

* El segundo fetch que se hace es el que recibe el topk, aqui se llama a la funcion que se encargara de ejecutra los diferentes algoritmos y los guarda en un array

* El ultimo fetch, se llama multiples veces desde el frontend debido a que no pudimos hayar la forma de mandar muchas imagenes como response y que sean utilizables en el frontend. El fetch recibe la posicion del archivo que quiere recibir, y simplemente lo devuelve.


## Preprocesamiento
La mayoria de datos que se cargan en los archivos .py que tiene prefijo preprocesamiento, cargan los archivos .csv, y los indices que llevarian buen tiempo cargarse en tiempo real.

## Librearias Usadas

 Se utilizaron las siguientes librerias:
 * face_recognition: Se utilizó las funciones face_encodings y face_distance. Se utilizo para obtener los vectores caracteristicos de cada imagen
 * pickle: Se utilizó las funciones load y dump
 * pandas: Se utilizo para el manejo de nuestro dataset
 * sklearn: Libreria importante para importar el PCA que viene incluido en la libreria. Se utilizó el PCA para reducir la dimensionalidad de los vectores caracteristicos que fueron pasados a traves de nuestro data_vector.csv
 * flask: Permite levantar la pagina web en localhost
 * rtree: Libreria usada para indexar los vectores caracteristicos.
 
## Eexperimentación

### Lineal Search by Range Algoritm 

### Knn-Secuencial vs Knn-Rtree vs Knn-HighD(Rtree) vs Knn-HighD(Secuencial)

### Video 
https://youtu.be/zSO5gA5PM2g
