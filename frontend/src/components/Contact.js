import "./../App.css";
import Info from "./Info";
import Sidebar from "./Sidebar";
import LogoTop from "./LogoTop";
import React from "react";
import { IconMap } from "../data/IconMap";

const Title = ({ icon, label }) => (
    <span className="title-item-content">
        <i className={`${icon} title-icon`}></i>
        <h3>{label}</h3>
    </span>
);

function Contact() {
    const { icon, label } = IconMap['contact'];

    const sendMail = () => {
        console.log("Email sent!"); // TODO implement e-Mail logic
    };

    return (
        <div className="container-fluid p-3 background-all">
            <div>
                <Sidebar />
                <LogoTop />
                <div className="centered-component">
                    <Title icon={icon} label={label} />
                    <textarea
                        className="wide-input"
                        placeholder="Enter your message here..."
                        rows="7"
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
