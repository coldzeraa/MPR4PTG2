import { useEffect, useRef } from "react";

const useVolumeLevel = () => {
  const audioContextRef = useRef(null);
  const analyserRef = useRef(null);
  const volumeRef = useRef(0);
  const volumeHistory = useRef([]); 
  let animationFrameId = null;

  const startRecording = () => {
    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
      console.error("Browser does not support audio recording.");
      return;
    }

    navigator.mediaDevices
      .getUserMedia({ audio: true })
      .then((stream) => {
        const audioContext = new (window.AudioContext || window.webkitAudioContext)();
        audioContextRef.current = audioContext;

        const analyser = audioContext.createAnalyser();
        analyser.fftSize = 256;
        analyserRef.current = analyser;

        const source = audioContext.createMediaStreamSource(stream);
        source.connect(analyser);

        const dataArray = new Uint8Array(analyser.frequencyBinCount);

        const updateVolume = () => {
          analyser.getByteFrequencyData(dataArray);
          const sum = dataArray.reduce((a, b) => a + b, 0);
          const average = sum / dataArray.length;

          volumeRef.current = average;
          volumeHistory.current.push(average); // Speichern der Lautstärkewerte
          console.log(average)

          animationFrameId = requestAnimationFrame(updateVolume);
        };

        updateVolume();
      })
      .catch((error) => {
        console.error("Error accessing microphone:", error);
      });
  };

  const stopRecording = () => {
    if (animationFrameId) {
      cancelAnimationFrame(animationFrameId);
    }

    if (audioContextRef.current) {
      audioContextRef.current.close();
      audioContextRef.current = null;
    }

    volumeRef.current = 0;
    volumeHistory.current = []; // Reset der Lautstärkewerte
  };

  useEffect(() => {
    return () => {
      if (animationFrameId) {
        cancelAnimationFrame(animationFrameId);
      }

      if (audioContextRef.current) {
        audioContextRef.current.close();
        audioContextRef.current = null;
      }
    };
  }, []);

  return [startRecording, stopRecording, volumeRef, volumeHistory]; // Rückgabe von volumeHistory
};

export default useVolumeLevel;