import React, { useState } from "react";
import Sidebar from "./Sidebar";
import LogoTop from "./LogoTop";
import "./../App.css";

function ExaminationInfo() {
  const [isSidebarExpanded, setIsSidebarExpanded] = useState(false);

  const handleSidebarToggle = (isExpanded) => {
    setIsSidebarExpanded(isExpanded);
  };

  return (
    <div>
      <Sidebar onToggle={handleSidebarToggle} />
      <div
        style={{
          marginLeft: isSidebarExpanded ? '250px' : '60px',
          transition: 'margin-left 0.3s ease',
          padding: '20px',
        }}
      >
        <LogoTop />
        <div>
          <span>ExaminationInfo works!</span>
        </div>
      </div>
    </div>
  );
}

export default ExaminationInfo;
