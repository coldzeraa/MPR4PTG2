import React, {useState, useEffect} from "react";
import {InputText} from 'primereact/inputtext';
import Sidebar from "./Sidebar";
import LogoTop from "./LogoTop";
import {IconMap} from "../data/IconMap";
import "./../App.css";
import {useNavigate} from "react-router-dom";
import ReactMarkdown from "react-markdown";


function Ishihara() {
    const [setIsSidebarExpanded] = useState(false);
    const [text, setText] = useState("");
    const [currentImageIndex, setCurrentImageIndex] = useState(0);

    const navigate = useNavigate();

    const picturePath = "/ishihara_images";
    const totalImages = 12;

    const handleChange = (e) => {
        setText(e.target.value);
    };

    const nextImage = () => {
        if (currentImageIndex < totalImages - 1) {
            setCurrentImageIndex(currentImageIndex + 1);
        }
        setText("");
    };

    const prevImage = () => {
        if (currentImageIndex > 0) {
            setCurrentImageIndex(currentImageIndex - 1);
        }
        setText("");
    };

    const {icon, label} = IconMap['picture'];

    const handleSidebarToggle = (isExpanded) => {
        setIsSidebarExpanded(isExpanded);
    };

    const PictureTitle = ({icon, label, num}) => (
        <span className="title-item-content">
        <i className={`${icon} title-icon`}></i>
        <h3>{label} {num}</h3>
    </span>
    );

    return (
        <div className="container-fluid p-3 background-all">
            <Sidebar onToggle={handleSidebarToggle}/>
            <LogoTop/>
            <PictureTitle icon={icon} label={label} num={currentImageIndex + 1}/>
            <div className="ishihara-container">
                <img
                    className="ishihara-image"
                    src={`${picturePath}/${currentImageIndex + 1}.png`}
                    alt={`Bild ${currentImageIndex + 1} konnte nicht geladen werden`}
                />
                <div className="image-input">
                    <h6>Erkannte Zahl:</h6>
                    <InputText
                        value={text}
                        onChange={handleChange}
                        placeholder="Hier Zahl eingeben"
                    />
                </div>
                <div className="button-container">
                    <button
                        className="btn btn-primary mt-2"
                        onClick={prevImage}
                        disabled={currentImageIndex === 0}
                    >
                        Zurück
                    </button>
                    <button
                        className="btn btn-primary mt-2"
                        onClick={nextImage}
                        disabled={!text || currentImageIndex === totalImages - 1}
                    >
                        Weiter
                    </button>
                </div>
            </div>
        </div>
    );
}

export default Ishihara;
