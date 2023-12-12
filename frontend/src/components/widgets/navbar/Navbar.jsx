import React from 'react';
import { Navbar, Container, Nav } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import {ThemeSwitcher } from './ThemeSwitcher';

export const AppNavbar = () => {
  return (
<Navbar bg="light" variant="light">
  <Container>
    <Navbar.Brand as={Link} to="/use-nn">Emotion Recognizer</Navbar.Brand>
    <Nav className="me-right">
      <Nav.Link as={Link} to="/history">History</Nav.Link>
    </Nav>
    <Nav className="me-auto">
      <Nav.Link as={Link} to="/change-password">Settings</Nav.Link>
    </Nav>
    {/*<ThemeSwitcher/>*/}
  </Container>
</Navbar>
  );
};
