// src/Canvas.js
import React, { useRef, useEffect } from 'react';
import html2canvas from 'html2canvas';
import jsPDF from 'jspdf';

const Canvas = ({ imageSrc, points, onExport }) => {
  const canvasRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    const context = canvas.getContext('2d');
    const image = new Image();
    image.src = imageSrc;

    image.onload = () => {
      context.drawImage(image, 0, 0, canvas.width, canvas.height);

      points.forEach(point => {
        context.beginPath();
        context.arc(point.x, point.y, 5, 0, 2 * Math.PI);
        context.fillStyle = 'red';
        context.fill();
        context.closePath();
      });
    };
  }, [imageSrc, points]);

  const exportToImage = async () => {
    const canvas = canvasRef.current;
    const imgData = await html2canvas(canvas).then(canvas => canvas.toDataURL('image/jpeg'));
    const pdf = new jsPDF();
    pdf.addImage(imgData, 'JPEG', 0, 0);
    pdf.save('perimetry-result.pdf');
  };

  useEffect(() => {
    if (onExport) {
      onExport(exportToImage);
    }
  }, [onExport]);

  return (
    <div>
      <canvas
        ref={canvasRef}
        width={800}
        height={600}
        style={{ border: '1px solid black', display: 'block' }}
      />
    </div>
  );
};

export default Canvas;
