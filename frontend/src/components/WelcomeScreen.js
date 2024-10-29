import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { ReactComponent as Logo } from "../icons/eye_logo.svg";
import "./../App.css";

function WelcomeScreen() {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    setIsVisible(true);
  }, []);

  // State to make sure which option was selected
  const [selectedOption, setSelectedOption] = useState("");

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
    navigate("/Info");
  };

  const [error, setError] = useState(null);

  // Handle Navigation To Login Page
  const navigate = useNavigate();
  const navigateToLogin = () => {
    navigate("/login");
  };

  // Handle Navigation To Registry Page
  const navigateToRegistry = () => {
    navigate("/registry");
  };

  // Handle Popup
  const [isOpen, setIsOpen] = useState(false);

  const openPopup = () => {
    setIsOpen(true);
  };

  const closePopup = () => {
    setIsOpen(false);
  };

  // Function to handle change
  const handleOptionChange = (event) => {
    setSelectedOption(event.target.value);
    setError("");
  };

  // Function to handle ok click
  const handleOkClick = () => {
    switch (selectedOption) {
      case "perimetry":
        closePopup();
        navigate("/tutorial");
        break;
      case "redGreen":
        closePopup();
        navigate("/ishihara");
        break;
      default:
        setError("Bitte wählen Sie eine Untersuchung aus.");
    }
  };

  return (
    <div className="container-fluid welcome-screen d-flex align-items-center justify-content-center">
      {/* Info Button on top right corner */}
      <InfoButton
        className="info-button"
        onClick={handleInfoClick}
      ></InfoButton>
      <div className="text-center text-white content">
        {/* Logo and Text on Page */}
        <Logo className={`App-logo ${isVisible ? "visible" : ""}`} />
        <h1>OptiMate</h1>
        <h3>Simply VIEWtiful</h3>

        {/* Button Container */}
        <div className="button-container">
          <button className="button start-button" onClick={navigateToLogin}>
            🔑 Einloggen
          </button>
          <button className="button start-button" onClick={navigateToRegistry}>
            📝 Registrieren
          </button>
          <button className="button start-button" onClick={openPopup}>
            ⏩ Überspringen
          </button>
          {/* Popup is shown if isOpen is true */}
          {isOpen && (
            <div className="popup-overlay">
              <div className="popup-content">
                <h2>Welche Untersuchung wollen Sie starten?</h2>
                <div className="popup-options">
                  <label>
                    <input
                      type="radio"
                      name="perimetry"
                      value="perimetry"
                      checked={selectedOption === "perimetry"}
                      onChange={handleOptionChange}
                    />
                    Gesichtsfeldmessung
                  </label>

                  <label>
                    <input
                      type="radio"
                      name="redGreen"
                      value="redGreen"
                      checked={selectedOption === "redGreen"}
                      onChange={handleOptionChange}
                    />
                    Rot-Grün-Test
                  </label>
                </div>
                {error && <p className="error-message">{error}</p>}
                <button className="popup-button" onClick={handleOkClick}>
                  OK
                </button>
                <button className="popup-button" onClick={closePopup}>
                  Schließen
                </button>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default WelcomeScreen;
