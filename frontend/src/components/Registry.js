import { useNavigate } from "react-router-dom";
import { useState } from "react";
import nameIcon from "./../images/nameIcon.png";
import emailIcon from "./../images/emailIcon.png";
import passwordIcon from "./../images/passwordIcon.png";
import LogoTop from "./LogoTop";

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

  const isFormFilled = () => {
    return Object.values(formData).every((value) => value.trim() !== "");
  };

  // Function to handle change in fomular
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  // Function to hash password
  const hashPassword = async () => {
    // Create SHA-256 hash
    const encoder = new TextEncoder();
    const data = encoder.encode(formData.password);
    const sha256Hash = await crypto.subtle.digest("SHA-256", data);

    // Transform SHA-256 hash to a hexadecimal format
    const hashArray = Array.from(new Uint8Array(sha256Hash));
    const hexHash = hashArray
      .map((b) => b.toString(16).padStart(2, "0"))
      .join("");

    formData.password = hexHash;
  };

  // Function to check response from backend
  const checkResponse = (e) => {
    switch (e) {
      case "NOT_AN_EMAIL":
        window.alert("Bitte geben Sie eine valide Email ein.");
        return false;
      case "PATIENT_ALREADY_EXISTS":
        window.alert("Es existiert bereits ein Account mit dieser Email");
        return false;
      case "INVALID_NAMES":
        window.alert(
          "Vor- und Nachname dürfen keine Zahlen oder Sonderzeichen enthalten!"
        );
        return false;
      default:
        return true;
    }
  };

  // Handle submit button
  const handleSubmit = async (e) => {
    e.preventDefault();

    // Check if all data has been entered
    if (!isFormFilled()) {
      window.alert("Bitte geben Sie Ihre Daten ein!");
      return;
    }

    // Hash password
    await hashPassword();

    try {
      // Fetch data via "POST" to backend
      const response = await fetch(
        `${process.env.REACT_APP_API_URL}/api/registry/`,
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

      // Check response
      if (checkResponse(responseData.message)) {
        localStorage.setItem("patientID", responseData.patientID);
        navigate("/login");
      }
    } catch (error) {
      console.error("Failed to submit form:", error);
    }
  };

  return (
    // Formatting
    <div className="container-fluid d-flex flex-column min-vh-100 justify-content-center align-items-center bg-light background-all">
      {/* Logo */}
      <LogoTop />
      {/*Back Button, Logo and Text on Page*/}
      <BackButton onClick={navigateToWelcomeScreen} />

      {/*Registry Card*/}
      <div
        className="card shadow-sm p-4"
        style={{ maxWidth: "400px", width: "100%" }}
      >
        {/*Input Form*/}
        <h2 className="text-center mb-4">Registrieren</h2>
        <form method="POST">
          {/* Vorname Field */}
          <div className="mb-3">
            <div className="input-group">
              <span className="input-group-text">
                <img src={nameIcon} alt="Name Icon" style={{ width: "20px" }} />
              </span>
              <input
                type="text"
                id="firstName"
                name="firstName"
                value={formData.firstName}
                onChange={handleChange}
                className="form-control"
                placeholder="Vorname"
                required
              />
            </div>
          </div>

          {/* Nachname Field */}
          <div className="mb-3">
            <div className="input-group">
              <span className="input-group-text">
                <img
                  src={nameIcon}
                  alt="Surname Icon"
                  style={{ width: "20px" }}
                />
              </span>
              <input
                type="text"
                id="lastName"
                name="lastName"
                value={formData.lastName}
                onChange={handleChange}
                className="form-control"
                placeholder="Nachname"
                required
              />
            </div>
          </div>

          {/* Email Field */}
          <div className="mb-3">
            <div className="input-group">
              <span className="input-group-text">
                <img
                  src={emailIcon}
                  alt="Email Icon"
                  style={{ width: "20px" }}
                />
              </span>
              <input
                type="email"
                id="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                className="form-control"
                placeholder="Email"
                required
              />
            </div>
          </div>

          {/* Passwort Field */}
          <div className="mb-3">
            <div className="input-group">
              <span className="input-group-text">
                <img
                  src={passwordIcon}
                  alt="Password Icon"
                  style={{ width: "20px" }}
                />
              </span>
              <input
                type="password"
                id="password"
                name="password"
                value={formData.password}
                onChange={handleChange}
                className="form-control"
                placeholder="Passwort"
                required
              />
            </div>
          </div>
          <div>
            <small>
              Du hast schon einen Account? <br /> Melde dich{" "}
              <a href="/login"> hier</a> an!
            </small>
          </div>
          <div className="d-grid">
            <button
              className="button"
              type="submit"
              style={{ margin: "20px" }}
              onClick={handleSubmit}
            >
              Weiter
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Registry;
