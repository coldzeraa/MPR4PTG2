import React from "react";
import Login from "./components/Login";
import HelloWorld from "./components/HelloWorld";
import WelcomeScreen from "./components/WelcomeScreen";
import Tutorial from "./components/Tutorial";
import ExportPage from "./components/ExportPage";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Perimetry from "./components/Perimetry";
import Info from "./components/Info";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<WelcomeScreen />} />
        <Route path="/login" element={<Login />} />
        <Route path="/hello_world" element={<HelloWorld />} />
        <Route path="/tutorial" element={<Tutorial />} />
        <Route path="/Perimetry" element={<Perimetry />} />
        <Route path="/export" element={<ExportPage />} />
        <Route path="/Info" element={<Info />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
