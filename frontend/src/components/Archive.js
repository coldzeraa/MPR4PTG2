import { useEffect, useState } from "react";
import LogoTop from "./LogoTop";
import Sidebar from "./Sidebar";
import PdfDownload from "./PdfDownload";
import { IconMap } from "../data/IconMap";

function Archive() {
  const patientID = localStorage.getItem("patientID");

  const [patientInfo, setPatientInfo] = useState(null);
  const [examinations, setExaminations] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    if (patientID) {
      fetchPatientInfo();
      fetchExaminations();
    }
  }, [patientID]);

  const fetchPatientInfo = async () => {
    const response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/get_patient_info?patientID=${encodeURIComponent(patientID)}`,
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

  const fetchExaminations = async () => {
    const response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/get_examinations?patientID=${encodeURIComponent(patientID)}`,
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
      console.log("Failed to fetch examinations");
    }
  };

  return (
    <div className="container-fluid p-4 background-all">
      <Sidebar />
      <LogoTop />
      <div className="row d-flex justify-content-center">
        <div className="col-md-8 col-lg-6">
          <div className="text-center mb-4">
            <h4 className="mb-3">Archive</h4>
          </div>

          {patientInfo && (
            <div className="card mb-4 shadow-sm border-0">
              <div className="card-body">
                <h5 className="card-title text-secondary">Patient Information</h5>
                <p className="mb-1"><strong>Name:</strong> {patientInfo.first_name} {patientInfo.last_name}</p>
                <p><strong>Email:</strong> {patientInfo.email}</p>
              </div>
            </div>
          )}

          {isLoading ? (
            <div className="text-center text-secondary">
              <p>Loading examinations...</p>
            </div>
          ) : (
            examinations.length > 0 ? (
              <div className="examination-list">
                {examinations.map((exam, index) => (
                  <div key={index} className="card mb-3 border-0 shadow-sm p-2 rounded-lg">
                    <div className="card-body d-flex justify-content-between align-items-center">
                      <div>
                        <p className="mb-1"><strong>Date:</strong> {new Date(exam.date_time).toLocaleDateString()}</p> {/*TODO add datetime*/}
                        {exam.type === 'P' ? (
                          <p className="mb-0">
                            <i className={`${IconMap.perimetry.icon} mr-2`}></i>
                            {' '}
                            {IconMap.perimetry.label}
                          </p>
                        ) : (
                          <p className="mb-0"> {exam.type}</p>
                        )}
                      </div>
                      
                    </div>
                    <PdfDownload exID={exam.exID} />
                  </div>
                  
            ))}
        </div>
        ) : (
        <div className="text-center text-muted">
          <p>No examination records found.</p>
        </div>
        )
          )}
      </div>
    </div>
    </div >
  );
}

export default Archive;
