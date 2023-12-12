import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { errorToast } from './widgets/floating_windows/error_toast';

export const LoginForm = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    username: '',
    password: '',
  });
  
  const [csrfToken, setCsrfToken] = useState('');

  useEffect(() => {
    // Получаем CSRF-токен из куки
    const csrfCookie = document.cookie.split('; ')
      .find(row => row.startsWith('csrftoken='))
      .split('=')[1];
    setCsrfToken(csrfCookie);
  }, []);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/account/api/login/', formData, {
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken,
        },
        withCredentials: true
      });
      if (response.status === 200) {
        navigate('/use-nn');
      } else if(response.status === 403) {
        console.error('Ошибка при авторизации');
        errorToast('Ошибка при авторизации')
      }
    } catch (error) {
      console.error('Ошибка при отправке запроса:', error);
      errorToast('Ошибка при отправке запроса')
    }
  };

  return (
<div className="container-fluid d-flex justify-content-center align-items-center vh-100 bg-dark">
      <div className="card p-4 bg-light border-light">
        <ToastContainer />
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
          <button type="submit" className="btn btn-primary rounded-pill">
            Login
          </button>
          <button type="button" className="btn btn-success rounded-pill mx-2" onClick={() => navigate('/registration')}>
            Sign up
          </button>
        </form>
      </div>
    </div>

  );
}