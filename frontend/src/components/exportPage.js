function ExportPage() {
  // Extract data from localStorage
  const FIRST_NAME = localStorage.getItem("firstName");
  const LAST_NAME = localStorage.getItem("lastName");
  const EMAIL = localStorage.getItem("email");

  // Boolean if data has been submitted
  const IS_DATA_AVAILABLE = FIRST_NAME && LAST_NAME && EMAIL;

  // Function to download PDF
  const generatePdfContent = async () => {
    const exID = localStorage.getItem("exID");

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
      const url = window.URL.createObjectURL(new Blob([blob]));
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", "Testergebnis.pdf");
      document.body.appendChild(link);
      link.click();
      link.parentNode.removeChild(link);
    } else {
      console.log("not okay");
    }
    // Fetch data
    // const userData = `Name: ${FIRST_NAME} ${LAST_NAME}\n Email: ${EMAIL}`;

    // // Generate PDF content
    // return `%PDF-1.5\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n3 0 obj\n<< /Type /Page /Parent 2 0 R /Resources << /Font << /F1 4 0 R >> >> /MediaBox [0 0 612 792] /Contents 5 0 R >>\nendobj\n4 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Times-Roman >>\nendobj\n5 0 obj\n<< /Length 60 >>\nstream\nBT /F1 18 Tf 50 700 Td (${userData}) Tj\nendstream\nendobj\nxref\n0 6\n0000000000 65535 f \n0000000009 00000 n \n0000000074 00000 n \n0000000127 00000 n \n0000000177 00000 n \n0000000231 00000 n \ntrailer\n<< /Size 6 /Root 1 0 R >>\nstartxref\n321\n%%EOF`;
  };

  // Function to download pdf
  const handlePdfDownload = () => {
    console.log(
      "downloading pdf...\nName: " +
        FIRST_NAME +
        ", " +
        LAST_NAME +
        "\nemail: " +
        EMAIL
    );

    if (IS_DATA_AVAILABLE) {
      // Generate Pdf Content
      const pdfContent = generatePdfContent();

      // // Create blob with pdfContent inside it
      // const blob = new Blob([pdfContent], { type: "application/pdf" });

      // // Create URL
      // const url = window.URL.createObjectURL(blob);

      // // Create invisible "a" element
      // const a = document.createElement("a");

      // // Create href for pdf- document
      // a.href = url;

      // // Download
      // a.download = "testPDF.pdf";

      // // Append invisible "a" element
      // document.body.appendChild(a);

      // // Click download
      // a.click();

      // // Remove "a" element
      // window.URL.revokeObjectURL(url);
    }
  };

  // Function to send email
  const handleEmailRequest = async () => {
    console.log(
      "sending email...\nName: " +
        FIRST_NAME +
        ", " +
        LAST_NAME +
        "\nemail: " +
        EMAIL
    );

    // Generate PDF content
    const pdfContent = generatePdfContent();

    // Create blob with pdfContent inside it
    const blob = new Blob([pdfContent], { type: "application/pdf" });

    // Convert blob to base64
    const reader = new FileReader();
    reader.readAsDataURL(blob);
    reader.onloadend = async () => {
      const base64data = reader.result.split(",")[1]; // Strip out the base64 header

      const requestBody = {
        firstName: FIRST_NAME,
        lastName: LAST_NAME,
        email: EMAIL,
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
          console.log("Email sent successfully:", data);
        } else {
          console.error("Failed to send email:", response.statusText);
        }
      } catch (error) {
        console.error("Error:", error);
      }
    };
  };

  return (
    <div className="container-fluid d-flex align-items-center justify-content-center">
      <div className="content">
        <h2>Auswertung abgeschlossen</h2>
        <p>Wie wollen Sie Ihr Ergebnis erhalten?</p>
        <button className="button" onClick={handlePdfDownload}>
          PDF Download
        </button>
        <button
          className={"" + (IS_DATA_AVAILABLE ? "button" : "button-disabled")}
          type="submit"
          onClick={handleEmailRequest}
          disabled={!IS_DATA_AVAILABLE}
        >
          Als E-Mail erhalten
        </button>
      </div>
    </div>
  );
}

export default ExportPage;
