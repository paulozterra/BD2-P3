export const Inputtopk = ({ onInputsChange }) => {
  const handleChange = (event) => {
    onInputsChange(event.target.value);
  };
  return (
    <>
      <input
        name="topk"
        className="white3"
        placeholder="Top K"
        onChange={(e) => handleChange(e)}
      />
    </>
  );
};
