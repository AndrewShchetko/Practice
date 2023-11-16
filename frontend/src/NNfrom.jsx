import React from 'react';

function NNForm({ onSubmit, form, emotion }) {
  return (
    <div>
      <h1>Use NN</h1>

      <form onSubmit={onSubmit} encType="multipart/form-data">
        <div className="form-error">{form.non_field_errors}</div>
        {form.as_p}

        <button type="submit">Send</button>
      </form>

      <h1>Emotion: {emotion}</h1>
    </div>
  );
}

export default NNForm;
