export const Input = ({ onInputsChange, onInputsSubmit, listofInputs }) => {
  const handleChange = (event) => {
    const newinput = { ...listofInputs };
    newinput[event.target.name] = event.target.value;
    onInputsChange(newinput);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    fetch("/api/consult", {
      method: "POST",
      body: JSON.stringify({
        consult: listofInputs.consult,
        topk: listofInputs.topk,
      }),
    })
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
      })
      .then((data) => {
        console.log(data);
      });
  };

  return (
    <>
      <h1>UTEC SEARCH</h1>
      <h3>CONSULTA:</h3>
      <input
        name="consult"
        className="textarea__consult white4"
        placeholder="Texto de la consulta"
        onChange={(e) => handleChange(e)}
      ></input>
      <div className="container__block">
        <h3>TOP K:</h3>
        <input
          name="topk"
          className="white3"
          placeholder="Top K"
          onChange={(e) => handleChange(e)}
        />
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
