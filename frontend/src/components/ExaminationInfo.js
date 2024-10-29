import React, { useState, useEffect } from "react";
import Sidebar from "./Sidebar";
import LogoTop from "./LogoTop";
import { IconMap } from "../data/IconMap";
import "./../App.css";
import { useNavigate } from "react-router-dom";

const ExaminationTitle = ({ icon, label }) => (
  <span className="title-item-content">
    <i className={`${icon} title-icon`}></i>
    <h3>{label}</h3>
  </span>
);

function ExaminationInfo() {
  const [setIsSidebarExpanded] = useState(false);
  const [infoText, setInfoText] = useState("");
  const [isChecked, setIsChecked] = useState(false);

  const handleSidebarToggle = (isExpanded) => {
    setIsSidebarExpanded(isExpanded);
  };
  const handleCheckboxChange = () => {
    setIsChecked((prevChecked) => !prevChecked);
  };

  const currentUrl = window.location.href;
  const lastSegment = currentUrl
    .substring(currentUrl.lastIndexOf("/") + 1)
    .split("_")[0];
  const { icon, label } = IconMap[lastSegment] || {
    icon: "fas fa-question",
    label: "Unknown",
  };

  useEffect(() => {
    const loadText = async () => {
      try {
        const response = await fetch(`../infotexts/info_${lastSegment}.txt`);
        if (!response.ok) {
          throw new Error("Failed to fetch the text file");
        }
        const text = await response.text();
        setInfoText(text);
      } catch (error) {
        console.error("Error loading the text file:", error);
        setInfoText("Error loading information.");
      }
    };

    loadText();
  }, [lastSegment]);

  const navigate = useNavigate();

  const handleExaminationID = async () => {
    const patient = {
      patID: localStorage.getItem("patientID"),
    };

    try {
      const response = await fetch(
        `${process.env.REACT_APP_API_URL}/api/examination/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(patient),
        }
      );
      const responseData = await response.json();
      localStorage.setItem("exID", responseData.exID);
    } catch (error) {
      console.error("Examination ID failed", error);
    }
  };

  const navigateToPerimetry = () => {
    const element = document.documentElement;
    if (element.requestFullscreen) {
      element.requestFullscreen();
    } else if (element.mozRequestFullScreen) {
      element.mozRequestFullScreen();
    } else if (element.webkitRequestFullscreen) {
      element.webkitRequestFullscreen();
    } else if (element.msRequestFullscreen) {
      element.msRequestFullscreen();
    }

    navigate("/Perimetry");
  };

  return (
    <div className="container-fluid p-3 background-all">
      <Sidebar onToggle={handleSidebarToggle} />
      <LogoTop />

      <div
        style={{
          transition: "margin-left 0.3s ease",
          padding: "20px",
        }}
      >
        <div className="centered-component">
          <ExaminationTitle icon={icon} label={label} />
          <h6>Information</h6>
          <span>{"TODO load text from file here..."}</span>
          <div className="d-flex flex-column align-items-center">
            <label>
              <input
                className="checkbox"
                type="checkbox"
                checked={isChecked}
                onChange={handleCheckboxChange}
              />
              akzeptieren
            </label>
            <button
              className="btn btn-primary mt-2"
              disabled={!isChecked}
              onClick={() => {
                handleExaminationID();
                navigateToPerimetry();
              }}
            >
              ➠ Starten
            </button>
          </div>
          <div></div>
        </div>
      </div>
    </div>
  );
}

export default ExaminationInfo;
