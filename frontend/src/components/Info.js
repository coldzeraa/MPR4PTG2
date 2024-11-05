import {useNavigate} from "react-router-dom";
import "./../App.css";
import {IconMap} from "../data/IconMap";
import LogoTop from "../LogoTop";
import React, {useEffect, useState} from "react";
import ReactMarkdown from "react-markdown";
import BackButton from "../BackButton"

const InfoTitle = ({icon, label}) => (
    <span className="title-item-content">
        <i className={`${icon} title-icon`}></i>
        <h3>{label}</h3>
    </span>
);


function Info() {
    const [infoHtml, setInfoHtml] = useState('');
    const {icon, label} = IconMap['info'];
    const infoItem = 'optimate'

    const navigate = useNavigate();

    useEffect(() => {
        const loadText = async () => {
            try {
                const response = await fetch(`/infotexts/info_${infoItem}.md`);
                if (!response.ok) {
                    throw new Error("Failed to fetch the text file");
                }
                const text = await response.text();
                setInfoHtml(text);
            } catch (error) {
                console.error("Error loading the text file:", error);
                setInfoHtml("Error loading information.");
            }
        };

        loadText();
    }, []);

    return (
        <div className="container-fluid p-3 background-all">
            <LogoTop/>
            <BackButton/>
            <div
                style={{
                    transition: 'margin-left 0.3s ease',
                    padding: '20px',
                }}
            >
                <div className="centered-component">
                    <InfoTitle icon={icon} label={label}/>
                    <ReactMarkdown>{infoHtml}</ReactMarkdown>
                    <div className="d-flex flex-column align-items-center">
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Info;
