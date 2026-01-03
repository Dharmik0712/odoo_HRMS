import {
Box,
Typography,
Chip,
Stack
} from "@mui/material";

export default function LeaveList({
leaves
}: {
leaves: any[];
}) {
return (
    <Box mt={3}>
    <Typography variant="subtitle1" gutterBottom>
        My Leave Requests
    </Typography>

    {leaves.length === 0 && (
        <Typography color="text.secondary">
        No leave requests yet
        </Typography>
    )}

    <Stack spacing={1}>
        {leaves.map((leave) => (
        <Box
            key={leave.id}
            sx={{
            p: 2,
            border: "1px solid #e5e7eb",
            borderRadius: 2
            }}
        >
            <Typography fontWeight={500}>
            {leave.leave_type}
            </Typography>

            <Typography variant="body2">
            {leave.start_date} → {leave.end_date}
            </Typography>

            <Chip
            label={leave.status}
            size="small"
            color={
                leave.status === "APPROVED"
                ? "success"
                : leave.status === "REJECTED"
                ? "error"
                : "warning"
            }
            sx={{ mt: 1 }}
            />
        </Box>
        ))}
    </Stack>
    </Box>
);
}
