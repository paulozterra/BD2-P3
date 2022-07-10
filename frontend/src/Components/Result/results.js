import React from "react";
import { Result } from "./result";

export const Results = ({ listofResult }) => {
  let knn_results = undefined;
  let rtree_results = undefined;
  let time = "";
  let time_sql = "";

  //lista de lista -> id tw, text, fecha,usuario,score
  if (listofResult !== undefined && listofResult !== []) {
    knn_results = listofResult[0];
    rtree_results = listofResult[1];
    time = "1.5";
    time_sql = "1.6";
  }

  return (
    <>
      <div className="container__block">
        <div className="container__top python">
          <h2>TopK - Python</h2>
          <Result listofResult={knn_results} />
          <h3>Tiempo: {time} </h3>
        </div>
        <div className="container__top postgresql">
          <h2>TopK - PostgreSQL</h2>
          <Result listofResult={rtree_results} />
          <div className="time">
            <h3>Tiempo: {time_sql} </h3>
          </div>
        </div>
      </div>
    </>
  );
};
