import { Card, CardContent, Typography, Button } from "@mui/material";
import { useEffect, useState } from "react";
import api from "../api/axios";

export default function LeaveApprovalPanel() {
const [leaves, setLeaves] = useState<any[]>([]);

useEffect(() => {
    api.get("/leave/all").then(res => setLeaves(res.data));
}, []);

const decide = async (id: string, approve: boolean) => {
    await api.post(`/leave/${id}/decision`, {
    approve,
    admin_comment: approve ? "Approved" : "Rejected"
    });
    setLeaves(leaves.filter(l => l.id !== id));
};

return (
    <Card>
    <CardContent>
        <Typography variant="h6">Leave Approvals</Typography>

        {leaves.map(l => (
        <Card key={l.id} sx={{ mt: 2, p: 2 }}>
            <Typography>
            {l.leave_type} ({l.start_date} → {l.end_date})
            </Typography>
            <Button onClick={() => decide(l.id, true)}>Approve</Button>
            <Button color="error" onClick={() => decide(l.id, false)}>
            Reject
            </Button>
        </Card>
        ))}
    </CardContent>
    </Card>
);
}
