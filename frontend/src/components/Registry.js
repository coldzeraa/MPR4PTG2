import { useNavigate } from "react-router-dom";
import { useState } from "react";
import nameIcon from "./../images/nameIcon.png";
import emailIcon from "./../images/emailIcon.png";
import passwordIcon from "./../images/passwordIcon.png";

function Registry() {
  // Create navigate
  const navigate = useNavigate();

  // Define Back Button
  function BackButton({ onClick }) {
    return (
      <button className="button back-button" onClick={onClick}>
        ← Zurück
      </button>
    );
  }

  // Navigate to welcome screen
  const navigateToWelcomeScreen = () => {
    navigate("/");
  };

  // React hook state to define state "formData"
  const [formData, setFormData] = useState({
    firstName: "",
    lastName: "",
    email: "",
    password: "",
  });

  // Function to handle change in fomular
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  // Handle submit button
  const handleSubmit = (e) => {
    // TODO send data to backend!!

    // TODO validate inputs in backend!
    navigate("/login");
  };

  return (
    // Formatting
    <div className="container-fluid d-flex align-items-center justify-content-center">
      {/*Back Button, Logo and Text on Page*/}
      <BackButton onClick={navigateToWelcomeScreen} />
      <div className="content">
        {/*Input Form*/}
        <h2>Registrieren</h2>
        <form method="POST">
          <div className="input-container">
            <div className="icon">
              <img src={nameIcon} alt="Name Icon" />
            </div>
            <input
              type="text"
              id="firstName"
              name="firstName"
              placeholder="Vorname"
              value={formData.firstName}
              onChange={handleChange}
            />
          </div>

          <div className="input-container">
            <div className="icon">
              <img src={nameIcon} alt="Name Icon" />
            </div>
            <input
              type="text"
              id="lastName"
              name="lastName"
              placeholder="Nachname"
              value={formData.lastName}
              onChange={handleChange}
            />
          </div>

          <div className="input-container">
            <div className="icon">
              <img src={emailIcon} alt="Email Icon" />
            </div>
            <input
              type="text"
              id="email"
              name="email"
              placeholder="Email"
              value={formData.email}
              onChange={handleChange}
            />
          </div>

          <div className="input-container">
            <div className="icon">
              <img src={passwordIcon} alt="Email Icon" />
            </div>
            <input
              type="text"
              id="password"
              name="password"
              placeholder="Passwort"
              value={formData.password}
              onChange={handleChange}
            />
          </div>
          <div>
            Du hast schon einen Account? <br /> Melde dich{" "}
            <a href="/login"> hier</a> an!
          </div>
          <button
            className="button"
            type="submit"
            style={{ margin: "20px" }}
            onClick={handleSubmit}
          >
            Weiter
          </button>
        </form>
      </div>
    </div>
  );
}

export default Registry;
