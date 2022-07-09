import React from "react";

export const Result = ({ listofResult }) => {
  const Rows = (props) => {
    const listResult = props.ExistConsult;
    if (listResult === undefined) {
      return <></>;
    }
    console.log(listResult);
    return (
      <>
        {listResult.map((todo) => {
          return (
            <div className="rTableRow" key={todo[0]}>
              <div className="rTableCell">{todo[3]} </div>
              <div className="rTableCell">{todo[1]} </div>
              <div className="rTableCell">{todo[4]} </div>
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
          <div className="rTableRow">
            <div className="rTableHead">
              <strong>User</strong>
            </div>
            <div className="rTableHead">
              <span style={{ fontweight: "bold" }}>Text</span>
            </div>
            <div className="rTableHead">Score</div>
          </div>
          <Rows ExistConsult={listofResult} />
        </div>
      </div>
    </>
  );
};
