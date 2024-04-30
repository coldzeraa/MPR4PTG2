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
        <div className="container-fluid welcome-screen d-flex align-items-center justify-content-center">
            {/* Info Button on top right corner */}
            <InfoButton className="info-button" onClick={handleInfoClick}>
            </InfoButton>
            <div className="text-center text-white content">
                {/* Logo and Text on Page */}
                <Logo className="App-logo" />
                <h1>OptiMate</h1>
                <h3>Simply VIEWtiful</h3>

                {/* Login Button */}
                <button className="button start-button" onClick={navigateToLogin}>
                    ➠ Starten
                </button>
            </div>
        </div>

    );
}

export default WelcomeScreen;