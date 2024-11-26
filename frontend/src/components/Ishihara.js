import React, {useState, useEffect} from "react";
import Sidebar from "./Sidebar";
import LogoTop from "./LogoTop";
import {IconMap} from "../data/IconMap";
import "./../App.css";
import {useNavigate} from "react-router-dom";
import ReactMarkdown from "react-markdown";

function Ishihara() {
    const [setIsSidebarExpanded] = useState(false);

    const handleSidebarToggle = (isExpanded) => {
        setIsSidebarExpanded(isExpanded);
    };

    const navigate = useNavigate();

    return (
        <div className="container-fluid p-3 background-all">
            <Sidebar onToggle={handleSidebarToggle}/>
            <LogoTop/>

        </div>
    );
}

export default Ishihara;
