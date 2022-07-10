import React, { useRef } from "react";
export const Inputimg = ({ onFileSucess, onFileError }) => {
  const fileInput = useRef(null);

  const handleFileInput = (e) => {
    // handle validations
    const file = e.target.files[0];
    if (file.size > 100024) {
      console.log(file.size);
      onFileError({ error: "file is too big" });
    } else onFileSucess(file, e);
  };

  return (
    <>
      <input
        type="file"
        name="consult"
        className="textarea__consult white4"
        placeholder="Texto de la consulta"
        onChange={handleFileInput}
      ></input>
    </>
  );
};
