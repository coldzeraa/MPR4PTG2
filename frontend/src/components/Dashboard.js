import { useNavigate } from "react-router-dom";
import "./../App.css";
import LogoTop from "./LogoTop";
import Sidebar from "./Sidebar";

function Dashboard() {
  const navigate = useNavigate();

  const handlePerimetryClick = () => {
    navigate("/perimetry_info");
  };

  const handleRedGreenClick = () => {
    navigate("/ishihara_info");
  };

  const handleArchiveClick = () => {
    navigate("/archive");
  };

  return (
    <div className="container-fluid p-3 background-all">
      <Sidebar />
      <LogoTop />
      {/* Dashboard content */}
      <div className="row d-flex justify-content-center">
        {/* Section 1: Perimetry */}
        <div className="col-md-3 mb-3">
          <div className="card text-center shadow-sm">
            <div
              className="card text-center shadow-sm text-decoration-none custom-card"
              onClick={handlePerimetryClick}
              style={{ cursor: "pointer" }}
            >
              <div className="card-body">
                <div className="icon mb-3 custom-icon-field">
                  {/* Placeholder for the icon */}
                  <span role="img" aria-label="icon">
                    👁️
                  </span>
                </div>
                <h5 className="card-title">Gesichtsfeldmessung</h5>
                <p className="card-text">
                  Führen Sie hier die Gesichtsfeldmessung durch. Sie benötigen
                  dafür eine VR-Brille.
                </p>
              </div>
            </div>
          </div>
        </div>

        {/* Section 2: Red-Green-Blindness */}
        <div className="col-md-3 mb-3">
          <div className="card text-center shadow-sm">
            <div
              className="card text-center shadow-sm text-decoration-none custom-card"
              onClick={handleRedGreenClick}
              style={{ cursor: "pointer" }}
            >
              <div className="card-body">
                <div className="icon mb-3 custom-icon-field">
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
              className="card text-center shadow-sm text-decoration-none custom-card"
              onClick={handleArchiveClick}
              style={{ cursor: "pointer" }}
            >
              <div className="card-body">
                <div className="icon mb-3 custom-icon-field">
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
}

export default Dashboard;
