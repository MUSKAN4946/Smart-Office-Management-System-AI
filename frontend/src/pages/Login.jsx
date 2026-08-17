import { useState } from "react";
import { loginUser } from "../services/authService";

import { useNavigate } from "react-router-dom";

function Login() {

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const navigate = useNavigate();

    const handleLogin = async (e) => {

        e.preventDefault();

        try {

            const response = await loginUser({
                email,
                password
            });

            alert("Login Successful!");

            localStorage.setItem(
                "token",
                response.access_token
            );

            localStorage.setItem(
    "user",
    JSON.stringify(response.user)
);

            navigate("/dashboard");

            console.log(response);

        } 

        catch (error) {

            console.log("FULL ERROR:", error);

            console.log("Response:", error.response);

            console.log("Data:", error.response?.data);

            alert(JSON.stringify(error.response?.data));

}

    };

    return (

        <div>

            <h1>Smart Office Management System</h1>

            <h2>Login</h2>

            <form onSubmit={handleLogin}>

                <input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />

                <br /><br />

                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />

                <br /><br />

                <button type="submit">
                    Login
                </button>

            </form>

        </div>

    );

}

export default Login;