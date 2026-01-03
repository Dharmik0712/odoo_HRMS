    import { Box, Button, Typography, Stack } from "@mui/material";
    import api from "../../api/axios";
    import { useState } from "react";

    export default function AttendancePanel() {
    const [loading, setLoading] = useState(false);

    const checkIn = async () => {
    setLoading(true);
    await api.post("/attendance/check-in");
    setLoading(false);
    alert("Checked in successfully");
    };

    const checkOut = async () => {
    setLoading(true);
    await api.post("/attendance/check-out");
    setLoading(false);
    alert("Checked out successfully");
    };

    return (
    <Box>
    <Typography variant="h6" gutterBottom>
    Attendance
    </Typography>

    <Stack spacing={2} direction="row">
    <Button
        variant="contained"
        onClick={checkIn}
        disabled={loading}
    >
        Check In
    </Button>

    <Button
        variant="outlined"
        onClick={checkOut}
        disabled={loading}
    >
        Check Out
    </Button>
    </Stack>
    </Box>
    );
    }
