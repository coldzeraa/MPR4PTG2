import { useNavigate } from "react-router-dom";
import { useState } from 'react';

function Login() {
  // Handle Navigation To Hello World Page
  const navigate = useNavigate();

  // Navigate to tutorial
  const navigateToTutorial = () =>{
    navigate("/tutorial")
  }

  // Navigate to welcome screen
  const navigateToWelcomeScreen = () =>{
    navigate("/")
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
      await fetch("http://127.0.0.1:8000/api/login/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      })
      // Get response
      .then(response => {
        if (!response.ok) {
          throw new Error('Sending failed');
        }
        // If response is okay navigate to tutorial
        navigateToTutorial();
        return response.json();
      })
      // Print response on console
      .then(data => {
        console.log(data.message);
      });
    
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
          <button onClick={navigateToWelcomeScreen} style={{ position: 'absolute', top: '10px', left: '10px' }}>
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
