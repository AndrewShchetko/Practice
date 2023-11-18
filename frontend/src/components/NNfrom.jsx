import React, { useState, useEffect } from "react";
import { Form, Button } from "react-bootstrap";
import axios from "axios";
import { useNavigate } from "react-router-dom";

export const NeuralNetworkForm = () => {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    image: null,
    comment: "",
  });
  const [resultText, setResultText] = useState('');

  // const authHeader = `${sessionStorage.getItem('auth')}`;

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleImageChange = (e) => {
    setFormData({
      ...formData,
      image: e.target.files[0],
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
      const data = new FormData();
      data.append("image", formData.image);
      data.append("comment", formData.comment);

      const response = await axios.post(
        "http://localhost:8000/api/result/",
        data, {
          headers: {
            'Content-Type': 'multipart/form-data',
            // 'Authorization': authHeader,
            'X-CSRFToken': csrfToken,
          },withCredentials: true, 
        });

      if (response.status === 200) {
        navigate("/use-nn");
        const { resultText } = response.data;
        setResultText(resultText);
      } else {
        console.error("Ошибка при отправке данных");
      }
    } catch (error) {
      console.error("Error during API request:", error);
    }
  };

  return (
    <div>
      <Form onSubmit={handleSubmit}>
        <Form.Group className="mb-3">
          <Form.Label>Comment:</Form.Label>
          <Form.Control
            type="text"
            name="comment"
            value={formData.comment}
            onChange={handleChange}
          />
        </Form.Group>
        <Form.Group className="mb-3">
          <Form.Label>Image:</Form.Label>
          <Form.Control
            type="file"
            name="image"
            accept="image/*"
            onChange={handleImageChange}
          />
        </Form.Group>
        <Button variant="primary" type="submit">
          Submit
        </Button>
      </Form>
      {resultText && (
        <div className="result-container">
          <h3>Result Text:</h3>
          <p>{resultText}</p>
        </div>
      )}
    </div>
  );
};
