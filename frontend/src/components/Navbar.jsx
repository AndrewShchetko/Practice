import React from 'react';
import { Navbar, Container, Nav } from 'react-bootstrap';
import { Link } from 'react-router-dom';

export const AppNavbar = () => {
  return (
    <Navbar bg="dark" variant="dark">
      <Container>
        <Navbar.Brand as={Link} to="/">Emotion Recognizer</Navbar.Brand>
        <Nav className="me-auto">
          <Nav.Link as={Link} to="/change-password">Settings</Nav.Link>
        </Nav>
      </Container>
    </Navbar>
  );
};
