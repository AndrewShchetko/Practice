import React, { useState, useEffect } from 'react';
import { Form, Button } from 'react-bootstrap';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

export const NeuralNetworkForm = () => {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    image: null,
    comment: '',
  });
  const [resultText, setResultText] = useState('');

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
      data.append('image', formData.image);
      data.append('comment', formData.comment);

      const response = await axios.post('http://localhost:8000/api/result/', data, {
        headers: {
          'Content-Type': 'multipart/form-data',
          'X-CSRFToken': csrfToken,
        },
        withCredentials: true,
      });

      if (response.status === 201 || response.status === 200) {
        navigate('/use-nn');
        const { emotion } = response.data; // Access 'emotion' directly
        setResultText(emotion);
      } else {
        toast.error('Ошибка при отправке данных');
      }
    } catch (error) {
      console.error('Error during API request:', error);
      toast.error('Ошибка при отправке запроса');
    }
  };

  return (
<div className="container-fluid d-flex justify-content-center align-items-center vh-100 bg-dark">
      <div className="card p-4 bg-light border-light">
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
        <ToastContainer />
        {/* Display the emotion on the page */}
        {resultText && (
          <div className="mt-3">
            <strong>Emotion:</strong> {resultText}
          </div>
        )}
      </div>
    </div>
  );
};
