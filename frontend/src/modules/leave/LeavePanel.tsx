import {
Box,
Button,
MenuItem,
TextField,
Typography
} from "@mui/material";
import { useEffect, useState } from "react";
import { applyLeave, getMyLeaves } from "../../api/leave.api";
import LeaveList from "./LeaveList";

export default function LeavePanel() {
const [leaveType, setLeaveType] = useState("PAID");
const [startDate, setStartDate] = useState("");
const [endDate, setEndDate] = useState("");
const [remarks, setRemarks] = useState("");
const [leaves, setLeaves] = useState<any[]>([]);
const [loading, setLoading] = useState(false);

const loadLeaves = async () => {
    const res = await getMyLeaves();
    setLeaves(res.data);
};

useEffect(() => {
    loadLeaves();
}, []);

const submit = async () => {
    setLoading(true);
    await applyLeave({
    leave_type: leaveType,
    start_date: startDate,
    end_date: endDate,
    remarks
    });
    setLoading(false);
    setStartDate("");
    setEndDate("");
    setRemarks("");
    loadLeaves();
};

return (
    <Box>
    <Typography variant="h6" gutterBottom>
        Apply Leave
    </Typography>

    <TextField
        select
        fullWidth
        label="Leave Type"
        margin="dense"
        value={leaveType}
        onChange={(e) => setLeaveType(e.target.value)}
    >
        <MenuItem value="PAID">Paid Leave</MenuItem>
        <MenuItem value="SICK">Sick Leave</MenuItem>
        <MenuItem value="UNPAID">Unpaid Leave</MenuItem>
    </TextField>

    <TextField
        fullWidth
        type="date"
        label="Start Date"
        margin="dense"
        InputLabelProps={{ shrink: true }}
        value={startDate}
        onChange={(e) => setStartDate(e.target.value)}
    />

    <TextField
        fullWidth
        type="date"
        label="End Date"
        margin="dense"
        InputLabelProps={{ shrink: true }}
        value={endDate}
        onChange={(e) => setEndDate(e.target.value)}
    />

    <TextField
        fullWidth
        label="Remarks"
        margin="dense"
        value={remarks}
        onChange={(e) => setRemarks(e.target.value)}
    />

    <Button
        variant="contained"
        fullWidth
        sx={{ mt: 2 }}
        onClick={submit}
        disabled={loading}
    >
        Apply Leave
    </Button>

    <LeaveList leaves={leaves} />
    </Box>
);
}
