import { useNavigate } from 'react-router-dom';
import './../App.css';

function Tutorial() {

    // Define Back Button
    function BackButton({ onClick }) {
        return (
            <button className="button back-button" onClick={onClick}>
                ← Back
            </button>
        );
    }

    const navigate = useNavigate();
    const navigateToStart = () => {
        // Handle Navigation To Start Page
        navigate("/hello_world"); // CHANGE HERE TO GET TO START PAGE OF TEST
    };

    const handleBackClick = () => {
        // Handle click event for the back button
        navigate("/login");
    };

    return (
        // Formatting
        <div className="container-fluid d-flex align-items-center justify-content-center">
            {/*Back Button, Logo and Text on Page*/}
            <BackButton onClick={handleBackClick} />
            <div className="content">
                <h1>Information</h1>
                <div className='scroll-box border rounded p-3'>
                    <p>Lorem ipsum Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.</p>
                </div>
                {/*Login Button*/}
                <br></br>
                <button className="button" onClick={navigateToStart}>➠ Starten</button>
            </div>
        </div>
    );
}

export default Tutorial;