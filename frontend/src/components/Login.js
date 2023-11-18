import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';

export const LoginForm = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    username: '',
    password: '',
  });


  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const [csrfToken, setCsrfToken] = useState('');

  useEffect(() => {
    // Получаем CSRF-токен из куки
    const csrfCookie = document.cookie.split('; ')
      .find(row => row.startsWith('csrftoken='))
      .split('=')[1];
    setCsrfToken(csrfCookie);
  }, []);
  
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://localhost:8000/account/api/login/', formData, {
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken,
          // 'Authorization': `${btoa(`${formData.username}:${formData.password}`)}`, 
        },
        // withCredentials: true, 
      });

      if (response.status === 200) {
         // sessionStorage.setItem('auth', btoa(`${formData.username}:${formData.password})`));
        navigate('/use-nn');
      } else {
        console.error('Ошибка при авторизации');
      }
    } catch (error) {
      console.error('Ошибка при отправке запроса:', error);
    }
  };
    
  return (
    <div className="container mt-5">
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="username" className="form-label">
            Username:
            <input
              type="text"
              className="form-control"
              id="username"
              name="username"
              value={formData.username}
              onChange={handleChange}
            />
          </label>
        </div>
        <div className="mb-3">
          <label htmlFor="password" className="form-label">
            Password:
            <input
              type="password"
              className="form-control"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
            />
          </label>
        </div>
        <button type="submit" className="btn btn-primary">
          Login
        </button>
      </form>
    </div>
  );
};

