import React from 'react';

function RegisterForm({ onSubmit, form }) {
  return (
    <div>
      <h1>Register</h1>

      <form onSubmit={onSubmit}>
        <input type="hidden" name="csrfmiddlewaretoken" value={/* передайте ваш CSRF-токен здесь */} />

        {/* Переписать этот участок в соответствии с React */}
        {form.map((f) => (
          <div key={f.id}>
            <p>
              <label className="form-label" htmlFor={f.id_for_label}>
                {f.label}:
              </label>
              {f}
            </p>
            <div className="form-error">{f.errors}</div>
          </div>
        ))}
        {/* Конец переписанной части */}

        <button type="submit">Register</button>
      </form>
    </div>
  );
}

export default RegisterForm;
