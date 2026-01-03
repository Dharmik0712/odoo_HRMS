import {
Grid,
Typography,
Paper
} from "@mui/material";
import { useState } from "react";
import DashboardCard from "./DashboardCard";

import AccessTimeIcon from "@mui/icons-material/AccessTime";
import EventAvailableIcon from "@mui/icons-material/EventAvailable";
import PaymentsIcon from "@mui/icons-material/Payments";
import PersonIcon from "@mui/icons-material/Person";
import LeavePanel from "../modules/leave/LeavePanel";
import AttendancePanel from "../modules/attendance/AttendancePanel";
import PayrollPanel from "../modules/payroll/PayrollPanel";

type Module = "attendance" | "leave" | "payroll" | "profile";

export default function EmployeeDashboard() {
const [activeModule, setActiveModule] =
    useState<Module | null>(null);

return (
    <>
    <Typography variant="h5" gutterBottom>
        Employee Dashboard
    </Typography>

    <Grid container spacing={3}>
        {/* LEFT: DASHBOARD CARDS */}
        <Grid item xs={12} md={8}>
        <Grid container spacing={3}>
            <Grid item xs={12} md={3}>
            <DashboardCard
                title="Attendance"
                subtitle="Check-in / Check-out"
                icon={<AccessTimeIcon color="primary" />}
                active={activeModule === "attendance"}
                onClick={() => setActiveModule("attendance")}
            />
            </Grid>

            <Grid item xs={12} md={3}>
            <DashboardCard
                title="Leave"
                subtitle="Apply & track leave"
                icon={<EventAvailableIcon color="success" />}
                active={activeModule === "leave"}
                onClick={() => setActiveModule("leave")}
            />
            </Grid>

            <Grid item xs={12} md={3}>
            <DashboardCard
                title="Payroll"
                subtitle="View salary"
                icon={<PaymentsIcon color="warning" />}
                active={activeModule === "payroll"}
                onClick={() => setActiveModule("payroll")}
            />
            </Grid>

            <Grid item xs={12} md={3}>
            <DashboardCard
                title="Profile"
                subtitle="Personal info"
                icon={<PersonIcon color="secondary" />}
                active={activeModule === "profile"}
                onClick={() => setActiveModule("profile")}
            />
            </Grid>
        </Grid>
        </Grid>

        {/* RIGHT: MODULE PANEL */}
        <Grid item xs={12} md={4}>
        <Paper
            elevation={3}
            sx={{
            p: 3,
            minHeight: 220,
            borderRadius: 3
            }}
        >
            {!activeModule && (
            <Typography color="text.secondary">
                Select a module to view details
            </Typography>
            )}

            {activeModule === "attendance" && <AttendancePanel />}

            {activeModule === "leave" && <LeavePanel />}


            {activeModule === "payroll" && <PayrollPanel />}


            {activeModule === "profile" && (
            <Typography>Profile module coming next</Typography>
            )}
        </Paper>
        </Grid>
    </Grid>
    </>
);
}
