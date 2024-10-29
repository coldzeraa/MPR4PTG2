import React from "react";
import Login from "./components/Login";
import WelcomeScreen from "./components/WelcomeScreen";
import Tutorial from "./components/Tutorial";
import ExportPage from "./components/ExportPage";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Perimetry from "./components/Perimetry";
import Info from "./components/Info";
import Registry from "./components/Registry";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<WelcomeScreen />} />
        <Route path="/login" element={<Login />} />
        <Route path="/tutorial" element={<Tutorial />} />
        <Route path="/perimetry" element={<Perimetry />} />
        <Route path="/export" element={<ExportPage />} />
        <Route path="/info" element={<Info />} />
        <Route path="/registry" element={<Registry />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
