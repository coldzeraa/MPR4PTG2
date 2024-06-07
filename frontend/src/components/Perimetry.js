import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./../App.css";
import useVolumeLevel from "./useVolumeLevel";

const Point = ({ x, y }) => {
  const adjustedX = x * 1.32; // 2/3 of the entire screen width
  return (
    <div style={{ position: "absolute", left: `${adjustedX}%`, top: `${y}%` }}>
      <p style={{ margin: 0, fontSize: "10px" }}>⚫</p>
    </div>
  );
};

function Perimetry() {
  const [startRecording, stopRecording, volume, max] = useVolumeLevel();

  const navigate = useNavigate();

  const navigateToExport = () => {
    if (
      document.fullscreenElement ||
      document.webkitFullscreenElement ||
      document.mozFullScreenElement ||
      document.msFullscreenElement
    ) {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      } else if (document.webkitExitFullscreen) {
        document.webkitExitFullscreen();
      } else if (document.mozCancelFullScreen) {
        document.mozCancelFullScreen();
      } else if (document.msExitFullscreen) {
        document.msExitFullscreen();
      }
    }
    // Handle Navigation To Export Page
    navigate("/export");
  };

  // States
  const [points, setPoints] = useState([]);
  const [currentPointIndex, setCurrentPointIndex] = useState(0);
  const [showPoint, setShowPoint] = useState(false);
  const [side, setSide] = useState("left");

  // Get Points from Backend
  useEffect(() => {
    // Get points from backend
    const fetchPoints = async () => {
      const response = await fetch(
        `${process.env.REACT_APP_API_URL}/api/get_points/`,
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      if (!response.ok) {
        throw new Error("Sending failed (Points)");
      }

      // Convert to JSON
      const data = await response.json();

      // Get point array
      const pointArray = data.points;

      // Formatted array
      const fetchedPoints = [];

      // Insert points into formatted array
      for (let i = 0; i < pointArray.length; i++) {
        fetchedPoints.push({ x: pointArray[i].x, y: pointArray[i].y });
      }

      // Set points state
      setPoints(fetchedPoints);
    };

    fetchPoints();
  }, []);

  // Function to save points to backend
  const handleResults = async (x, y, result) => {
    try {
      const test = {
        x,
        y,
        result,
      };

      const response = await fetch(
        `${process.env.REACT_APP_API_URL}/api/perimetry/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(test),
        }
      );

      if (!response.ok) {
        throw new Error("Failed to send results");
      }
    } catch (error) {
      console.error("Failed to submit results:", error);
    }
  };

  useEffect(() => {
    const interval = setInterval(() => {
      setShowPoint(true);
      setTimeout(() => {
        setShowPoint(false);
        startRecording();
        const currentPoint = points[currentPointIndex];
        const currentX = currentPoint.x;
        const currentY = currentPoint.y;

        setCurrentPointIndex((prevIndex) => (prevIndex + 1) % points.length);
        if (currentPointIndex === points.length - 1 && side === "left") {
          setCurrentPointIndex(0);
          setSide("right");
        } else if (
          currentPointIndex === points.length - 1 &&
          side === "right"
        ) {
          navigateToExport();
        }

        handleResults(currentX, currentY, max >= 15);

        stopRecording();
      }, 300); // 200
    }, 100); // 1200

    return () => clearInterval(interval);
  }, [points, currentPointIndex, side, max]);

  return (
    <div className="split-container">
      <div className={side === "left" ? "split-focus" : "split-unfocus"}>
        {/* Render the current point */}
        {points.length > 0 && side === "left" && showPoint && (
          <Point
            key={currentPointIndex}
            x={points[currentPointIndex].x * 0.5}
            y={points[currentPointIndex].y}
          />
        )}
      </div>
      <div
        className="split-midpoint"
        style={{ left: side === "left" ? "calc(33%)" : "calc(66%)" }}
      >
        <p style={{ fontSize: "20px", fontWeight: "bold", color: "green" }}>
          +
        </p>
      </div>
      <div className={side === "right" ? "split-focus" : "split-unfocus"}>
        {/* Render the current point */}
        {points.length > 0 && side === "right" && showPoint && (
          <Point
            key={currentPointIndex}
            x={25 + points[currentPointIndex].x * 0.5}
            y={points[currentPointIndex].y}
          />
        )}
      </div>
    </div>
  );
}

export default Perimetry;
