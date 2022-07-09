import React, { useState } from "react";
import { Result } from "./result";

export const Results = ({ listofResult }) => {
  let result = undefined;
  let result_sql = undefined;
  let time = "";
  let time_sql = "";

  const parseData = (object_data) => {
    let list_data = [];
    let temp = [];
    for (const property in object_data) {
      temp.push(property);
      temp.push(...object_data[property]);
      list_data.push(temp);
      temp = [];
    }
    //reestructurar mayor score
    list_data.sort((a, b) => (a[4] < b[4] ? 1 : -1));
    return list_data;
  };
  //lista de lista -> id tw, text, fecha,usuario,score
  if (listofResult != undefined) {
    result = parseData(listofResult["data"]);
    result_sql = parseData(listofResult["data_sql"]);
    time = listofResult["time"];
    time_sql = listofResult["times_sql"];
  }

  return (
    <>
      <div className="container__block">
        <div className="container__top python">
          <h2>TopK - Python</h2>
          <Result listofResult={result} />
          <h3>Tiempo: {time} </h3>
        </div>
        <div className="container__top postgresql">
          <h2>TopK - PostgreSQL</h2>
          <Result listofResult={result_sql} />
          <div className="time">
            <h3>Tiempo: {time_sql} </h3>
          </div>
        </div>
      </div>
    </>
  );
};
