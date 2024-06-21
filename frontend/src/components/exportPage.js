function ExportPage() {
  // Extract data from localStorage
  const FIRST_NAME = localStorage.getItem("firstName");
  const LAST_NAME = localStorage.getItem("lastName");
  const EMAIL = localStorage.getItem("email");

  // Boolean if data has been submitted
  const IS_DATA_AVAILABLE = FIRST_NAME && LAST_NAME && EMAIL;

  const handlePdfDownload = async () => {
    const blob = await generatePdfContent();
    const url = window.URL.createObjectURL(new Blob([blob]));
    const link = document.createElement("a");
    link.href = url;
    link.setAttribute("download", "Testergebnis.pdf");
    document.body.appendChild(link);
    link.click();
    link.parentNode.removeChild(link);
  };

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
      return blob;
    } else {
      console.log("not okay");
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
    const pdfContent = await generatePdfContent();

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
        <button className="button" onClick={generatePdfContent}>
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
