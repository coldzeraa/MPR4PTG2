import React from "react";
import Login from "./components/Login";
import WelcomeScreen from "./components/WelcomeScreen";
import Dashboard from "./components/Dashboard";
import Tutorial from "./components/Tutorial";
import ExportPage from "./components/ExportPage";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Perimetry from "./components/Perimetry";
import Info from "./components/Info";
import ExaminationInfo from "./components/ExaminationInfo";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<WelcomeScreen />} />
        <Route path="/login" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/tutorial" element={<ExaminationInfo />} />
        <Route path="/perimetry" element={<Perimetry />} />
        <Route path="/export" element={<ExportPage />} />
        <Route path="/info" element={<ExaminationInfo />} />
        <Route path="/ishihara" element={<ExaminationInfo />} />
      </Routes>
    </BrowserRouter>
  );
}
// TODO:
// <Route path="/info" element={<Info />} />

export default App;
