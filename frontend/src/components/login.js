import { useNavigate } from "react-router-dom";
import { useState } from 'react';

function Login() {
  // Handle Navigation To Hello World Page
  const navigate = useNavigate();
  const navigateToHelloWorld = () => {
    navigate("/hello_world");
  };

  const [formData, setFormData] = useState({
    firstName: "",
    lastName: "",
    email: "",
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://127.0.0.1:8000/api/login/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Sending failed');
        }
        navigate("/hello_world");
        return response.json();
      })
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

          {/*Submit Button and Skip Button*/}
          <button type="submit" onClick={handleSubmit}>
            Weiter
          </button>
          <button type="submit" onClick={navigateToHelloWorld}>Überspringen</button>
        </form>
      </div>
    </div>
  );
}

export default Login;
