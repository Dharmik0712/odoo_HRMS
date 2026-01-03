import api from "./axios";

export const getMyPayroll = () => api.get("/payroll/me");
