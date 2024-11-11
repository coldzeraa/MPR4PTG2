import { useNavigate } from "react-router-dom";
import "./../App.css";
import LogoTop from "./LogoTop";
import BackButton from "../BackButton"

function Info() {

  const navigate = useNavigate();

  return (
    // Formatting
    <div className="container-fluid p-3 background-all">
      <LogoTop />
      {/*Back Button, Logo and Text on Page*/}
      <BackButton />
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
              <br />
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
