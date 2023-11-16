import React, { useState } from 'react';

function RegisterForm({ onSubmit, form }) {
  const [csrfToken, setCsrfToken] = useState('');

  const handleCsrfToken = () => {
    // Ваш код для получения CSRF-токена
    // Например, можно использовать fetch или axios для запроса к вашему API
    // и затем установить полученный токен в состояние
    setCsrfToken('your_obtained_csrf_token');
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // Ваш код для обработки отправки формы
    onSubmit();
  };

  // Вызываем хэндлер для получения CSRF-токена при монтировании компонента
  React.useEffect(() => {
    handleCsrfToken();
  }, []);

  return (
    <div>
      <h1>Register</h1>

      <form onSubmit={handleSubmit}>
        {/* Передача CSRF-токена в виде скрытого поля */}
        <input type="hidden" name="csrfmiddlewaretoken" value={csrfToken} />

        {/* Переписанный участок формы с использованием React */}
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


//function RegisterForm({ onSubmit, form }) {
//  return (
//    <div>
//      <h1>Register</h1>
//
//      <form onSubmit={onSubmit}>
//        <input type="hidden" name="csrfmiddlewaretoken" value={/* передайте ваш CSRF-токен здесь */} />
//
//        {/* Переписать этот участок в соответствии с React */}
//        {form.map((f) => (
//          <div key={f.id}>
//            <p>
//              <label className="form-label" htmlFor={f.id_for_label}>
//                {f.label}:
//              </label>
//              {f}
//            </p>
//            <div className="form-error">{f.errors}</div>
//          </div>
//        ))}
//        {/* Конец переписанной части */}
//
//        <button type="submit">Register</button>
//      </form>
//    </div>
//  );
//}
//
//export default RegisterForm;
