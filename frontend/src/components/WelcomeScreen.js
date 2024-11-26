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
    localStorage.clear();
    navigate("/login");
  };

  // Handle Navigation To Registry Page
  const navigateToRegistry = () => {
    localStorage.clear();
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
  const handleOkClick = async () => {
    // TODO send empty form to backend to create a dummy patient!!!!
    localStorage.clear();
    console.log(localStorage.getItem("firstName"), localStorage.getItem("lastName"), localStorage.getItem("patientID"), localStorage.getItem("exID"));

    try {
      const response = await fetch(
        `${process.env.REACT_APP_API_URL}/api/create_dummy_patient/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          // Send empty object to backend
          body: JSON.stringify({}),
        }
      );
      if (!response.ok) {
        throw new Error("Failed to create dummy patient");
      }

      const dummyResponseData = await response.json();
      localStorage.setItem("patientID", dummyResponseData.patientID);

      console.log(localStorage.getItem("firstName"), localStorage.getItem("lastName"), localStorage.getItem("patientID"), localStorage.getItem("exID"));


      switch (selectedOption) {
        case "perimetry":
          localStorage.setItem("skip_button", dummyResponseData.skip_button);
          localStorage.setItem("skip_button", "true"); 
          navigate("/perimetry_info");
          break;
        case "redGreen":
          localStorage.setItem("skip_button", dummyResponseData.skip_button);
          localStorage.setItem("skip_button", "true"); 
          navigate("/ishihara_info");
          break;
        default:
          setError("Bitte wählen Sie eine Untersuchung aus.");
      }
    } catch (error) {
      console.error("Error handling skip: ", error);
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
