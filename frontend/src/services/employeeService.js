import API from "../api/axios";

export const getEmployees = async () => {

    const token = localStorage.getItem("token");

    const response = await API.get(
        "/employees/",
        {
            headers: {
                Authorization: `Bearer ${token}`
            }
        }
    );

    return response.data;

};

export const addEmployee = async (employee) => {

    const token = localStorage.getItem("token");

    const response = await API.post(
        "/employees/",
        employee,
        {
            headers: {
                Authorization: `Bearer ${token}`
            }
        }
    );

    return response.data;

};



export const updateEmployee = async (id, employee) => {

    const token = localStorage.getItem("token");

    const response = await API.put(

        `/employees/${id}`,

        employee,

        {
            headers: {
                Authorization: `Bearer ${token}`
            }
        }

    );

    return response.data;

};



export const deleteEmployee = async (id) => {

    const token = localStorage.getItem("token");

    const response = await API.delete(

        `/employees/${id}`,

        {
            headers: {
                Authorization: `Bearer ${token}`
            }
        }

    );

    return response.data;

};