// PdfDownload.js
import React, { useState, useEffect } from "react";

export const generatePdfContent = async (exID) => {
  const response = await fetch(
    `${process.env.REACT_APP_API_URL}/api/get_pdf?id=${encodeURIComponent(
      exID
    )}`,
    {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    }
  );

  if (response.ok) {
    const blob = await response.blob();
    return blob;
  } else {
    console.error("Failed to fetch PDF content");
    throw new Error("Failed to fetch PDF content");
  }
};

async function deletePatient() {
  const patient = {
    patID: localStorage.getItem("patientID"),
  };
    try {
      const response = await fetch(
        `${process.env.REACT_APP_API_URL}/api/delete_patient_data/`,
        {
          method: "DELETE",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(patient),
        }
      );

      if (!response.ok) {
        throw new Error("Deleting PatID Failed");
      }
    } catch (error) {
      console.error("Error deleting Patient from DB: ", error);
    }
  
}

function PdfDownload({ exID }) {
  const [firstDownload, setFirstDownload] = useState(false);
  const [skipButton, setSkipButton] = useState(false);

  useEffect(() => {
    // Sync with localStorage on component mount
    const initialFirstDownload = localStorage.getItem("firstDownload") === "true";
    const initialSkipButton = localStorage.getItem("skip_button") === "true";
    setFirstDownload(initialFirstDownload);
    setSkipButton(initialSkipButton);
  }, []);

  const handlePdfDownload = async () => {
    try {
      const blob = await generatePdfContent(exID);
      const url = window.URL.createObjectURL(new Blob([blob]));
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", "Testergebnis.pdf");
      document.body.appendChild(link);
      link.click();
      link.parentNode.removeChild(link);

      // Update localStorage and state
      localStorage.setItem("firstDownload", true);
      setFirstDownload(true);

      if(skipButton) {
        deletePatient();
      }

    } catch (error) {
      console.error("Error during PDF download:", error);
    }
  };

  return (
    <button
      className={"button " + (firstDownload && skipButton ? "button-disabled" : "")}
      onClick={handlePdfDownload}
      disabled={firstDownload && skipButton} 
    >
      Download
    </button>
  );
}
export default PdfDownload;
