import {Navbar as BootstrapNavbar} from 'react-bootstrap/Navbar';
import {Image as BootstrapImage} from 'react-bootstrap/Image';

function Navbar(){
return(
    <Navbar expand="lg" className="bg-body-tertiary">
      <Container>
        <Navbar.Brand href="#home">
            <img
              src="/img/logo.svg"
              width="30"
              height="30"
              className="d-inline-block align-top"
              alt="React Bootstrap logo"
            />
         </Navbar.Brand>
        </Container>
   </Navbar>
)
}

export default Navbar;