import { useNavigate } from "react-router-dom";
import { useState } from "react";
import emailIcon from "./../images/emailIcon.png";
import passwordIcon from "./../images/passwordIcon.png";
import bcrypt from "bcryptjs";

function Login() {
  // Create navigate
  const navigate = useNavigate();

  // Navigate to tutorial
  const navigateToTutorial = () => {
    navigate("/tutorial");
  };

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
  };

  // React hook state to define state "formData"
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  // Function to handle change in fomular
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  // Function to check the response
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

  // Function to hash password
  const hashPassword = async () => {
    // Use bcrypt to hash password
    const saltRounds = 10;

    try {
      formData.password = await bcrypt.hash(formData.password, saltRounds);
    } catch (error) {
      console.log("Could not hash password!");
    }
  };

  // Function to handle sumbission
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (Object.values(formData).every((value) => value === "")) {
      showNoDataError();
      return;
    }

    // Hash password
    await hashPassword();

    try {
      // Fetch data via "POST" to backend
      const response = await fetch(
        `${process.env.REACT_APP_API_URL}/api/login/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(formData),
        }
      );

      if (!response.ok) {
        throw new Error("Sending failed");
      }

      // Parse response as JSON
      const responseData = await response.json();
      localStorage.setItem("patientID", responseData.patientID);

      // TODO SESSION

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
        <h2>Einloggen</h2>
        <form method="POST">
          <div className="input-container">
            <div className="icon">
              <img src={emailIcon} alt="Email Icon" />
            </div>
            <input
              type="email"
              id="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              placeholder="Email"
            />
          </div>

          <div class="input-container">
            <div class="icon">
              <img src={passwordIcon} alt="Password Icon" />
            </div>
            <input
              type="password"
              id="password"
              name="password"
              placeholder="Passwort"
              value={formData.password}
              onChange={handleChange}
            />
          </div>
          <div>
            Du hast noch keinen Account? <br /> Registriere dich{" "}
            <a href="/registry"> hier</a>!
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

export default Login;
