import {
AppBar,
Toolbar,
Typography,
Avatar,
Box,
Button
} from "@mui/material";

export default function TopBar() {
return (
    <AppBar
    elevation={0}
    color="transparent"
    sx={{ borderBottom: "1px solid #e5e7eb" }}
    >
    <Toolbar>
        <Typography
        variant="h6"
        sx={{ flexGrow: 1, fontWeight: 600 }}
        >
        Dayflow HRMS
        </Typography>

        <Box display="flex" alignItems="center" gap={2}>
        <Avatar sx={{ bgcolor: "#2563eb" }}>D</Avatar>
        <Button
            variant="outlined"
            color="error"
            size="small"
        >
            Logout
        </Button>
        </Box>
    </Toolbar>
    </AppBar>
);
}
