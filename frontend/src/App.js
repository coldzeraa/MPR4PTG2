import React from "react";
import Login from "./components/login";
import HelloWorld from "./components/HelloWorld";
import WelcomeScreen from "./components/WelcomeScreen";
import Tutorial from "./components/tutorial";
import ExportPage from "./components/exportPage"
import { BrowserRouter, Route, Routes } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<WelcomeScreen/>}/>
        <Route path="/login" element={<Login />} />
        <Route path="/hello_world" element={<HelloWorld />} />
        <Route path="/tutorial" element={<Tutorial />} />
        <Route path="/export" element={<ExportPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
