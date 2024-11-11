import "./../App.css";
import Info from "./Info";
import Sidebar from "./Sidebar";
import LogoTop from "./LogoTop";
import React, { useState } from "react";
import { IconMap } from "../data/IconMap";

const Title = ({ icon, label }) => (
    <span className="title-item-content">
        <i className={`${icon} title-icon`}></i>
        <h3>{label}</h3>
    </span>
);

function Contact() {
    const { icon, label } = IconMap['contact'] || { icon: "", label: "Kontakt" };
    const [message, setMessage] = useState("");
    const [subject, setSubject] = useState("");

    const sendMail = () => {
        const email = "optimate.development@gmail.com";
        const mailSubject = encodeURIComponent(subject);
        const mailBody = encodeURIComponent(message);
        const mailtoLink = `mailto:${email}?subject=[Issue] ${mailSubject}&body=${mailBody}`;
        window.location.href = mailtoLink;
    };

    return (
        <div className="container-fluid p-3 background-all">
            <Sidebar />
            <LogoTop />
            <div className="contact-box">
                <div className="content-box">
                    <Title icon={icon} label={label} />
                    <input
                        className="input-field"
                        placeholder="Betreff"
                        value={subject}
                        onChange={(e) => setSubject(e.target.value)}
                    />
                    <textarea
                        className="input-field"
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
