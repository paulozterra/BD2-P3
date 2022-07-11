# BD2-P3

## Integrantes:
| Edgar Chacon| Paulo Cuaresma|
| ----- | ---- |
| 100%| 100% |

## Introducción

En este proyecto, se busco recrear el reconocimiento de rostros, en base a mas de 13 mil datos que se encuentran en la carpeta lfw, se implementó diferentes versiones del algoritmo de busqueda KNN, Secuencial, indexado con Rtree, y HighD (PCA) en el caso de nuestro grupo.

## Preprocesamiento
La mayoria de datos que se cargan en los archivos .py que tiene prefijo preprocesamiento, cargan los archivos .csv, y los indices que llevarian buen tiempo cargarse en tiempo real.

* preprocessingimg, usa la libreria de face recognition, para obtener los vectores caracteristicos de las imagenes (13176 imagenes),y los guarda en un csv junto con su nombre

``` python
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
 ```
 * preprocessingrtree, usa la libreria rtree para construir los indices, ademas se ha dinamizado la funcion para que construya el indice en base a ciertos parametros que entre otras cosas decide el path donde se guardara el indice y la dimension con la que se trabajara. Ademas cabe recalcar que si el indice ya existe, solo se devolvera y no se rehara todo el procesos costo.
 ``` python
 def create_rtree_index(size, type):
    [data_path, json_path, indices_path] = decide_paths(size, type)
    ind = None
    dic = {}
    dic2 = {}
    path = indices_path
    prop = rtree.index.Property()
    prop.dimension = decide_dimension(type)
    prop.buffering_capacity = 10
    prop.dat_extension = 'data'
    prop.idx_extension = 'index'
    f = rf"{path}.index"
    fileObj = Path(f)
    ind = None
    if(fileObj.is_file() == False):
        ind = rtree.index.Index(path, properties=prop)
        aux = 0
        if isinstance(size, str):
            size = 20000
        with open(data_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for data in csv_reader:
                datos = [float(x) for x in data[1:]]
                dic[data[0]] = datos
                dic2[aux] = data[0]
                aux += 1
                if (aux > size):
                    break
        for i in dic2:
            ind.insert(i, tuple(dic[dic2[i]]))
        if (size == 20000):
            size = "max"
        with open(json_path, "w") as outfile:
            json.dump(dic2, outfile)
    else:
        ind = rtree.index.Index(path, properties=prop)
    return ind
 ```
* preprocessingPCA, usa la libreria de sktlearn para transformar los originales vectores caracterisiticos de las imagenes, a uno mas reducidos. Y se guarda toda la informacion importante, que sirva para poder hacer el parser de la imagen que se ingresara luego.
 ``` python
 df = pd.read_csv("data_vectorh.csv")

posvectors = [str(i) for i in range(1, 129)]
x = df.loc[:, posvectors]
y = df.loc[:, ["path"]]

scaler = StandardScaler()
scalert = scaler.fit_transform(x)

pca = PCA(.95)
pcat = pca.fit_transform(scalert)
dfActual = pd.DataFrame(data=pcat)
dfFinal = pd.concat([df[["path"]], dfActual], axis=1)

dataset = "data_vector_pca.csv"
scalerp = "scaler.dat"
pcap = "pca.dat"
dfFinal.to_csv(dataset, header=None, index=False)
pickle.dump(scaler, open(scalerp, "wb"))
pickle.dump(pca, open(pcap, "wb"))
 ```
 


## Front end
La vista del front end esta conformada por
* El front end se desarrollo con angular
* Input que permite ingresar la img que se quiere buscar dentro de la base datos
* Input tipo texto que permite ingresar el topk de elementos que se quieren buscar.
* Cuatro columnos en donde se asigna los elementos encontrados respectivamente 
![WhatsApp Image 2022-07-10 at 11 43 56 PM](https://user-images.githubusercontent.com/66433825/178191198-3df65a7e-ddae-4835-9544-06ae251b666d.jpeg)

Guia del Front end, codigo:
* Primero se debe ingresar la imagen, que hara un fetch para cargar la imagen y parsearla en el backend
 ``` javascript 
 const onFileSelectSuccess = (file, event) => {
    fetchImage(file);
    const formData = new FormData();
    formData.append("file", file);

    event.preventDefault();
    fetch("/api_consult_img", {
      method: "POST",
      body: formData,
    }).then((response) => {
      if (response.ok) {
        return response.json();
      }
    });
  };
 ```
* La imagen ademas tambien es cargada para ser mostrada en el frontada.
 ``` javascript 
 const [selectedFile, setSelectedFile] = useState("");
 
 const showImage = async (imageUrl) => {
    const imageObjectURL = URL.createObjectURL(imageUrl);
    setSelectedFile(imageObjectURL);
  };
  
  const Showimage = () => {
    if (selectedFile === "") {
      return <></>;
    }
    return <img src={selectedFile} alt="icons" className="center" />;
  };
 ```
 
* Se debe ingresar el topk, y al dar a submit, se mandara a backend y ejectura los algoritmos de busqueda,
``` javascript 
 const handleSubmit = (event) => {
    event.preventDefault();
    fetch("/api_consult_topk", {
      method: "POST",
      body: JSON.stringify({ topk: topk }),
    })
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
      })
      .then((data) => {
        onInputsSubmit(topk);
      });
  };
 ```
 * Al obtener el response, se procede a ejecutar el ultimo fetch, que pedira todos las respuesta y luego pasaran a ser mostradas.
``` javascript 
const img = async (pos_, type_) => {
    const res = await fetch("/api_answers", {
      method: "POST",
      body: JSON.stringify({ pos: pos_, type: type_ }),
    });
    if (!res.ok) throw new Error(res.statusText);
    const data = await res.blob();
    return data;
  };
  
const handleInputSubmit = async (topk) => {
    setEmpty();

    for (let i = 0; i < topk; i++) {
      let knn = img(i, 0);
      let rtree = img(i, 1);
      let knnpca = img(i, 2);
      let rtreepca = img(i, 3);
      knn.then((response) => getImg(response, 0));
      rtree.then((response) => getImg(response, 1));
      knnpca.then((response) => getImg(response, 2));
      rtreepca.then((response) => getImg(response, 3));
    }
    test(
      knnaux.length,
      rtreeaux.length,
      knnauxpca.length,
      rtreeauxpca.length,
      topk
    );
  };
  ```
  * El proceso para poder parsear las imagenes para que sean visibiles lo desarrolla la funcion 

``` javascript 
 const getImg = async (aux, type) => {
     if (aux != undefined) {
       const reader = new FileReader();
       reader.readAsDataURL(aux);
       reader.onloadend = () => {
         const base64data = reader.result;
         if (type == 0) {
           setKnnAux((old) => [...old, base64data]);
         } else if (type == 1) setRtreeAux((old) => [...old, base64data]);
         else if (type == 2) setKnnAuxPca((old) => [...old, base64data]);
         else setRtreeAuxPca((old) => [...old, base64data]);
       };
     }
   };
  ```
  
## Back end
El back end se desarrollo con python, las librerias principales seran ahondadas dentro de la seccion Librerias Usadas

### Guia de implementación backend, codigo

* Al iniciar el programa se cargan diferentes archivos y datos que seran usados posteriormente, como el indice rtree, los vectores caracteristicas para la busqueda lineal, etc 
 ``` python 
RTREE = preprocessingrtree.create_rtree_index(CANTITY, TYPE1)
RTREEPCA = preprocessingrtree.create_rtree_index(CANTITY, TYPE2)
DIC = preprocessingrtree.readJson(CANTITY, TYPE1)
DICPCA = preprocessingrtree.readJson(CANTITY, TYPE2)
parsedQuery = None
parsedQueryPCA = None
nameimg = None
```

* El primer fetch que se recibe es el de la imagen. La imagen se parsea y se devuelven dos diferentes vectores, el primero se usa para los algoritmos KNN, Secuencial y Rtree, y el segundo para los algoritmos KNN High D, Secuencial y Rtree  

 ``` python 
@app.route('/api_consult_img', methods=['POST'])
def consultImg():
    global nameQuery, parsedQuery, parsedQueryPCA
    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        nameQuery = file.filename
        [parsedQuery, parsedQueryPCA] = parseBasicEncode(file)
```

 
* Para calcular el primer valor de retorno de la funcion solo se calcula los vectores caracterisiticos con la libreria face recognition, y para el segundo valor de retorno, se usa lo que fue guardado en el preprocesamiento de PCA. 
 ``` python 
scaler = pickle.load(open("scaler.dat", "rb"))
pca = pickle.load(open("pca.dat", "rb"))

def parseBasicEncode(file_stream):
    picture = face_recognition.load_image_file(
        file_stream)
    encode = face_recognition.face_encodings(picture)
    x_df = pd.DataFrame(data=encode, columns=[str(i) for i in range(1, 129)])
    x_scaled = scaler.transform(x_df)
    x_pca = pca.transform(x_scaled)
    return [encode[0], x_pca[0]]
```

* El segundo fetch que se hace es el que recibe el topk, aqui se llama a la funcion que se encargara de ejecutra los diferentes algoritmos y los guarda en un array
 ``` python 
@app.route('/api_consult_topk', methods=['POST'])
def consultTopk():
    global answers
    request_data = json.loads(request.data)
    topk = int(request_data['topk'])
    testing = search_all(parsedQuery, data_vectors, RTREE, DIC,
                         parsedQueryPCA, data_vectors_pca, RTREEPCA, DICPCA, topk)
    answers = testing
```
* El ultimo fetch, se llama multiples veces desde el frontend debido a que no pudimos hayar la forma de mandar muchas imagenes como response y que sean utilizables en el frontend. El fetch recibe la posicion del archivo que quiere recibir, y simplemente lo devuelve.

 ``` python 
 @app.route('/api_answers', methods=['POST'])
 def sendanswer():
    request_data = json.loads(request.data)
    pos = int(request_data['pos'])
    type = int(request_data['type'])
    return send_file(answers[type][pos], mimetype='image/jpeg')
 ```
### PCA
 * La maldición de dimensionalidad causa diversos efectos al organizar y analizar datos de grandes dimensiones. Esto provoca muchas veces una baja ineficiencia de los datos, en nuestro caso de los vectores característicos ya que los datos se vuelven más dispersos, también tiene impacto en el caso de la optimización y aprendizaje automático, afectando a los k vecinos más proximos de cada vector característico. ![knnfit2-1](https://user-images.githubusercontent.com/66433825/178222481-52176b25-5d2a-4df7-a3e0-7b563665b05d.png)

 *Es por esta razón que se necesita mitagar la maldición de dimensionalidad y en nuestro caso nos ayudamos con el PCA que obtuvimos de la libreria scikit-learn,el PCA nos permite reducir las dimensiones de nuestros vectores característicos apartir de una presion que se elegimos(95%).
 * Para utilizar el PCA, primero necesitamos nuestro csv de vectores caracteristicos anteriormente obtenidos de nuestra carpeta lfw
      ``` python 
      df = pd.read_csv("datos/data_vectorh.csv")
      ```
 * Luego se procede a estandarizar los datos
       ``` python 
      scaler = StandardScaler()
      scalert = scaler.fit_transform(x)
      ```
 * Definimos una precisión para nuestra reducción de dimensiones (95%)
     ``` python
    pca = PCA(.95)
    pcat = pca.fit_transform(scalert)
    dfActual = pd.DataFrame(data=pcat)
    dfFinal = pd.concat([df[["path"]], dfActual], axis=1)
    ```
 * Guardamos nuestro nuevo dataset con el que trabajaremos con el KNN secuencial y el KNN rtree
  ``` python
 dataset = "datos/data_vector_pca.csv"
 dfFinal.to_csv(dataset, header=None, index=False)
  ```
### Implementacion de Algoritmos de Busqueda KNN Secuencial y KNN Rtree Index,

* La funciones se adaptaron para que puedan funcionar tanto para la data despues de haber pasado por PCA como para la que no, recibe una query (vector caracteristico guardado en un numpy array), un k (numero de elementos traidos).
* En el caso del KNN Secuencial, adicionalmente lleva un diccionario, con datos en formato {nombre_img: vector_caracteristico}
* En el caso del KNN indexado Rtree, se debe mandar el indice rtree, y un diccionario en formato {indice: nombre_img}, esto debido a que el indice guarda los valores con un indice numerico, por lo tanto para poder obtener la direccion de la imagen, en el preprocesamiento rtree se creo tal diccionario, y fueron guardados en la carpeta json

> funcion searchKNN 
 ``` python 
def searchKNN(Query, k, dic_vectors):
    result = []
    for file in dic_vectors:
        dist = face_distance([Query], np.array(dic_vectors[file]))
        heapq.heappush(result, (-dist, file))
        if (len(result) > k):
            heapq.heappop(result)
    result.sort(key=lambda tup: tup[1])
    resultparser = [x[1] for x in result]
    return resultparser
```

> funcion searchRtree
 ``` python 
 def searchRtree(Query, k, dic2, ind):
    query = tuple(Query)
    result = list(ind.nearest(coordinates=query, num_results=k))
    resultparser = [dic2[str(x)] for x in result]
    return resultparser
```
### Implementacion de Algoritmo de Busqueda RangeSearch 
* Este algoritmo de busqueda no se visualiza en la aplicacion web, pero si en la parte de experimentacion, se adapto igual que los algoritmos anteriores y la unica diferencia es que debe pasarsele un radio.

 > funcion rangeSearch
 ``` python 
def rangeSearch(Query, dic_vectors, radio):
    result = []
    for file in dic_vectors:
        dist = face_distance([Query], np.array(dic_vectors[file]))
        if (dist < radio):
            result.append(dist)
    return result
   ```
   
## Librearias Usadas

 Se utilizaron las siguientes librerias:
 * face_recognition: Se utilizó las funciones face_encodings y face_distance. Se utilizo para obtener los vectores caracteristicos de cada imagen
 * pickle: Se utilizó las funciones load y dump
 * pandas: Se utilizo para el manejo de nuestro dataset
 * sklearn: Libreria importante para importar el PCA que viene incluido en la libreria. Se utilizó el PCA para reducir la dimensionalidad de los vectores caracteristicos que fueron pasados a traves de nuestro data_vector.csv
 * flask: Permite levantar la pagina web en localhost
 * rtree: Libreria usada para indexar los vectores caracteristicos.
 
## Eexperimentación

* Para los experimentos se crearon 3 archivos, experimentation, searchAllExp y timer, y se uso una imagen de Castillo, todo se guardo en la carpeta de experimentacion, y en el caso se quiera usar, se debe llevar los archivos, excepto por la imagen, a la carpeta de backend

* En el archivo experimentation, se creao la simulacion de la busqueda completa del programa en la funcion experiment_timer_vs, para poder obtener los tiempos de cada algoritmo. Asi como tambien se crea la funcion experiment_rangeSearch que permite obtener los tiempos del algoritmo de busqueda por rango

> funcion experiment_timer_vs: 
``` python
def experiment_timer_vs(cantity):
    data_vectors = {}
    with open('datos/data_vector.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for data in csv_reader:
            datos = [float(x) for x in data[1:]]
            data_vectors[data[0]] = datos
    data_vectors_pca = {}
    with open('datos/data_vector_pca.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for data in csv_reader:
            datos = [float(x) for x in data[1:]]
            data_vectors_pca[data[0]] = datos
    TYPE1 = "standart"
    TYPE2 = "pca"
    CANTITY = cantity
    RTREE = preprocessingrtree.create_rtree_index(CANTITY, TYPE1)
    RTREEPCA = preprocessingrtree.create_rtree_index(CANTITY, TYPE2)
    DIC = preprocessingrtree.readJson(CANTITY, TYPE1)
    DICPCA = preprocessingrtree.readJson(CANTITY, TYPE2)
    parsedQuery = None
    parsedQueryPCA = None

    file = "experimentacion\Castillo.jpg"
    [parsedQuery, parsedQueryPCA] = parseBasicEncode(file)

    search_all(parsedQuery, data_vectors, RTREE, DIC,
               parsedQueryPCA, data_vectors_pca, RTREEPCA, DICPCA, 8)
 ```
 > funcion experiment_rangeSearch:
``` python
def experiment_rangeSearch(radio):
    data_vectors = {}
    with open('datos/data_vector.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for data in csv_reader:
            datos = [float(x) for x in data[1:]]
            data_vectors[data[0]] = datos
    data_vectors_pca = {}
    with open('datos/data_vector_pca.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for data in csv_reader:
            datos = [float(x) for x in data[1:]]
            data_vectors_pca[data[0]] = datos
    parsedQuery = None
    parsedQueryPCA = None

    file = "experimentacion\Castillo.jpg"
    [parsedQuery, parsedQueryPCA] = parseBasicEncode(file)

    range_Search(parsedQuery, data_vectors,
                 parsedQueryPCA, data_vectors_pca, radio)
```

* En el archivo searchAllExp, se altero el archivo searchAll, para que se obtengan los tiempos de cada funcion y se imprimera

* El archivo timer se coloca la pagina de donde se extrajo, se usa para medir los tiempos, y es el mejor comparacion de tiempos nos arrojo

> class Timer 

``` python
class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class Timer:
    def __init__(self, text="Elapsed time: {:0.4f} seconds"):
        self._start_time = None
        self.text = text

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
```
* Los datos obtenidos de los prints se pasaron a https://infogram.com/ y se obtuvieron los grafos comparativos

### Lineal Search by Range Algoritm 
![WhatsApp Image 2022-07-11 at 2 47 13 AM](https://user-images.githubusercontent.com/66433825/178215044-5d3a94db-bc82-47a0-ba55-9bf8cf735f84.jpeg)

### Knn-Secuencial vs Knn-Rtree vs Knn-HighD(Rtree) vs Knn-HighD(Secuencial)
![WhatsApp Image 2022-07-11 at 2 32 06 AM](https://user-images.githubusercontent.com/66433825/178212023-89bbd24f-4ed9-4709-823b-b00c737fe0b5.jpeg)

### Video 
https://youtu.be/zSO5gA5PM2g
