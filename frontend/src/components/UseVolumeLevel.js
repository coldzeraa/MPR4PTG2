import { useState, useEffect, useRef } from "react";
import { SoundMeter } from "./Soundmeter";

function handleSuccess(stream) {
  window.stream = stream;
  const soundMeter = (window.soundMeter = new SoundMeter(window.audioContext));
  soundMeter.connectToSource(stream, function (e) {
    if (e) {
      alert(e);
      return;
    }
  });
}

function handleError(error) {
  console.log(
    "navigator.MediaDevices.getUserMedia error: ",
    error.message,
    error.name
  );
}

function useVolumeLevel() {
  const [level, setLevel] = useState(0);
  const [isRecording, setIsRecording] = useState(false);
  const volumeRef = useRef(0); // useRef verwenden, um volume zu halten

  const stopRecording = () => {
    if (window.soundMeter && isRecording) {
      setLevel(0);
      window.soundMeter.stop();
      setIsRecording(false);
    }
  };

  const startRecording = () => {
    const constraints = (window.constraints = {
      audio: true,
      video: false,
    });
    try {
      window.AudioContext = window.AudioContext || window.webkitAudioContext;
      window.audioContext = new AudioContext();
    } catch (e) {
      alert("Web Audio API not supported.");
    }

    navigator.mediaDevices
      .getUserMedia(constraints)
      .then(handleSuccess)
      .catch(handleError);

    setIsRecording(true);
  };

  const updateVolume = () => {
    if (window.soundMeter && isRecording) {
      // let v = window.soundMeter.instant * 200;
      // setLevel(Math.min(v, 100));
      // console.log(level);
      let v = window.soundMeter.instant * 200;
      setLevel(Math.min(v, 100));
      volumeRef.current = v; // volumeRef aktualisieren
      console.log(volumeRef.current); // Aktuellen Wert von `volume` überprüfen
    }
  };

  useEffect(() => {
    let intervalId;
    intervalId = setInterval(updateVolume, 50);

    return () => clearInterval(intervalId);
  });

  return [startRecording, stopRecording, volumeRef];
}

export default useVolumeLevel;
