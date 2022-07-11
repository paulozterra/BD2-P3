import { Inputimg } from "./Inputs/inputimg";
import { Inputtopk } from "./Inputs/inputstopk";
import React, { useState } from "react";

export const Input = ({ onInputsSubmit, listofInputs }) => {
  const [topk, setTopK] = useState("");
  const [selectedFile, setSelectedFile] = useState(null);
  const handleInputsChange = (newinput) => {
    setTopK(newinput);
  };

  const fetchImage = async (imageUrl) => {
    const imageObjectURL = URL.createObjectURL(imageUrl);
    setSelectedFile(imageObjectURL);
  };

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
  const onFileSelectError = ({ error }) => {
    alert(error);
  };

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

  return (
    <>
      <h3>CONSULTA:</h3>
      <Inputimg
        onFileSucess={onFileSelectSuccess}
        onFileError={onFileSelectError}
      ></Inputimg>
      <>
        <img src={selectedFile} alt="icons" className="center" />
      </>
      <div className="container__block">
        <h3>TOP K:</h3>
        <Inputtopk onInputsChange={handleInputsChange} />
        <button
          type="submit"
          className="white2"
          onClick={(e) => handleSubmit(e)}
        >
          Buscar
        </button>
      </div>
    </>
  );
};
