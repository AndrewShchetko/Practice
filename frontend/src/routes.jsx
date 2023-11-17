import React from 'react';
import { Route, Routes } from 'react-router-dom';
import { LoginForm } from './components/Login';
import { RegistrationForm } from './components/Registration';
import { NeuralNetworkForm } from './components/NNfrom';
import { ChangePasswordForm } from './components/Settings';
import { ResultsComponent } from './components/History';


export const AppRoutes = () => {
  return (
      <Routes>
        <Route path="/" element={<LoginForm/>} />
        <Route path="/register" element={<RegistrationForm />} />
        <Route path="/change-password" element={<ChangePasswordForm />} />
        <Route path="/use-nn" element={<NeuralNetworkForm />} />
        <Route path="/results" element={<ResultsComponent />} />
      </Routes>
  );
};
