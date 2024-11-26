import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./../App.css";
import useVolumeLevel from "./UseVolumeLevel";

const Point = ({ x, y }) => {
  const adjustedX = x * 1;
  return (
    <div style={{ position: "absolute", left: `${adjustedX}%`, top: `${y}%` }}>
      <p style={{ margin: 0, fontSize: "10px" }}>⚫</p>
    </div>
  );
};

function Perimetry() {
  const SIDES = ["left", "right"];

  const VISIBILITY_SPAN = 100;
  const INTERVAL = 50;

  const VOLUME_THRESHOLD = 15;

  const [startRecording, stopRecording, volume] = useVolumeLevel();

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
  const [side, setSide] = useState();

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
  }, []);

  // Function to save points to backend
  const handleResults = async (x, y, result) => {
    try {
      const ex = localStorage.getItem("exID");
      const data = {
        x: x,
        y: y,
        exID: ex,
        result: result,
      };
      const response = await fetch(
        `${process.env.REACT_APP_API_URL}/api/perimetry/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
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
    if (points.length !== 0) {
      startRecording();
      runPerimetryTest();
    }
  }, [points]);

  const runPerimetryTest = async () => {
    for (let sideIndex = 0; sideIndex < SIDES.length; sideIndex++) {
      setSide(SIDES[sideIndex]);
      for (let i = 0; i < 3; i++) { // TODO change points.length
        setShowPoint(true);
        await new Promise((resolve) => setTimeout(resolve, VISIBILITY_SPAN));
        setShowPoint(false);

        const currentPoint = points[i];
        const currentX = currentPoint.x;
        const currentY = currentPoint.y;
        await handleResults(
          currentX,
          currentY,
          volume.current >= VOLUME_THRESHOLD
        );

        setCurrentPointIndex((prevIndex) => prevIndex + 1);

        await new Promise((resolve) => setTimeout(resolve, INTERVAL));
      }
      setCurrentPointIndex(0);
    }
    stopRecording();
    navigateToExport();
  };

  return (
    <div className="split-container">
      <div className={side === "left" ? "split-focus" : "split-unfocus"}>
        {/* Render the current point */}
        {side === "left" && showPoint && (
          <Point
            key={currentPointIndex}
            x={points[currentPointIndex].x * 0.5}
            y={points[currentPointIndex].y}
          />
        )}
      </div>
      <div
        className="split-midpoint"
        style={{ left: side === "left" ? "calc(25%)" : "calc(75%)" }}
      >
        <p style={{ fontSize: "20px", fontWeight: "bold", color: "green" }}>
          +
        </p>
      </div>
      <div className={side === "right" ? "split-focus" : "split-unfocus"}>
        {/* Render the current point */}
        {side === "right" && showPoint && (
          <Point
            key={currentPointIndex}
            x={50 + points[currentPointIndex].x * 0.5}
            y={points[currentPointIndex].y}
          />
        )}
      </div>
    </div>
  );
}

export default Perimetry;
