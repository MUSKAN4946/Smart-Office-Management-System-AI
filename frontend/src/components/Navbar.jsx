import { useNavigate } from "react-router-dom";

function Navbar() {

    const navigate = useNavigate();

const handleLogout = () => {

    localStorage.removeItem("token");

    localStorage.removeItem("user");

    navigate("/login");

};

    return (

        <div
            style={{
                backgroundColor: "#0d6efd",
                color: "white",
                padding: "18px 30px",
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center"
            }}
        >

            <h2>🏢 Smart Office Management System</h2>

            <button
                onClick={handleLogout}
                style={{
                    backgroundColor: "white",
                    color: "#0d6efd",
                    border: "none",
                    padding: "10px 18px",
                    borderRadius: "8px",
                    cursor: "pointer",
                    fontWeight: "bold"
                }}
            >
                Logout
            </button>

        </div>

    );

}

export default Navbar;