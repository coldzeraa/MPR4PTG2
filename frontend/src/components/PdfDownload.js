import React, { useState, useEffect } from "react";
import html2pdf from "html2pdf.js";

export const generatePdfContent = async (exID) => {
  console.log("IN GENERATE PDF CONTENT ", exID);

  let exType = await getExaminationType(exID);
  let exName = exType === "P" ? "perimetry" : "ishihara";

  console.log("EXTYPE", exType);
  console.log("EXNAME", exName);

  if (exType === "P") {
    const response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/get_${exName}_pdf?id=${encodeURIComponent(exID)}`,
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      }
    );

    if (response.ok) {
      const blob = await response.blob();
      console.log("PDF Blob Retrieved", blob);
      return blob;
    } else {
      console.error("Failed to fetch PDF content");
      throw new Error("Failed to fetch PDF content");
    }
  } else {
    const htmlContent = await fetchHtmlContent(exID);
    console.log("HTML Content Retrieved", htmlContent);
    return htmlContent;
  }
};


async function getExaminationType(exID) {
  console.log("BLLLLLUB", exID);
  const response = await fetch(
    `${process.env.REACT_APP_API_URL}/api/get_examination_type?id=${encodeURIComponent(exID)}`,
    {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    }
  );

  if (response.ok) {
    const data = await response.json();
    console.log("Examination Type:", data.exType);
    return data.exType;
  } else {
    console.error("Failed to fetch examination type");
    throw new Error("Failed to fetch examination type");
  }
}

async function fetchHtmlContent(exID) {
  const response = await fetch(
    `${process.env.REACT_APP_API_URL}/api/get_ishihara_pdf?id=${encodeURIComponent(exID)}`,
    {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    }
  );

  if (response.ok) {
    // Use response.text() to get the HTML content as a string
    const htmlContent = await response.text();
    console.log("Fetched HTML Content:", htmlContent); // Log to check the content
    return htmlContent;
  } else {
    console.error("Failed to fetch HTML content", response.status, response.statusText);
    throw new Error(`Failed to fetch HTML content. Status: ${response.status} ${response.statusText}`);
  }
}



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
  const [htmlContent, setHtmlContent] = useState("");

  useEffect(() => {
    const initialFirstDownload = localStorage.getItem("firstDownload") === "true";
    const initialSkipButton = localStorage.getItem("skip_button") === "true";
    setFirstDownload(initialFirstDownload);
    setSkipButton(initialSkipButton);
  }, []);

  const handlePdfDownload = async () => {
    try {
      const content = await generatePdfContent(exID);
      console.log(content);

      if (typeof content === "string") {
        const element = document.createElement("div");
        element.innerHTML = content;
        console.log(content)
        document.body.appendChild(element);

        const options = {
          filename: "Testergebnis.pdf",
          html2canvas: { scale: 2 },
          jsPDF: { unit: "mm", format: "a4", orientation: "portrait" },
        };

        html2pdf().from(element).set(options).save();

        document.body.removeChild(element);
      } else {
        const url = window.URL.createObjectURL(content);
        const link = document.createElement("a");
        link.href = url;
        link.setAttribute("download", "Testergebnis.pdf");
        document.body.appendChild(link);
        link.click();
        link.parentNode.removeChild(link);
      }

      localStorage.setItem("firstDownload", true);
      setFirstDownload(true);

      if (skipButton) {
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
