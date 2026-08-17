import { Link } from "react-router-dom";

function Sidebar() {
    return (
        <div
            style={{
                width: "230px",
                background: "#1e3a8a",
                color: "white",
                minHeight: "100vh",
                padding: "20px",
                position: "fixed",
                left: 0,
                top: 0
            }}
        >
            <h2>🏢 Smart Office</h2>

            <hr />

            <div style={{ display: "flex", flexDirection: "column", gap: "15px" }}>

                <Link to="/dashboard" style={linkStyle}>
                    📊 Dashboard
                </Link>

                <Link to="#" style={linkStyle}>
                    👨 Employees
                </Link>

                <Link to="#" style={linkStyle}>
                    🏢 Departments
                </Link>

                <Link to="#" style={linkStyle}>
                    📅 Attendance
                </Link>

                <Link to="#" style={linkStyle}>
                    🌴 Leaves
                </Link>

                <Link to="#" style={linkStyle}>
                    💰 Payroll
                </Link>

                <Link to="#" style={linkStyle}>
                    📄 Reports
                </Link>

                <Link to="#" style={linkStyle}>
                    👤 Profile
                </Link>

                <Link to="#" style={linkStyle}>
                    🔔 Notifications
                </Link>

            </div>
        </div>
    );
}

const linkStyle = {
    color: "white",
    textDecoration: "none",
    fontSize: "17px"
};

export default Sidebar;