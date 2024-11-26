import React from "react";
import Login from "./components/Login";
import WelcomeScreen from "./components/WelcomeScreen";
import Dashboard from "./components/Dashboard";
import ExportPage from "./components/ExportPage";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Perimetry from "./components/Perimetry";
import Info from "./components/Info";
import Registry from "./components/Registry";
import ExaminationInfo from "./components/ExaminationInfo";
import Contact from "./components/Contact";
import Archive from "./components/Archive";
import Ishihara from "./components/Ishihara";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<WelcomeScreen />} />
        <Route path="/login" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/perimetry_info" element={<ExaminationInfo />} />
        <Route path="/perimetry" element={<Perimetry />} />
        <Route path="/export" element={<ExportPage />} />
        <Route path="/info" element={<Info />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/registry" element={<Registry />} />
        <Route path="/ishihara_info" element={<ExaminationInfo />} />
        <Route path="/archive" element={<Archive />} />
        <Route path="/ishihara" element={<Ishihara />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
