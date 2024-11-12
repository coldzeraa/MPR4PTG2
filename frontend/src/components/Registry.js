import {useNavigate} from "react-router-dom";
import {useState} from "react";
import nameIcon from "./../images/nameIcon.png";
import emailIcon from "./../images/emailIcon.png";
import passwordIcon from "./../images/passwordIcon.png";
import LogoTop from "./LogoTop";
import BackButton from "../BackButton";

function Registry() {
    // Create navigate
    const navigate = useNavigate();

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
        setFormData({...formData, [e.target.name]: e.target.value});
    };

    // Handle submit button
    const handleSubmit = (e) => {
        // TODO send data to backend!!

        // TODO validate inputs in backend!
        navigate("/login");
    };

    return (
        // Formatting
        <div
            className="container-fluid d-flex flex-column min-vh-100 justify-content-center align-items-center bg-light background-all">
            {/* Logo */}
            <LogoTop/>
            {/*Back Button, Logo and Text on Page*/}
            <BackButton/>

            {/*Registry Card*/}
            <div className="card shadow-sm p-4" style={{maxWidth: '400px', width: '100%'}}>
                {/*Input Form*/}
                <h2 className="text-center mb-4">Registrieren</h2>
                <form method="POST">

                    {/* Vorname Field */}
                    <div className="mb-3">
                        <div className="input-group">
              <span className="input-group-text">
                <img src={nameIcon} alt="Name Icon" style={{width: '20px'}}/>
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
                <img src={nameIcon} alt="Surname Icon" style={{width: '20px'}}/>
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
                <img src={emailIcon} alt="Email Icon" style={{width: '20px'}}/>
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
                <img src={passwordIcon} alt="Password Icon" style={{width: '20px'}}/>
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
                    <div className="text-center mb-3">
                        <small>
                            Du hast schon einen Account? <br/> Melde dich{" "}
                            <a href="/login"> hier</a> an!
                        </small>
                    </div>
                    <div className="d-grid">
                        <button
                            className="button"
                            type="submit"
                            style={{margin: "20px"}}
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
