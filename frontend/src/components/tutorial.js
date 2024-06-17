import { useNavigate } from "react-router-dom";
import "./../App.css";
import useVolumeLevel from "./useVolumeLevel";

function Tutorial() {
  const [startRecording] = useVolumeLevel();

  // Define Back Button
  function BackButton({ onClick }) {
    return (
      <button className="button back-button" onClick={onClick}>
        ← Zurück
      </button>
    );
  }


    const navigate = useNavigate();

    const handleExaminationID = async () => {
        const patient = {
            patID: localStorage.getItem("patientID")
        };

        try {
            const response = await fetch(`http://localhost:8000/api/examination/`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(patient)
                }
            );
            const responseData = await response.json();
            localStorage.setItem("exID", responseData.exID);
        }
        catch (error) {
            console.error("Examination ID failed", error);
        }
    }
    
    const navigateToPerimetry = () => {
        startRecording()

        // Request fullscreen
        const element = document.documentElement;
        if (element.requestFullscreen) {
            element.requestFullscreen();
        } else if (element.mozRequestFullScreen) { /* Firefox */
            element.mozRequestFullScreen();
        } else if (element.webkitRequestFullscreen) { /* Chrome, Safari and Opera */
            element.webkitRequestFullscreen();
        } else if (element.msRequestFullscreen) { /* IE/Edge */
            element.msRequestFullscreen();
        }

    // Handle Navigation To Start Page of Test
    // Request fullscreen
    const element = document.documentElement;
    if (element.requestFullscreen) {
      element.requestFullscreen();
    } else if (element.mozRequestFullScreen) {
      /* Firefox */
      element.mozRequestFullScreen();
    } else if (element.webkitRequestFullscreen) {
      /* Chrome, Safari and Opera */
      element.webkitRequestFullscreen();
    } else if (element.msRequestFullscreen) {
      /* IE/Edge */
      element.msRequestFullscreen();
    }

    // Navigate to the Perimetry page
    navigate("/Perimetry");
  };

  const handleBackClick = () => {
    // Handle click event for the back button
    navigate("/login");
  };

  return (
    // Formatting
    <div className="container-fluid d-flex align-items-center justify-content-center">
      {/*Back Button, Logo and Text on Page*/}
      <BackButton onClick={handleBackClick} />
      <div className="content">
        <h1>Information</h1>
        <div className="scroll-box border rounded p-3 content-left">
          Beachten Sie bitte folgende Hinweise, um OptiMate optimal nutzen zu
          können:
          <br />
          <br />
          <ol>
            <li>
              <b>Wählen Sie eine ruhige Umgebung für die Untersuchung.</b>
              <br />
              Vermeiden Sie Störgeräusche, um das Ergebnis nicht zu verfälschen.
            </li>
            <br />
            <li>
              <b>Starten Sie erst, wenn Sie bereit sind.</b>
              <br />
              Durch den Druck auf "Start" wird ein Countdown gestartet, der
              Ihnen 15 Sekunden Zeit gibt, um Ihr Mobiltelefon in die
              VR-Vorrichtung einzusetzen.
            </li>
            <br />
            <li>
              <b>Handeln Sie in Ihrem eigenen Interesse.</b>
              <br />
              Um ein möglichst aussagekräftiges Ergebnis zu erhalten, sollten
              Sie nur dann angeben, einen Punkt gesehen zu haben, wenn Sie ihn
              tatsächlich wahrgenommen haben.
            </li>
          </ol>

        </div>
        {/*Login Button*/}
        <br />
        <button className="button" onClick={navigateToPerimetry}>
          ➠ Starten
        </button>
      </div>
    </div>
  );
}

export default Tutorial;
