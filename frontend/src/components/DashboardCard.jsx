function DashboardCard({ title, value }) {

    return (

        <div
            style={{
                width: "220px",
                background: "white",
                borderRadius: "15px",
                padding: "25px",
                textAlign: "center",
                boxShadow: "0 4px 12px rgba(0,0,0,0.15)",
                transition: "0.3s"
            }}
        >

            <h3
                style={{
                    color: "#555"
                }}
            >
                {title}
            </h3>

            <h1
                style={{
                    color: "#0d6efd",
                    fontSize: "40px"
                }}
            >
                {value}
            </h1>

        </div>

    );

}

export default DashboardCard;