import React, { useState } from 'react';
import '../App.css';
import {IconMap} from '../data/IconMap';

const MenuItem = ({ icon, label, expanded, link }) => (
    <div
        className="menu-item"
        onClick={() => window.location.href = link}
        role="button"
        tabIndex={0}
    >
        <i className={`${icon} menu-icon`}></i>
        {expanded && <span>{label}</span>}
    </div>
);

export default function Sidebar() {
    const [expanded, setExpanded] = useState(false);

    const toggleSidebar = () => {
        setExpanded(prev => !prev);
    };

    return (
        <div>
            <button onClick={toggleSidebar} className="toggle-button">
                <i className={`fas ${expanded ? 'fa-chevron-right' : 'fa-bars'}`} style={{ fontSize: '24px' }}></i>
            </button>

            <div className={`sidebar ${expanded ? 'expanded' : 'collapsed'}`}>
                {expanded && (
                    <>
                        <h3 className="menu-title">Menü</h3>
                        <div className="menu-items">
                                {Object.entries(IconMap).map(([key, item], index) => (
                                    key !== "contact" &&
                                    <MenuItem
                                        key={index}
                                        icon={item.icon}
                                        label={item.label}
                                        expanded={expanded}
                                        link={item.link}
                                    />
                                ))}
                          
                        </div>
                        <div className="small-links">
                            <a href="info" className="small-link">Über Optimate</a>
                            <a href="contact" className="small-link">Kontakt</a>
                            <a href="/" className="small-link">Ausloggen</a>
                        </div>
                        <div className="flex justify-center items-center">
                            <a
                                className="flex items-center gap-1 text-sm hover:text-blue-700 hover:underline"
                                href="https://github.com/coldzeraa/MPR4PTG2"
                                target="_blank"
                                rel="noopener noreferrer"
                            >
                                Find us on{' '}
                                <img
                                    src={require('../icons/github.svg').default}
                                    alt="GitHub Logo"
                                    width={15}
                                    height={15}
                                />
                            </a>
                        </div>
                    </>
                )}
            </div>
        </div>
    );
}
