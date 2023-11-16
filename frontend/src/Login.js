import React from 'react';

function LoginForm({ onSubmit, form, onRegisterClick }) {
  return (
    <div>
      <h1>Log in to account</h1>

      <form onSubmit={onSubmit}>
        <div className="form-error">{form.non_field_errors}</div>

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

        <button type="submit">Log In</button>
      </form>

      <button onClick={handleClick}>
  No account? Register
</button>

    </div>
  );
}

export default LoginForm;
