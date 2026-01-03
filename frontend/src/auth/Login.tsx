import { useAuth } from "../context/AuthContext";

const { login: setAuth } = useAuth();

const submit = async () => {
const res = await login(email, password);

localStorage.setItem("token", res.access_token);

// backend already returns role
setAuth({ role: res.role });

window.location.href = "/";
};
