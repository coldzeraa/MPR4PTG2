import { useState, useEffect } from 'react';
import { ReactComponent as Logo } from './../logo.svg';
import './../App.css';

function Perimetry() {
    // State to store the array of points
    const [points, setPoints] = useState([]);

    // Get Points from Backend
    useEffect(() => {
        const fetchPoints = async () => {
            // REPLACE WITH ACTUAL BACKEND DATA
            const fetchedPoints = [
                { x: 100, y: 200 },
                { x: 300, y: 400 },
                
            ];
            setPoints(fetchedPoints);
        };

        fetchPoints();
    }, []);

    return (
        <div className="split-container">
            <div className="split-left">
                <p>+</p>
                {/* Map through the points array and render a point component for each point */}
                {points.map((point, index) => (
                    <Point key={index} x={point.x} y={point.y} />
                ))}
            </div>
            <div className="split-midpoint"></div>
            <div className="split-right">
            <p>+</p>
                {/* You can render points on the right side as well if needed */}
            </div>
        </div>
    );
}

// Point component to render individual points
const Point = ({ x, y }) => (
    <div style={{ position: 'absolute', top: y, left: x }}>
        <p>?</p>
    </div>
);

export default Perimetry;
