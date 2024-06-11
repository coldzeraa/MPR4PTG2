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

  const fetchPoints = async () => {
    try {
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
        throw new Error("Fetching points failed");
      }

      // Get JSON data from response
      const data = await response.json();

      // Convert to array
      const pointArray = data.points;

      // Map points to array
      const fetchedPoints = pointArray.map((point) => ({
        x: point.x,
        y: point.y,
      }));

      setPoints(fetchedPoints);
    } catch (error) {
      console.error("Error fetching points:", error);
    }
  };

  // Get Points from Backend
  useEffect(() => {
    fetchPoints();
    startRecording();
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
        const currentPoint = points[currentPointIndex];
        const currentX = currentPoint.x;
        const currentY = currentPoint.y;

        // TODO sometimes currentPoint.x is null
        setCurrentPointIndex((prevIndex) => (prevIndex + 1) % points.length);

        //setCurrentPointIndex((prevIndex) => prevIndex + 1);
        console.log(currentPointIndex);

        if (currentPointIndex === points.length - 1 && side === "left") {
          setCurrentPointIndex(0);
          setSide("right");
        } else if (
          currentPointIndex === points.length - 1 &&
          side === "right"
        ) {
          navigateToExport();
          stopRecording();
        }
        handleResults(currentX, currentY, max >= 15);
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
