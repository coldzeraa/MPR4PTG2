import "./../App.css";
import Info from "./Info";
import Sidebar from "./Sidebar";
import LogoTop from "./LogoTop";
import React, {useState} from "react";
import {IconMap} from "../data/IconMap";

const Title = ({icon, label}) => (
    <span className="title-item-content">
        <i className={`${icon} title-icon`}></i>
        <h3>{label}</h3>
    </span>
);

function Contact() {
    const {icon, label} = IconMap['contact'];
    const [message, setMessage] = useState("");
    const [subject, setSubject] = useState("");

    const sendMail = () => {
        const email = "optimate.development@gmail.com";
        const subject = encodeURIComponent("BESCHWERDE"); // TODO from file
        const body = encodeURIComponent(message);
        const mailtoLink = `mailto:${email}?subject=[ ISSUE ] ${subject}&body=${body}`;
        window.location.href = mailtoLink;
    };

    // TODO add "[ISSUE] " to subject
    // TODO add subject text area

    return (
        <div className="container-fluid p-3 background-all">
            <div>
                <Sidebar/>
                <LogoTop/>
                <div className="centered-component">
                    <Title icon={icon} label={label}/>
                    <input placeholder="Betreff"></input>
                    <textarea
                        className="wide-input"
                        placeholder="Geben Sie hier Ihre Nachricht ein..."
                        rows="5"
                        value={message}
                        onChange={(e) => setMessage(e.target.value)}
                    />
                    <button
                        className="button start-button"
                        onClick={sendMail}
                    >
                        Send Message
                    </button>
                </div>
            </div>
        </div>
    );
}

export default Contact;
