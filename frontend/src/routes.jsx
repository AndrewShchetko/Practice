import { BrowserRouter as Router, Link, Route, useRoutes } from 'react-router-dom';
import LoginForm from './Login';
import RegisterForm from './Registration';
import NNForm from './NNfrom';

const AppRoutes = () =>{
   const routeElements = useRoutes(
    [
        { path: '/', element: <LoginForm /> },
        { path: '/register', element: <RegisterForm /> },
        { path: '/nnform', element: <NNForm /> },
    ]
   )
   return (
    <Router>
      <nav>
        <ul>
          <li>
            <Link to="/">Login</Link>
          </li>
          <li>
            <Link to="/register">RegisterForm</Link>
          </li>
          <li>
            <Link to="/nnform">Use NN</Link>
          </li>
        </ul>
      </nav>
      {routeElements}
    </Router>
  );
}
export default AppRoutes;