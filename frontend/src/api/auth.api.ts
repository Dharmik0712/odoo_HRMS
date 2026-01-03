import api from "./axios";

export const login = async (email: string, password: string) => {
const res = await api.post("/auth/login", { email, password });
return res.data;
};

export const signup = async (
employee_id: string,
email: string,
password: string,
role: string
) => {
const res = await api.post("/auth/signup", {
    employee_id,
    email,
    password,
    role
});
return res.data;
};
