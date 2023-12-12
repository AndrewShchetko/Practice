import React from 'react';
import { Route, Routes } from 'react-router-dom';
//import {appRoutes} from './config';
import { LoginForm } from './components/Login';
import { RegistrationForm } from './components/Registration';
import { NeuralNetworkForm } from './components/NNfrom';
import { ChangePasswordForm } from './components/Settings';
import { HistoryComponent } from './components/History';


export const AppRoutes = () => {
  return(
//  <Routes>
//    {/* {Object.values(appRoutes).map((route) => (
//      <Route key={route.path} path={route.path} element={route.element} />
//    ))} */}
//    <Route path='/' element={<LoginForm/>}/>
//  </Routes>);
      <Routes>
        <Route path="/" element={<LoginForm/>} />
        <Route path="/registration" element={<RegistrationForm />} />
        <Route path="/change-password" element={<ChangePasswordForm />} />
        <Route path="/use-nn" element={<NeuralNetworkForm />} />
        <Route path="/history" element={<HistoryComponent />} />
      </Routes>
  );
};
