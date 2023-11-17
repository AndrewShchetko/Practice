import React, { useState } from "react";
import { Form, Button } from "react-bootstrap";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";

export const RegistrationForm = () => {
  const [formData, setFormData] = useState({
    username: "",
    password1: "",
    password2: "",
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
      const response = await axios.post(
        "http://localhost:8000/account/api/register/",
        formData,
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      if (response.status === 200) {
        // Регистрация прошла успешно, обработка успешного ответа
        console.log("Пользователь зарегистрирован успешно");
      } else {
        // Обработка ошибки
        console.error("Ошибка при регистрации");
      }
    } catch (error) {
      console.error("Ошибка при отправке запроса:", error);
    }
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group className="mb-3" controlId="formUsername">
        <Form.Label>Username:</Form.Label>
        <Form.Control
          type="text"
          name="username"
          value={formData.username}
          onChange={handleChange}
        />
      </Form.Group>

      <Form.Group className="mb-3" controlId="formPassword1">
        <Form.Label>Password:</Form.Label>
        <Form.Control
          type="password"
          name="password1"
          value={formData.password1}
          onChange={handleChange}
        />
      </Form.Group>

      <Form.Group className="mb-3" controlId="formPassword2">
        <Form.Label>Confirm Password:</Form.Label>
        <Form.Control
          type="password"
          name="password2"
          value={formData.password2}
          onChange={handleChange}
        />
      </Form.Group>

      <Button variant="primary" type="submit">
        Register
      </Button>
    </Form>
  );
};
