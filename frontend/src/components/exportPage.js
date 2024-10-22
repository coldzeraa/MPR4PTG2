import React, { useState, useEffect, useRef } from "react";
import { jsPDF } from "jspdf";
import "./../App.css";

function ExportPage() {
  // Extract data from localStorage
  const FIRST_NAME = localStorage.getItem('firstName');
  const LAST_NAME = localStorage.getItem('lastName');
  const EMAIL = localStorage.getItem('email');

  // Boolean if data has been submitted
  const IS_DATA_AVAILABLE = FIRST_NAME && LAST_NAME && EMAIL;

  // State to store points
  const [points, setPoints] = useState([]);

  // Reference to canvas
  const canvasRef = useRef(null);

  // Fetch points from API
  const fetchPoints = async () => {
    try {
      const response = await fetch(`${process.env.REACT_APP_API_URL}/api/get_points/`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (!response.ok) {
        throw new Error("Fetching points failed");
      }

      const data = await response.json();
      const pointArray = data.points.map(point => ({
        x: point.x,
        y: point.y,
      }));
      setPoints(pointArray);
    } catch (error) {
      console.error("Error fetching points:", error);
    }
  };

  // Draw points on canvas
  useEffect(() => {
    const canvas = canvasRef.current;
    const context = canvas.getContext("2d");

    // Clear the canvas
    context.clearRect(0, 0, canvas.width, canvas.height);

    // Draw points
    points.forEach((point) => {
      context.beginPath();
      context.arc(point.x, point.y, 5, 0, 2 * Math.PI);
      context.fillStyle = "red";
      context.fill();
      context.closePath();
    });
  }, [points]);

  useEffect(() => {
    fetchPoints();
  }, []);

  // Function to download PDF with canvas image
  const handlePdfDownload = () => {
    console.log("downloading pdf...\nName: " + FIRST_NAME + ", " + LAST_NAME + "\nemail: " + EMAIL);

    if (IS_DATA_AVAILABLE) {
      const canvas = canvasRef.current;
      const imageData = canvas.toDataURL("image/jpeg");

      const doc = new jsPDF();

      // Add user data
      doc.text(`Name: ${FIRST_NAME} ${LAST_NAME}`, 10, 10);
      doc.text(`Email: ${EMAIL}`, 10, 20);

      // Add canvas image
      doc.addImage(imageData, 'JPEG', 10, 30, 180, 160); // Adjust dimensions as needed

      // Save the PDF
      doc.save("testPDF.pdf");
    }
  };

  // Function to send email with pdf
  const handleEmailRequest = async () => {
    console.log("sending email...\nName: " + FIRST_NAME + ", " + LAST_NAME + "\nemail: " + EMAIL);

    if (IS_DATA_AVAILABLE) {
      const canvas = canvasRef.current;
      const imageData = canvas.toDataURL("image/jpeg");

      const doc = new jsPDF();

      // Add user data
      doc.text(`Name: ${FIRST_NAME} ${LAST_NAME}`, 10, 10);
      doc.text(`Email: ${EMAIL}`, 10, 20);

      // Add canvas image
      doc.addImage(imageData, 'JPEG', 10, 30, 180, 160); // Adjust dimensions as needed

      // Convert PDF to Base64
      const pdfData = doc.output('datauristring').split(',')[1]; // Strip out the base64 header

      const requestBody = {
        firstName: FIRST_NAME,
        lastName: LAST_NAME,
        email: EMAIL,
        pdfBase64: pdfData
      };

      try {
        const response = await fetch(`${process.env.REACT_APP_API_URL}/api/emailing/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(requestBody),
        });

        if (response.ok) {
          const data = await response.json();
          console.log('Email sent successfully:', data);
        } else {
          console.error('Failed to send email:', response.statusText);
        }
      } catch (error) {
        console.error('Error:', error);
      }
    }
  };

  return (
    <div className="container-fluid d-flex align-items-center justify-content-center">
      <div className="content">
        <h2>Auswertung abgeschlossen</h2>
        <p>Wie wollen Sie Ihr Ergebnis erhalten?</p>
        <button className="button" onClick={handlePdfDownload}>PDF Download</button>
        <button className={"" + (IS_DATA_AVAILABLE ? "button" : "button-disabled")} type="submit" onClick={handleEmailRequest} disabled={!IS_DATA_AVAILABLE}>Als E-Mail erhalten</button>
        <canvas
          ref={canvasRef}
          width={800}
          height={600}
          style={{ border: "1px solid black", marginTop: "20px" }}
        />
      </div>
    </div>
  );
}

export default ExportPage;
