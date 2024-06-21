import { useNavigate } from "react-router-dom";
import "./../App.css";
import useVolumeLevel from "./useVolumeLevel";

function Info() {
  // Define Back Button
  function BackButton({ onClick }) {
    return (
      <button className="button back-button" onClick={onClick}>
        ← Zurück
      </button>
    );
  }

  const navigate = useNavigate();

  const handleBackClick = () => {
    // Handle click event for the back button
    navigate("/");
  };

  return (
    // Formatting
    <div className="container-fluid d-flex align-items-center justify-content-center">
      {/*Back Button, Logo and Text on Page*/}
      <BackButton onClick={handleBackClick} />
      <div className="content">
        <h1>Information</h1>
        <div className="scroll-box border rounded p-3 content-left">
          <h6>
            <i>
              <b>Allgemeines</b>
            </i>
          </h6>
          OptiMate ist eine Web-Applikation, die durch Simulation einer
          Gesichtsfeldmessung die Erkennung von Ausfällen des Gesichtsfeldes
          erleichtern soll. Hierfür werden Punkte angezeigt, deren Wahrnehmung
          dann über Spracherkennung mitgeteilt wird. Anschließend erfolgt eine
          Auswertung der Messung, die sowohl lokal als auch per Email exportiert
          werden kann. OptiMate wurde im Rahmen eines Studienprojekts des
          Studiengangs Medizin- und Bioinformatik an der FH Oberösterreich,
          Campus Hagenberg entwickelt.
          <h6>
            <i>
              <b>Wichtiger Hinweis</b>
            </i>
          </h6>
          Bitte beachten Sie, dass OptiMate kein zertifiziertes Medizinprodukt
          ist und keinesfalls eine professionelle medizinische Diagnostik oder
          Therapie ersetzt. Konsultieren Sie bei medizinischen Anliegen stets
          einen qualifizierten Facharzt.
        </div>
        {/*Login Button*/}
        <br />
      </div>
    </div>
  );
}

export default Info;
