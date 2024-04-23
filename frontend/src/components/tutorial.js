import { useNavigate } from 'react-router-dom';
import './../App.css';

function Tutorial() {

    // Define Back Button
    function BackButton({ onClick }) {
        return (
            <button className="back-button" onClick={onClick}>
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
        <div className="welcome-screen-container">
            <div className="welcome-screen-background"></div>
            <div className="content">

                {/*Info Button, Logo and Text on Page*/}
                <BackButton onClick={handleBackClick} />
                <h1>Information</h1>
                <p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.</p>

                {/*Login Button*/}
                <button onClick={navigateToStart}>Starten</button>
            </div>
        </div>
    );
}

export default Tutorial;