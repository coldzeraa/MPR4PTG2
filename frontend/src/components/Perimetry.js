import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './../App.css';

const Point = ({ x, y }) => {
    const adjustedX = x * 1.32; // 2/3 of the entire screen width
    return (
        <div style={{ position: 'absolute', left: `${adjustedX}%`, top: `${y}%` }}>
            <p style={{ margin: 0, fontSize: '10px' }}>⚫</p>
        </div>
    );
};

function Perimetry() {
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
                setCurrentPointIndex(prevIndex => (prevIndex + 1) % points.length);
                if (currentPointIndex === points.length - 1 && side === 'left') {
                    setCurrentPointIndex(0);
                    setSide('right');
                } else if (currentPointIndex === points.length - 1 && side === 'right') {
                    navigateToExport();                    
                }
            }, 50); // 200 
        }, 100); // 1200

        return () => clearInterval(interval);
    }, [points, currentPointIndex, side]);


    return (
        <div className="split-container">
            <div className={side === 'left' ? "split-focus" : "split-unfocus"}>
                {/* Render the current point */}
                {points.length > 0 && side === 'left' && showPoint && (
                    <Point key={currentPointIndex} x={(points[currentPointIndex].x * 0.5)} y={points[currentPointIndex].y} />
                )}
            </div>
            <div className="split-midpoint" style={{ left: side === 'left' ? 'calc(33%)' : 'calc(66%)' }}>
                <p style={{ fontSize: '20px', fontWeight: 'bold', color: 'green' }}>+</p>
            </div>
            <div className={side === 'right' ? "split-focus" : "split-unfocus"}>
                {/* Render the current point */}
                {points.length > 0 && side === 'right' && showPoint && (
                    <Point key={currentPointIndex} x={25 + (points[currentPointIndex].x * 0.5)} y={points[currentPointIndex].y} />
                )}
            </div>
        </div>
    );
}

export default Perimetry;
