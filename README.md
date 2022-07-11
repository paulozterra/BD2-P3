# BD2-P3

## Introducción

En este proyecto, se busco recrear el reconocimiento de rostros, en base a mas de 13 mil datos que se encuentran en la carpeta lfw, se implementó diferentes versiones del algoritmo de busqueda KNN, Secuencial, indexado con Rtree, y HighD (PCA) en el caso de nuestro grupo.

## Preprocesamiento
La mayoria de datos que se cargan en los archivos .py que tiene prefijo preprocesamiento, cargan los archivos .csv, y los indices que llevarian buen tiempo cargarse en tiempo real.

* preprocessingPCA


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
** Implementacion de Algoritmo KNN Secuencial
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
** Implementacion de Algoritmo KNN indexado Rtree
 ``` python 
 def searchRtree(Query, k, dic2, ind):
    query = tuple(Query)
    result = list(ind.nearest(coordinates=query, num_results=k))
    resultparser = [dic2[str(x)] for x in result]
    return resultparser
 ```
 ``` python 
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
