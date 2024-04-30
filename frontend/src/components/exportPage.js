
function ExportPage() {

  const handlePdfDownload = () => {};

  const handleEmailRequest = () => {};

  return (
    <div className="container-fluid d-flex align-items-center justify-content-center">
      <div className="content">
        <h2>Auswertung abgeschlossen</h2>
        <p>Wie wollen Sie Ihr Ergebnis erhalten?</p>
        <button className="button" type="submit"  onClick={handlePdfDownload}>PDF Download</button>
        <button className="button" type="submit"  onClick={handleEmailRequest}>Als E-Mail erhalten</button>
      </div>
    </div>
  );
}

export default ExportPage;
