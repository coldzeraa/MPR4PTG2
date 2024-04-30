import { useNavigate } from "react-router-dom";
import { useState } from 'react';

function Login() {
  // Create navigate
  const navigate = useNavigate();

  // Navigate to tutorial
  const navigateToTutorial = () =>{
    navigate("/tutorial")
  };

  // Define Back Button
  function BackButton({ onClick }) {
    return (
        <button className="button back-button" onClick={onClick}>
            ← Back
        </button>
    );
  };

  // Navigate to welcome screen
  const navigateToWelcomeScreen = () => {
    navigate("/");
  };

  // Show alert if just one name was entered
  const showNameError = () => {
    window.alert("Bitte Vor- und Nachname eingeben.");
  };

  // Show alert if email was invalid
  const showEmailError = () => {
    window.alert("Bitte geben Sie eine valide Email ein.");
  };

  // Show alert if enterd name contains numbers or special characters
  const showInvalidNameError = () => {
    window.alert(
      "Vor- und Nachname dürfen keine Zahlen oder Sonderzeichen enthalten!"
    );
  };

  // Show alert if no data was provided and "weiter" button was clicked
  const showNoDataError = () => {
    window.alert("Bitte geben Sie Ihre Daten ein!");
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

  // Funktion to check the response
  const checkResponse = (e) => {
    // Check response of backend
    switch (e) {
      // Case just one name was entered
      case "NOT_BOTH_NAMES":
        showNameError();
        break;
      // Case email was invalid
      case "NOT_AN_EMAIL":
        showEmailError();
        break;
      // Case names contain numbers or special characters
      case "INVALID_NAMES":
        showInvalidNameError();
        break;
      // Default case just navigate to next page
      default:
        navigateToTutorial();
        break;
    }
  };

  // Function to handle sumbission
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (Object.values(formData).every(value => value === "")){
      showNoDataError();
      return;
    }

    try {
      // Fetch data via "POST" to backend
      const response = await fetch("http://127.0.0.1:8000/api/login/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      })
      if (!response.ok) {
        throw new Error("Sending failed");
      }

      // Parse response as JSON
      const responseData = await response.json();

      // Check response
      checkResponse(responseData.message);
    
    } catch (error) {
      console.error("Failed to submit form:", error);
    }
  };

  // Function to handle skip
  const handleSkip = async (e) => {
    e.preventDefault();
    try {
      // Empty formular to send to backend
      const form = {
        firstName: "",
        lastName: "",
        email: "",
      };

      // Fetch data via "POST" to backend
      const response = await fetch("http://127.0.0.1:8000/api/login/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(form),
      });

      // Check if response is okay
      if (!response.ok) {
        throw new Error("Sending failed");
      }

      // Parse response as JSON
      const responseData = await response.json();

      // Check response
      checkResponse(responseData.message);
    } catch (error) {
      console.error("Failed to submit form:", error);
    }
  };


  return (
    // Formatting
    <div className="container-fluid d-flex align-items-center justify-content-center">
      {/*Back Button, Logo and Text on Page*/}
      <BackButton onClick={navigateToWelcomeScreen} />
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


          <button className="button" type="submit" onClick={handleSubmit}>
            Weiter
          </button>
          <button className="button" type="submit" onClick={handleSkip}>
            Überspringen
          </button>
        </form>
      </div>
    </div>
  );
}

export default Login;
