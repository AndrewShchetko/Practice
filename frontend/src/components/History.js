import React, { useState, useEffect } from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';


export const ResultsComponent = () => {
  const [results, setResults] = useState([]);

  useEffect(() => {
    const fetchResults = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/list/', {
          headers: {
            'Content-Type': 'application/json',
            // Добавьте токен авторизации, если он необходим
            // 'Authorization': `Bearer ${yourAccessToken}`
          },
        });

        if (response.status === 200) {
          setResults(response.data);
        } else {
          console.error('Ошибка при получении результатов');
        }
      } catch (error) {
        console.error('Ошибка при отправке запроса:', error);
      }
    };

    fetchResults();
  }, []); // Пустой массив зависимостей, чтобы запрос выполнялся только один раз при загрузке компонента

  return (
    <Container>
      <h1>Results</h1>
      <Row>
        <Col>
          <ul>
            {results.map((result) => (
              <li key={result.image.id}>
                <img src={result.image.image} alt="Result" />
                <p>Comment: {result.image.comment}</p>
                <p>Emotion: {result.emotion}</p>
              </li>
            ))}
          </ul>
        </Col>
      </Row>
    </Container>
  );
};
