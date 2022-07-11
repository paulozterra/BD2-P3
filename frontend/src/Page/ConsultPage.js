import React, { useState, useEffect } from "react";
import { Results } from "../Components/Result/results";
import { Input } from "../Components/Form/input";
export const ConsultPage = () => {
  const [result, setResult] = useState(undefined);
  const [knnaux, setKnnAux] = useState([]);
  const [rtreeaux, setRtreeAux] = useState([]);
  const handleInputSubmit = async (topk) => {
    setResult([]);
    //topk = 1;

    for (let i = 0; i < topk; i++) {
      let knn = img(i, 0);
      let rtree = img(i, 1);
      knn.then((response) => getImg(response, 0));
      rtree.then((response) => getImg(response, 1));
      //knndata.push(getImg(i, 0));
      //rtreedata.push(getImg(i, 1));
    }
    test(knnaux.length, rtreeaux.length, topk);
  };

  const test = (len1, len2, topk) => {
    if (len1 == topk && len2 == topk) {
      setLastResult([knnaux, rtreeaux]);
    }
  };

  const setLastResult = (data) => {
    setResult(data);
  };

  const getImg = async (aux, type) => {
    if (aux != undefined) {
      console.log(aux);
      const reader = new FileReader();
      reader.readAsDataURL(aux);
      reader.onloadend = () => {
        const base64data = reader.result;
        if (type == 0) {
          setKnnAux((old) => [...old, base64data]);
        } else setRtreeAux((old) => [...old, base64data]);
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
    })
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
      })
      .then((data) => {
        console.log(data);
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
