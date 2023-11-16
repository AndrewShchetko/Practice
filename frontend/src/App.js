import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Navbar from './Navbar';
import Home from './Home';
import LoginForm from './Login';
import Register from './Register';
import Settings from './Settings';
import NNForm from './NNForm';

function App() {
  return (
    <Router>
      <Navbar />
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/login" component={LoginForm} />
        <Route path="/register" component={Register} />
        <Route path="/settings" component={Settings} />
        <Route path="/nnform" component={NNForm} />
      </Switch>
    </Router>
  );
}

export default App;
