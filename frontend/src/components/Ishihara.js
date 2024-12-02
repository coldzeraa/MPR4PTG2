import React, { useState } from "react";
import { InputText } from 'primereact/inputtext';
import Sidebar from "./Sidebar";
import LogoTop from "./LogoTop";
import { IconMap } from "../data/IconMap";
import "./../App.css";
import { useNavigate } from "react-router-dom";

function Ishihara() {
    const [text, setText] = useState("");
    const [currentImageIndex, setCurrentImageIndex] = useState(0);
    const navigate = useNavigate();

    const picturePath = process.env.PUBLIC_URL + "/ishihara_images";

    const totalImages = 12;

    const handleChange = (e) => setText(e.target.value);

    const nextImage = () => {
        if (currentImageIndex < totalImages - 1) {
            setCurrentImageIndex((prev) => prev + 1);
            setText("");
        } else {
            navigate("/export");
        }
    };

    const prevImage = () => {
        if (currentImageIndex > 0) {
            setCurrentImageIndex((prev) => prev - 1);
        }
        setText("");
    };

    const { icon, label } = IconMap["picture"];

    const PictureTitle = ({ icon, label, num }) => (
        <span className="title-item-content">
            <i className={`${icon} title-icon`}></i>
            <h3>{label} {num}</h3>
        </span>
    );

    return (
        <div className="container-fluid p-3 background-all">
            <Sidebar onToggle={() => {}} />
            <LogoTop />
            <PictureTitle icon={icon} label={label} num={currentImageIndex + 1} />
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
                    {currentImageIndex < totalImages - 1 ? (
                        <button
                            className="btn btn-primary mt-2"
                            onClick={nextImage}
                            disabled={!text}
                        >
                            Weiter
                        </button>
                    ) : (
                        <button
                            className="btn btn-success mt-2"
                            onClick={nextImage}
                            disabled={!text}
                        >
                            Fertig
                        </button>
                    )}
                </div>
            </div>
        </div>
    );
}

export default Ishihara;
