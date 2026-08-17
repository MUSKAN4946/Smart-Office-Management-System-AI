import API from "../api/axios";

export const loginUser = async (data) => {

    const formData = new URLSearchParams();

    formData.append("username", data.email);
    formData.append("password", data.password);

    const response = await API.post(
        "/users/login",
        formData,
        {
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            }
        }
    );

    return response.data;
};