import React, { useState, useEffect } from 'react';
import { Form, Button, Col, Row } from 'react-bootstrap';
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
  const [inputImageURL, setInputImageURL] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleImageChange = (e) => {
    const selectedImage = e.target.files[0];
    setFormData({
      ...formData,
      image: selectedImage,
    });

    setInputImageURL(URL.createObjectURL(selectedImage));
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
        const { emotion } = response.data;
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
        <Row>
          <Col md={8}>
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
          </Col>
          <Col md={4}>
  {formData.image && (
    <div className="mt-3 border rounded p-2" style={{ borderWidth: '4px', borderColor: '#007bff', borderStyle: 'solid' }}>
      <strong>Selected Image:</strong>
      <img
        src={inputImageURL}
        alt="Selected"
        className="img-fluid mt-2"
      />
    </div>
  )}
</Col>

        </Row>

        <ToastContainer />

        {/* Display the emotion on the page */}
        {resultText && (
          <div className="mt-3">
            <strong style={{ fontSize: '24px' }}>Emotion:</strong>
            <span style={{ fontSize: '24px', marginLeft: '8px' }}>{resultText}</span>
          </div>
        )}
      </div>
    </div>
  );
};
