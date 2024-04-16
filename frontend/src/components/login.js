import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

function Login(){
 
  const navigate = useNavigate();

    const navigate_to_hello_world = () => {
     navigate("/hello_world");
    };

    return (
        <div style={{ display: "flex", justifyContent: "center", alignItems: "center", height: "100vh" }}>
          <div>
            <h2>Persönliche Daten</h2>
            <form>
              <div style={{ marginBottom: "10px" }}>
                <label htmlFor="firstName" style={{ display: "block" }}/>
                <input
                  type="text"
                  id="firstName"
                  name="firstName"
                  placeholder="Vorname"
                />
              </div>
              <div style={{ marginBottom: "10px" }}>
                <label htmlFor="lastName" style={{ display: "block" }}/>
                <input
                  type="text"
                  id="lastName"
                  name="lastName"
                  placeholder="Nachname"
                />
              </div>
              <div style={{ marginBottom: "10px" }}>
                <label htmlFor="email" style={{ display: "block" }}/>
                <input
                  type="email"
                  id="email"
                  name="email"
                  placeholder="Email"
                />
              </div>
              <button type="submit" onClick={navigate_to_hello_world}>Weiter</button>
              <button type="submit">Überspringen</button>
            </form>
          </div>
        </div>
      );
      

}

export default Login;