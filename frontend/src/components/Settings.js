import React, { useState } from 'react';
import { Form, Button } from 'react-bootstrap';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';

export const ChangePasswordForm = () => {
  const [formData, setFormData] = useState({
    username: '',
    old_password: '',
    new_password: '',
  });

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
        },
      });

      if (response.status === 200) {
        // Смена пароля прошла успешно, обработка успешного ответа
        console.log('Пароль успешно изменен');
      } else {
        // Обработка ошибки
        console.error('Ошибка при смене пароля');
      }
    } catch (error) {
      console.error('Ошибка при отправке запроса:', error);
    }
  };

  return (
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
  );
};
