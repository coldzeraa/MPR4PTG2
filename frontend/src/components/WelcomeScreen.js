import { useNavigate } from 'react-router-dom';
import { ReactComponent as Logo } from './../logo.svg';
import './../App.css';

function WelcomeScreen() {

    // Define Info Button on the right top corner
    function InfoButton({ onClick }) {
        return (
            <button className="info-button" onClick={onClick}>
                ℹ️
            </button>
        );
    }

    const handleInfoClick = () => {
        // Handle click event for the info button
        window.alert('Info Button Clicked!');
    };

    // Handle Navigation To Login Page
    const navigate = useNavigate();
    const navigateToLogin = () => {
        navigate("/login");
    };

    return (
        // Formatting
        <div className="welcome-screen-container">
            <div className="welcome-screen-background"></div>
            <div className="content">

                {/*Info Button, Logo and Text on Page*/}
                <InfoButton onClick={handleInfoClick} />
                <Logo className="App-logo" />
                <h1>OptiMate</h1>
                <h3>Simply VIEWtiful</h3>

                {/*Login Button*/}
                <button onClick={navigateToLogin}>Starten</button>
            </div>
        </div>
    );
}

export default WelcomeScreen;