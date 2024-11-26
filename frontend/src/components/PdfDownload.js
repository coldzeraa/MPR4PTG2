import React from "react";

// Function to handle PDF download
const handlePdfDownload = async (exID) => {
  const blob = await generatePdfContent(exID);
  const url = window.URL.createObjectURL(new Blob([blob]));
  const link = document.createElement("a");
  link.href = url;
  link.setAttribute("download", "Testergebnis.pdf"); // TODO rename and save each picture again
  document.body.appendChild(link);
  link.click();
  link.parentNode.removeChild(link);
};

// Function to fetch PDF content
const generatePdfContent = async (exID) => {
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

function PdfDownload({ exID, onDownload }) {
  return (
    <button className="button" onClick={() => onDownload(exID)}>
      Download
    </button>
  );
}

export { generatePdfContent }; // Export the function for external use
export default PdfDownload;
