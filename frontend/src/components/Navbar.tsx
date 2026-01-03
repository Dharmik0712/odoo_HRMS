import { AppBar, Toolbar, Typography, Button } from "@mui/material";

export default function Navbar() {
const logout = () => {
    localStorage.removeItem("token");
    window.location.href = "/login";
};

return (
    <AppBar position="static">
    <Toolbar>
        <Typography sx={{ flexGrow: 1 }}>Dayflow HRMS</Typography>
        <Button color="inherit" onClick={logout}>
        Logout
        </Button>
    </Toolbar>
    </AppBar>
);
}
