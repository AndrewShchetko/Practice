import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Card } from 'react-bootstrap';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import { ToastContainer } from 'react-toastify';
import { errorToast } from './widgets/floating_windows/error_toast';
import 'react-toastify/dist/ReactToastify.css';

export const HistoryComponent = () => {
  const [results, setResults] = useState([]);
  const [csrfToken, setCsrfToken] = useState('');

  useEffect(() => {
    // Получаем CSRF-токен из куки
    const csrfCookie = document.cookie.split('; ')
      .find(row => row.startsWith('csrftoken='))
      .split('=')[1];
    setCsrfToken(csrfCookie);
  }, []);

  useEffect(() => {
    const fetchResults = async () => {
      try {
        const response = await axios.get('http://localhost:8000/account/api/list/', {
          headers: {
            'Content-Type': 'multipart/form-data',
            'X-CSRFToken': csrfToken,
          },
          withCredentials: true,
        });
        console.log('Response data:', response.data); // Log the response data

        if (response.status === 200) {
          setResults(response.data);
        } else {
          console.error('Ошибка при получении результатов');
          errorToast('Ошибка при получении результатов');
        }
      } catch (error) {
        console.error('Ошибка при отправке запроса:', error);
        errorToast('Ошибка при отправке запроса');
      }
    };

    fetchResults();
  }, [csrfToken]);

  return (
    <Container fluid>
      <ToastContainer />
      <h1 style={{ color: 'white' }}>History</h1>
      <Row xs={1} md={3} className="g-4">
        {results.map((result, index) => (
          <Col key={index}>
            <Card className="mb-3">
              <Card.Img src={result.image.image} alt="Result" className="card-img-top" />
              <Card.Body>
                <Card.Title style={{ color: 'black' }}>Emotion: {result.emotion}</Card.Title>
                <Card.Text style={{ color: 'black' }}>Comment: {result.image.comment}</Card.Text>
              </Card.Body>
            </Card>
          </Col>
        ))}
      </Row>
    </Container>
      );
    };
    