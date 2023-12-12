import React from 'react';
import {AppRoutes} from './routes';
import { BrowserRouter } from 'react-router-dom';
import { AppNavbar as Navbar } from './components/widgets/navbar/Navbar';

const App = () => {
  return (
    <BrowserRouter>
      <Navbar /> 
      <AppRoutes />
    </BrowserRouter>
  );
}

export default App;
