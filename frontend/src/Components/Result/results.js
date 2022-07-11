import React from "react";
import { Result } from "./result";

export const Results = ({ listofResult }) => {
  let knn_results = undefined;
  let rtree_results = undefined;
  let knnpca_results = undefined;
  let rtreepca_results = undefined;
  let time = "";
  let time_sql = "";
  let time3 = "";
  let time4 = "";

  //lista de lista -> id tw, text, fecha,usuario,score
  if (listofResult !== undefined && listofResult !== []) {
    knn_results = listofResult[0];
    rtree_results = listofResult[1];
    knnpca_results = listofResult[2];
    rtreepca_results = listofResult[3];
    time = "1.5";
    time_sql = "1.6";
    time3 = "0";
    time4 = "1";
  }

  return (
    <>
      <div className="container__block">
        <div className="container__top knn">
          <h2>Knn Secuential</h2>
          <Result listofResult={knn_results} />
          <h3>Tiempo: {} </h3>
        </div>
        <div className="container__top rtree">
          <h2>Rtree</h2>
          <Result listofResult={rtree_results} />
          <div className="time">
            <h3>Tiempo: {} </h3>
          </div>
        </div>
        <div className="container__top pca">
          <h2>PCA Knn</h2>
          <Result listofResult={knnpca_results} />
          <div className="time">
            <h3>Tiempo: {} </h3>
          </div>
        </div>
        <div className="container__top pca">
          <h2>PCA Rtree</h2>
          <Result listofResult={rtreepca_results} />
          <div className="time">
            <h3>Tiempo: {} </h3>
          </div>
        </div>
      </div>
    </>
  );
};
