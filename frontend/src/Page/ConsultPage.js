import React, { useState, useEffect } from "react";
import { Results } from "../Components/Result/results";
import { Input } from "../Components/Form/input";
export const ConsultPage = () => {
  const [result, setResult] = useState(undefined);

  const handleInputSubmit = (data) => {
    getLatestTodos(data);
  };

  const getLatestTodos = (data) => {
    setResult(data);
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
