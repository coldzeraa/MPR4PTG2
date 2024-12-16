import { useEffect, useState } from "react";
import LogoTop from "./LogoTop";
import Sidebar from "./Sidebar";
import PdfDownload from "./PdfDownload";
import { IconMap } from "../data/IconMap";

function Archive() {
  // States
  const [patientInfo, setPatientInfo] = useState(null);
  const [examinations, setExaminations] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [filterType, setFilterType] = useState("");
  const [filterDate, setFilterDate] = useState("");
  const [patientID, setPatientID] = useState();
  const [currentPage, setCurrentPage] = useState(1); // Aktuelle Seite
  const examinationsPerPage = 4; // Anzahl der Examinations pro Seite

  // useEffect that gets patientID from localStorage and sets the state
  useEffect(() => {
    const storedPatientID = localStorage.getItem("patientID");
    if (storedPatientID) {
      setPatientID(storedPatientID);
    }
  }, []);

  // useEffect gets triggered if patientID is set
  useEffect(() => {
    if (patientID) {
      fetchPatientInfo();
      fetchExaminations();
    }
  }, [patientID]);

  // Filter all examinations that align with type and date and sort them descending by date
  const filteredExaminations = examinations
    .filter((exam) => {
      const matchesType = filterType ? exam.type === filterType : true;
      const examDate = new Date(exam.date_time).toISOString().split("T")[0];
      const matchesDate = filterDate ? examDate === filterDate : true;
      return matchesType && matchesDate;
    })
    .sort((a, b) => new Date(b.date_time) - new Date(a.date_time));

  // Pagination logic
  const indexOfLastExamination = currentPage * examinationsPerPage;
  const indexOfFirstExamination = indexOfLastExamination - examinationsPerPage;
  const currentExaminations = filteredExaminations.slice(
    indexOfFirstExamination,
    indexOfLastExamination
  );

  // Handle page change
  const nextPage = () => {
    if (
      currentPage < Math.ceil(filteredExaminations.length / examinationsPerPage)
    ) {
      setCurrentPage((prevPage) => prevPage + 1);
    }
  };

  const prevPage = () => {
    if (currentPage > 1) {
      setCurrentPage((prevPage) => prevPage - 1);
    }
  };

  const fetchPatientInfo = async () => {
    const response = await fetch(
      `${
        process.env.REACT_APP_API_URL
      }/api/get_patient_info?patientID=${encodeURIComponent(patientID)}`,
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
      console.error("Failed to fetch patient info");
    }
  };

  const fetchExaminations = async () => {
    const response = await fetch(
      `${
        process.env.REACT_APP_API_URL
      }/api/get_examinations?patientID=${encodeURIComponent(patientID)}`,
      {
        method: "GET",
        headers: { "Content-Type": "application/json" },
      }
    );
    if (response.ok) {
      const json = await response.json();
      setIsLoading(false);
      setExaminations(json.examinations);
      return json;
    } else {
      console.error("Failed to fetch examinations");
    }
  };

  return (
    <div className="container-fluid p-4 background-all">
      <Sidebar />
      <LogoTop />
      <div className="row d-flex justify-content-center">
        <div className="col-md-8 col-lg-6">
          <div className="text-center mb-4">
            {patientInfo ? (
              <h4 className="mb-3">{patientInfo.first_name}'s Archiv</h4>
            ) : (
              <h4 className="mb-3">Lädt...</h4>
            )}
          </div>
          <div className="mb-4 d-flex justify-content-between align-items-center">
            <div>
              <label htmlFor="typeFilter" className="form-label">
                Nach Typ filtern:
              </label>
              <select
                id="typeFilter"
                className="form-select"
                onChange={(e) => setFilterType(e.target.value)}
              >
                <option value="">Alle</option>
                <option value="P">Perimetrie</option>
                <option value="I">Ishihara</option>
              </select>
            </div>
            <div>
              <label htmlFor="dateFilter" className="form-label">
                Nach Datum filtern:
              </label>
              <input
                id="dateFilter"
                type="date"
                className="form-control"
                onChange={(e) => setFilterDate(e.target.value)}
              />
            </div>
          </div>
          {isLoading ? (
            <div className="text-center text-secondary">
              <p>Lädt Ergebnisse...</p>
            </div>
          ) : currentExaminations.length > 0 ? (
            <div className="examination-list">
              {currentExaminations.map((exam, index) => (
                <div
                  key={index}
                  className="card mb-3 border-0 shadow-sm p-2 rounded-lg"
                >
                  <div className="card-body d-flex justify-content-between align-items-center">
                    <div>
                      <p className="mb-1">
                        <strong>Datum:</strong>{" "}
                        {new Date(exam.date_time).toLocaleString("at-AT", {
                          timeZone: "UTC",
                          year: "numeric",
                          month: "2-digit",
                          day: "2-digit",
                          hour: "2-digit",
                          minute: "2-digit",
                          second: "2-digit",
                        })}
                      </p>{" "}
                      {exam.type === "P" ? (
                        <p className="mb-0">
                          <i className={`${IconMap.perimetry.icon} mr-2`}></i>{" "}
                          {IconMap.perimetry.label}
                        </p>
                      ) : (
                        <p className="mb-0">
                          <i className={`${IconMap.ishihara.icon} mr-2`}></i>{" "}
                          {IconMap.ishihara.label}
                        </p>
                      )}
                    </div>
                  </div>
                  <PdfDownload exID={exam.exID} />
                </div>
              ))}
              {/* Pagination Controls */}
              <div className="pagination-controls text-center mt-4">
                <button
                  className="btn btn-primary me-2"
                  onClick={prevPage}
                  disabled={currentPage === 1}
                >
                  Zurück
                </button>
                <button
                  className="btn btn-primary"
                  onClick={nextPage}
                  disabled={
                    currentPage >=
                    Math.ceil(filteredExaminations.length / examinationsPerPage)
                  }
                >
                  Weiter
                </button>
              </div>
            </div>
          ) : (
            <div className="text-center text-muted">
              <p>Keine Ergebnisse gefunden.</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default Archive;
