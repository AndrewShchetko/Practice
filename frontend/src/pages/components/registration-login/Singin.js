import {FloatingLabel as BootstrapFloatingLabel} from 'react-bootstrap/FloatingLabel';
import {Form as BootstrapForm} from 'react-bootstrap/Form';

function FormSignIn() {
  return (
    <>
      <BootstrapFloatingLabel
        controlId="floatingInput"
        label="Email address"
        className="mb-3"
      >
        <BootstrapForm.Control type="email" placeholder="name@example.com" />
      </BootstrapFloatingLabel>
      <BootstrapFloatingLabel controlId="floatingPassword" label="Password">
        <BootstrapForm.Control type="password" placeholder="Password" />
      </BootstrapFloatingLabel>
    </>
  );
}

export default FormSignIn;