import { useNavigate } from "react-router-dom";

function BackButton() {
    const navigate = useNavigate();
    return (
        <button className="button back-button" onClick={() => navigate(-1)}>← Zurück</button>
    );
}

export default BackButton;