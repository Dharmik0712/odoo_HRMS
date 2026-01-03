import {
Box,
Typography,
Stack,
Button,
Chip
} from "@mui/material";
import { useEffect, useState } from "react";
import api from "../../api/axios";

export default function LeaveApprovalPanel() {
const [leaves, setLeaves] = useState<any[]>([]);
const [loading, setLoading] = useState(false);

const loadLeaves = async () => {
    const res = await api.get("/leave/all");
    setLeaves(res.data.filter((l: any) => l.status === "PENDING"));
};

useEffect(() => {
    loadLeaves();
}, []);

const decide = async (id: string, approve: boolean) => {
    setLoading(true);
    await api.post(`/leave/${id}/decision`, {
    approve,
    admin_comment: approve ? "Approved" : "Rejected"
    });
    setLoading(false);
    loadLeaves();
};

return (
    <Box>
    <Typography variant="h6" gutterBottom>
        Pending Leave Approvals
    </Typography>

    {leaves.length === 0 && (
        <Typography color="text.secondary">
        No pending requests 🎉
        </Typography>
    )}

    <Stack spacing={2}>
        {leaves.map((leave) => (
        <Box
            key={leave.id}
            sx={{
            p: 2,
            border: "1px solid #e5e7eb",
            borderRadius: 2
            }}
        >
            <Typography fontWeight={600}>
            {leave.employee_id}
            </Typography>

            <Typography variant="body2">
            {leave.leave_type} | {leave.start_date} →{" "}
            {leave.end_date}
            </Typography>

            <Chip
            label={leave.status}
            size="small"
            color="warning"
            sx={{ mt: 1 }}
            />

            <Stack direction="row" spacing={1} mt={2}>
            <Button
                variant="contained"
                color="success"
                size="small"
                disabled={loading}
                onClick={() => decide(leave.id, true)}
            >
                Approve
            </Button>

            <Button
                variant="outlined"
                color="error"
                size="small"
                disabled={loading}
                onClick={() => decide(leave.id, false)}
            >
                Reject
            </Button>
            </Stack>
        </Box>
        ))}
    </Stack>
    </Box>
);
}
