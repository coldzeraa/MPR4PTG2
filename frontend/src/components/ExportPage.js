// ExportPage.js
import React, { useState, useEffect } from "react";
import LogoTop from "./LogoTop";
import Sidebar from "./Sidebar";
import PdfDownload, { generatePdfContent } from "./PdfDownload";


function ExportPage() {

  // extract data from localStorage
  const exaID = localStorage.getItem("exID");
  const patID = localStorage.getItem("patientID");
  
  const [patientInfo, setPatientInfo] = useState(null);
  const [skipButton, setSkipButton] = useState(null);
  const [dataAvailable, setDataAvailable] = useState(false);
  const [emailSentSuccessfully, setEmailSent] = useState(false);

  useEffect(()  => {
    fetchPatientInfo(patID);
    const storedValue = localStorage.getItem("skip_button");
    setSkipButton(storedValue);
  }, []); 

  useEffect(() => {
    if (patientInfo) {
      const isAvailable = patientInfo.first_name && patientInfo.last_name && patientInfo.email;
      setDataAvailable(isAvailable);
    }
  }, [patientInfo]);
  
  useEffect(() => {
    if (skipButton === "true") {  
      handleSkipValues(exaID, patID);
      localStorage.clear();
    }
  }, [skipButton]);

  const fetchPatientInfo = async (patID) => {
    if (patID == null) return;
    
    const response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/get_patient_info?patientID=${encodeURIComponent(patID)}`,
      {
        method: "GET",
        headers: { "Content-Type": "application/json" },
      }
    );
    if (response.ok) {
      const json = await response.json();
      setPatientInfo(json);
      
      return json;
    } else {
      console.log("Failed to fetch patient info");
    }
  };

  const handleEmailRequest = async () => {
    // Generate PDF content for email
    const pdfContent = await generatePdfContent(exaID);

    if (!pdfContent) {
      console.error("PDF content generation failed");
      return;
    }

    // Create blob with pdfContent inside it
    const blob = new Blob([pdfContent], { type: "application/pdf" });

    // Convert blob to base64
    const reader = new FileReader();
    reader.readAsDataURL(blob);
    reader.onloadend = async () => {
      const base64data = reader.result.split(",")[1]; // Strip out the base64 header
      const requestBody = {
        firstName: patientInfo.first_name,
        lastName: patientInfo.last_name,
        email: patientInfo.email,
        pdfBase64: base64data,
      };

      try {
        const response = await fetch(
          `${process.env.REACT_APP_API_URL}/api/emailing/`,
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(requestBody),
          }
        );

        if (response.ok) {
          const data = await response.json();
          setEmailSent(true);
          console.log("Email sent successfully:", data);
        } else {
          console.error("Failed to send email:", response.statusText);
        }
      } catch (error) {
        console.error("Error:", error);
      }
    };
  };

  const handleSkipValues = async (exaID, patID) => {
    console.log("In HANDLESKIPVALUES; ExID: ",exaID, "PatID: ", patID);
    try {
      const response = await fetch(
        `${process.env.REACT_APP_API_URL}/api/delete_patient_data/`, 
        {
          method: "DELETE",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ patID }), 
        }
      );
  
      if (!response.ok) {
        throw new Error("Failed to delete patient data");
      }
  
    } catch (error) {
      console.error("Error deleting patient data:", error);
    }
  };

  return (
    <div className="container-fluid p-3 background-all" style={{ height: "100vh" }}>
      <LogoTop />
      <Sidebar />
      <div className="d-flex align-items-center justify-content-center">
        <div className="content">
          <h2>Auswertung abgeschlossen</h2>
          <p>Wie wollen Sie Ihr Ergebnis erhalten?</p>
          <PdfDownload exID={exaID} />
          <button
            className={"" + (dataAvailable ? "button" : "button-disabled")}
            type="submit"
            onClick={handleEmailRequest}
            disabled={!dataAvailable}
          >
            Als E-Mail erhalten
          </button>
          {/* TODO {emailSentSuccessfully ? (<p>Ihre Email wurde versandt!</p>): (<p>Das hat leider nicht funktioniert!</p>)}*/}
          {skipButton === "true" && (
            <div className="content">
              <br></br>
              <div className="alert alert-warning" role="alert">
                <strong>Wichtiger Hinweis!</strong><br></br>Sie haben kein Konto erstellt. Bitte beachten
                Sie, dass keine persönlichen Daten gespeichert werden und Sie nach Verlassen der Seite
                nicht mehr darauf zugreifen können.
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default ExportPage;
