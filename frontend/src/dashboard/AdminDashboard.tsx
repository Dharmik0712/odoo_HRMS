import { Grid, Typography, Paper } from "@mui/material";
import LeaveApprovalPanel from "../modules/admin/LeaveApprovalPanel";

export default function AdminDashboard() {
return (
    <>
    <Typography variant="h5" gutterBottom>
        Admin Dashboard
    </Typography>

    <Grid container spacing={3}>
        <Grid item xs={12} md={6}>
        <Paper sx={{ p: 3 }}>
            <LeaveApprovalPanel />
        </Paper>
        </Grid>

        <Grid item xs={12} md={6}>
        <Paper
            sx={{
            p: 3,
            minHeight: 200,
            color: "text.secondary"
            }}
        >
            Employee & Payroll modules coming next
        </Paper>
        </Grid>
    </Grid>
    </>
);
}
