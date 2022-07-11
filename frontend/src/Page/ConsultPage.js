import React, { useState, useEffect } from "react";
import { Results } from "../Components/Result/results";
import { Input } from "../Components/Form/input";
export const ConsultPage = () => {
  const [result, setResult] = useState(undefined);
  const [knnaux, setKnnAux] = useState([]);
  const [rtreeaux, setRtreeAux] = useState([]);
  const [knnauxpca, setKnnAuxPca] = useState([]);
  const [rtreeauxpca, setRtreeAuxPca] = useState([]);

  const setEmpty = () => {
    setResult([]);
    setKnnAux([]);
    setRtreeAux([]);
    setKnnAuxPca([]);
    setKnnAuxPca([]);
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

  const test = (len1, len2, len3, len4, topk) => {
    if (len1 == topk && len2 == topk && len3 == topk && len4 == topk) {
      setLastResult([knnaux, rtreeaux, knnauxpca, rtreeauxpca]);
    }
  };

  const setLastResult = (data) => {
    setResult(data);
  };

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

  const img = async (pos_, type_) => {
    const res = await fetch("/api_answers", {
      method: "POST",
      body: JSON.stringify({ pos: pos_, type: type_ }),
    });
    if (!res.ok) throw new Error(res.statusText);
    const data = await res.blob();
    return data;
  };

  useEffect(() => {
    fetch("/api", {
      method: "POST",
    }).then((response) => {
      if (response.ok) {
        return response.json();
      }
    });
  }, []);

  return (
    <>
      <h1>UTEC SEARCH</h1>
      <Input onInputsSubmit={handleInputSubmit}></Input>

      <Results listofResult={result}></Results>
    </>
  );
};
