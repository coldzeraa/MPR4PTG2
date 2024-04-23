import { useNavigate } from "react-router-dom";
import { useState } from "react";

function Login() {
  // Handle Navigation To Hello World Page
  const navigate = useNavigate();

  // Navigate to tutorial
  const navigateToTutorial = () => {
    navigate("/tutorial");
  };

  // Navigate to welcome screen
  const navigateToWelcomeScreen = () => {
    navigate("/");
  };

  const showNameError = () => {
    window.alert("Bitte Vor- und Nachname eingeben.");
  };

  const showEmailError = () => {
    window.alert("Bitte geben Sie eine valide Email ein.");
  };

  const showInvalidNameError = () => {
    window.alert("Vor- und Nachname dürfen keine Zahlen enthalten!")
  }

  // React hook state to define state "formData"
  const [formData, setFormData] = useState({
    firstName: "",
    lastName: "",
    email: "",
  });

  // Function to handle change in fomular
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  // Function to handle sumbission
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Fetch data via "POST" to backend
      const response = await fetch("http://127.0.0.1:8000/api/login/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error("Sending failed");
      }

      // Parse response as JSON
      const responseData = await response.json();

      // Check response data for "NOT_BOTH_NAMES"
      switch (responseData) {
        case "NOT_BOTH_NAMES":
          showNameError();
          break;
        case "NOT_AN_EMAIL":
          showEmailError();
          break;
        // TODO
        case "INVALID_NAMES":
          showInvalidNameError();
          break;
        default:
          navigateToTutorial();
          break;
      }
    } catch (error) {
      console.error("Failed to submit form:", error);
    }
  };

  return (
    // Formatting
    <div className="welcome-screen-container">
      <div className="welcome-screen-background"></div>
      <div className="content">
        {/*Input Form*/}
        <h2>Persönliche Daten</h2>
        <form method="POST">
          <div style={{ marginBottom: "10px" }}>
            <label htmlFor="firstName" style={{ display: "block" }} />
            <input
              type="text"
              id="firstName"
              name="firstName"
              placeholder="Vorname"
              value={formData.firstName}
              onChange={handleChange}
            />
          </div>
          <div style={{ marginBottom: "10px" }}>
            <label htmlFor="lastName" style={{ display: "block" }} />
            <input
              type="text"
              id="lastName"
              name="lastName"
              placeholder="Nachname"
              value={formData.lastName}
              onChange={handleChange}
            />
          </div>
          <div style={{ marginBottom: "10px" }}>
            <label htmlFor="email" style={{ display: "block" }} />
            <input
              type="email"
              id="email"
              name="email"
              placeholder="Email"
              value={formData.email}
              onChange={handleChange}
            />
          </div>

          {/*Weiter Button, Überspringen Button and Zurück Button */}
          <button
            onClick={navigateToWelcomeScreen}
            style={{ position: "absolute", top: "10px", left: "10px" }}
          >
            Zurück
          </button>
          <button type="submit" onClick={handleSubmit}>
            Weiter
          </button>
          <button type="submit" onClick={navigateToTutorial}>
            Überspringen
          </button>
        </form>
      </div>
    </div>
  );
}

export default Login;
