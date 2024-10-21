import { useNavigate, Link } from "react-router-dom";
import "./../App.css";
import LogoTop from "./LogoTop";

function Dashboard() {

  const navigate = useNavigate();

  // Define Back Button
  function BackButton({ onClick }) {
    return (
      <button className="button back-button" onClick={onClick}>
        ← Zurück
      </button>
    );
  }

  // Handle click events
  const handleBackClick = () => {
    navigate("/Login");
  };

  const handlePerimetryClick = () => {
    navigate("/Tutorial");
  }

  const handleRedGreenClick = () => {
    // TODO Change to Real Red Green Blindess Test
    navigate("/Tutorial")
  }

  const handleArchiveClick = () => {
    // TODO Change to Real Archive
    navigate("/Tutorial")
  }


  return (
    <div className="container-fluid p-3 background-all" >
      <LogoTop />
      {/*Back Button, Logo and Text on Page*/}
      <BackButton onClick={handleBackClick} />
      {/* Dashboard content */}
      <div className="row d-flex justify-content-center">
        {/* Section 1: Perimetry */}
        <div className="col-md-3 mb-3">
          <div className="card text-center shadow-sm">
            <div
              className="card text-center shadow-sm text-decoration-none"
              onClick={handlePerimetryClick}
              style={{ cursor: 'pointer' }}
            >
              <div className="card-body">
                <div className="icon mb-3">
                  {/* Placeholder for the icon */}
                  <span role="img" aria-label="icon">
                    👁️
                  </span>
                </div>
                <h5 className="card-title">Gesichtsfeldmessung</h5>
                <p className="card-text">
                  Führen Sie hier die Gesichtsfeldmessung durch. Sie benötigen dafür eine VR-Brille.
                </p>
              </div>
            </div>
          </div>
        </div>

        {/* Section 2: Red-Green-Blindness */}
        <div className="col-md-3 mb-3">
          <div className="card text-center shadow-sm">
            <div
              className="card text-center shadow-sm text-decoration-none"
              onClick={handleRedGreenClick}
              style={{ cursor: 'pointer' }}
            >
              <div className="card-body">
                <div className="icon mb-3">
                  {/* Placeholder for the icon */}
                  <span role="img" aria-label="icon">
                    🩸
                  </span>
                </div>
                <h5 className="card-title">Rot-Grün-Test</h5>
                <p className="card-text">
                  Führen Sie hier den Rot-Grün-Test durch.
                </p>
              </div>
            </div>
          </div>
        </div>

        {/* Section 3: Archive */}
        <div className="col-md-3 mb-3">
          <div className="card text-center shadow-sm">
            <div
              className="card text-center shadow-sm text-decoration-none"
              onClick={handleArchiveClick}
              style={{ cursor: 'pointer' }}
            >
              <div className="card-body">
                <div className="icon mb-3">
                  {/* Placeholder for the icon */}
                  <span role="img" aria-label="icon">
                    📂
                  </span>
                </div>
                <h5 className="card-title">Archiv</h5>
                <p className="card-text">
                  Hier finden Sie vergangene Ergebnisse.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
