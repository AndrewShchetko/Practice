import React, { useState, useEffect } from 'react';
import { Form, Button, Container, Row, Col } from 'react-bootstrap';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import { ToastContainer} from 'react-toastify';
import { errorToast } from './widgets/floating_windows/error_toast';

export const ChangePasswordForm = () => {
  const [formData, setFormData] = useState({
    username: '',
    old_password: '',
    new_password: '',
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
      const response = await axios.post('http://localhost:8000/account/api/change-password/', formData, {
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken,
        },
        withCredentials: true,
      });

      if (response.status === 200) {
        // Смена пароля прошла успешно, обработка успешного ответа
        console.log('Пароль успешно изменен');
      } else {
        // Обработка ошибки
        console.error('Ошибка при смене пароля');
        errorToast('Ошибка при смене пароля');
      }
    } catch (error) {
      console.error('Ошибка при отправке запроса:', error);
      errorToast('Ошибка при отправке запроса');
    }
  };

  return (
    <div className="bg-dark vh-100">
      <ToastContainer/>
    <Container className="d-flex justify-content-center align-items-center h-100">
      <Row>
        <Col md={15}>
          <div className="card p-4 bg-light border-light">
            <Form onSubmit={handleSubmit}>
              <Form.Group className="mb-3" controlId="formBasicUsername">
                <Form.Label>Username:</Form.Label>
                <Form.Control
                  type="text"
                  name="username"
                  value={formData.username}
                  onChange={handleChange}
                />
              </Form.Group>

              <Form.Group className="mb-3" controlId="formBasicOldPassword">
                <Form.Label>Old Password:</Form.Label>
                <Form.Control
                  type="password"
                  name="old_password"
                  value={formData.old_password}
                  onChange={handleChange}
                />
              </Form.Group>

              <Form.Group className="mb-3" controlId="formBasicNewPassword">
                <Form.Label>New Password:</Form.Label>
                <Form.Control
                  type="password"
                  name="new_password"
                  value={formData.new_password}
                  onChange={handleChange}
                />
              </Form.Group>

              <Button variant="primary" type="submit">
                Change Password
              </Button>
            </Form>
          </div>
        </Col>
      </Row>
    </Container>
  </div>
  );
};
