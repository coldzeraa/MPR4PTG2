import { useNavigate } from "react-router-dom";
import { useState } from "react";
import emailIcon from "./../images/emailIcon.png";
import passwordIcon from "./../images/passwordIcon.png";
import LogoTop from "./LogoTop";
import BackButton from "../BackButton";

function Login() {
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
      // Case password is wrong
      case "WRONG_PASSWORD":
        window.alert("Das Passwort ist falsch!");
        return false;
      // Case case no account with that email
      case "NO_PATIENT_FOUND":
        window.alert("Kein Account mit dieser Email registriert!");
        return false;
      // Case invalid request method
      case "INVALID_REQUEST_METHOD":
        return false;
      // Default case return true
      default:
        return true;
    }
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

      if (checkResponse(responseData.message)) {
        localStorage.setItem("patientID", responseData.patientID);
        navigate("/dashboard");
      }
    } catch (error) {
      console.error("Failed to submit form:", error);
    }
  };

  return (
    <div className="container-fluid d-flex flex-column min-vh-100 justify-content-center align-items-center bg-light background-all">
      {/* Logo */}
      <LogoTop />
      <BackButton onClick={navigateToWelcomeScreen} />
      {/* Login Card */}
      <div
        className="card shadow-sm p-4"
        style={{ maxWidth: "400px", width: "100%" }}
      >
        <h2 className="text-center mb-4">Einloggen</h2>

        <form method="POST" onSubmit={handleSubmit}>
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

          {/* Password Field */}
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

          {/* Register Link */}
          <div className="text-center mb-3">
            <small>
              Du hast noch keinen Account?{" "}
              <a href="/registry">Registriere dich hier!</a>
            </small>
          </div>

          {/* Submit Button */}
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

export default Login;
