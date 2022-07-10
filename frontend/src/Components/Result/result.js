import React from "react";

export const Result = ({ listofResult }) => {
  const Rows = (props) => {
    const listResult = props.ExistConsult;
    if (listResult === undefined || listResult === []) {
      return <></>;
    }
    console.log(listResult);
    return (
      <>
        {listResult.map((todo, index) => {
          return (
            <div className="rTableRow" key={index}>
              <img src={todo} alt="" />
            </div>
          );
        })}
      </>
    );
  };
  return (
    <>
      <div className="container__top-consult white5">
        <div className="rTable">
          <Rows ExistConsult={listofResult} />
        </div>
      </div>
    </>
  );
};
