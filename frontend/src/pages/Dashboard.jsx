import { useEffect, useState } from "react";
import { getDashboard } from "../services/dashboardService";

import DashboardCard from "../components/DashboardCard";

import Navbar from "../components/Navbar";

import Sidebar from "../components/Sidebar";


function Dashboard() {

    const user = JSON.parse(localStorage.getItem("user"));

    const [dashboard, setDashboard] = useState(null);

    useEffect(() => {

        loadDashboard();

    }, []);

    const loadDashboard = async () => {

        try {

            const data = await getDashboard();

            setDashboard(data);

        } catch (error) {

            console.log(error);

            alert("Failed to load dashboard");

        }

    };

    if (!dashboard) {

        return <h2>Loading Dashboard...</h2>;

    }




   return (

    <div
        style={{
            display: "flex"
        }}
    >

        <Sidebar />

        <div
            style={{
                flex: 1
            }}
        >

            <Navbar />

            <div
                style={{
                    padding: "40px",
                    backgroundColor: "#f4f6f9",
                    minHeight: "100vh",
                    maxWidth: "1200px",
                    margin: "0 auto"
                }}
            >

<h1
    style={{
        marginBottom: "10px"
    }}
>
    Dashboard
</h1>


<h2>
    Welcome, {user?.full_name} 👋
</h2>

<p>
    Role : {user?.role}
</p>

<p>
    {new Date().toLocaleDateString()}
</p>

<br />

<div
    style={{
        display: "flex",
        flexWrap: "wrap",
        justifyContent: "center",
        gap: "20px"
    }}
>

    <DashboardCard
        title="Employees"
        value={dashboard.total_employees}
    />

    <DashboardCard
        title="Departments"
        value={dashboard.total_departments}
    />

    <DashboardCard
        title="Attendance"
        value={dashboard.total_attendance}
    />

    <DashboardCard
        title="Leaves"
        value={dashboard.total_leaves}
    />

    <DashboardCard
        title="Payrolls"
        value={dashboard.total_payrolls}
    />

    <DashboardCard
        title="Users"
        value={dashboard.total_users}
    />

</div>

            </div>

        </div>

    </div>

);

}

export default Dashboard;