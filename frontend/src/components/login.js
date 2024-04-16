import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

function Login() {

  // Handle Navigation To Hello World Page
  const navigate = useNavigate();
  const navigateToHelloWorld = () => {
    navigate("/hello_world");
  };

  return (
    // Formatting
    <div className="welcome-screen-container">
      <div className="welcome-screen-background"></div>
      <div className="content">

        {/*Input Form*/}
        <h2>Persönliche Daten</h2>
        <form>
          <div style={{ marginBottom: "10px" }}>
            <label htmlFor="firstName" style={{ display: "block" }} />
            <input
              type="text"
              id="firstName"
              name="firstName"
              placeholder="Vorname"
            />
          </div>
          <div style={{ marginBottom: "10px" }}>
            <label htmlFor="lastName" style={{ display: "block" }} />
            <input
              type="text"
              id="lastName"
              name="lastName"
              placeholder="Nachname"
            />
          </div>
          <div style={{ marginBottom: "10px" }}>
            <label htmlFor="email" style={{ display: "block" }} />
            <input
              type="email"
              id="email"
              name="email"
              placeholder="Email"
            />
          </div>

          {/*Submit Button and Skip Button*/}
          <button type="submit" onClick={navigateToHelloWorld}>Weiter</button>
          <button type="submit">Überspringen</button>
        </form>
      </div>
    </div>
  );
}

export default Login;