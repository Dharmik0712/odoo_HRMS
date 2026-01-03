import api from "./axios";

export const applyLeave = (payload: {
leave_type: string;
start_date: string;
end_date: string;
remarks?: string;
}) => api.post("/leave/apply", payload);

export const getMyLeaves = () => api.get("/leave/me");
