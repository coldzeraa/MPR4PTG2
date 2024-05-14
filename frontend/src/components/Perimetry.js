import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './../App.css';
import useVolumeLevel from './useVolumeLevel';

// Point component to render individual points
const Point = ({ x, y }) => (
    <div style={{ position: 'absolute', left: `${x}%`, top: `${y}%` }}>
        <p style={{ margin: 0, fontSize: '10px' }}>⚫</p>
    </div>
);


function Perimetry() {
    const [startRecording, stopRecording, volume, max] = useVolumeLevel();



    const navigate = useNavigate();
    const navigateToExport = () => {
        // Handle Navigation To Export Page
        navigate("/export"); 
    };

    // States 
    const [points, setPoints] = useState([]);
    const [currentPointIndex, setCurrentPointIndex] = useState(0);
    const [showPoint, setShowPoint] = useState(false);
    const [side, setSide] = useState('left');

    // Get Points from Backend
    useEffect(() => {
        const fetchPoints = async () => {
            // TODO REPLACE WITH ACTUAL BACKEND DATA
            const fetchedPoints = [
                { x: 10, y: 10 },
                { x: 20, y: 20 },
                { x: 30, y: 30 },
                { x: 40, y: 40 },
                { x: 50, y: 50 },
                { x: 60, y: 60 },
                { x: 70, y: 70 },
                { x: 80, y: 80 },
                { x: 90, y: 90 }, 
            ];
            setPoints(fetchedPoints);
        };

        fetchPoints();
    }, []);


    useEffect(() => {
        const interval = setInterval(() => {
            setShowPoint(true);
            setTimeout(() => {
                setShowPoint(false);
                startRecording()
                setCurrentPointIndex(prevIndex => (prevIndex + 1) % points.length);
                if (currentPointIndex === points.length - 1 && side === 'left') {
                    setCurrentPointIndex(0);
                    setSide('right');
                } else if (currentPointIndex === points.length - 1 && side === 'right') {
                    navigateToExport();                    
                }
            }, 300); // 200 
        }, 2000); // 1200
        console.log(max)

        if(max >= 15) {
            console.log("seen")
        }
        stopRecording()
        return () => clearInterval(interval);
    }, [points, currentPointIndex, side]);


    return (
        <div className="split-container">
            <div className="split-left">
                {/* Render the current point */}
                {points.length > 0 && side === 'left' && showPoint && (
                    <Point key={currentPointIndex} x={(points[currentPointIndex].x * 0.5) % 50} y={points[currentPointIndex].y} />
                )}
            </div>
            <div className="split-midpoint">
                <p style={{ fontSize: '20px', fontWeight: 'bold' }}>+</p>
            </div>
            <div className="split-right">
                {/* Render the current point */}
                {points.length > 0 && side === 'right' && showPoint && (
                    <Point key={currentPointIndex} x={50 + (points[currentPointIndex].x * 0.5) % 50} y={points[currentPointIndex].y} />
                )}
            </div>
        </div>
    );
}

export default Perimetry;