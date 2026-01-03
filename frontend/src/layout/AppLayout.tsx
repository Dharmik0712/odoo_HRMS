import { Box, Container } from "@mui/material";
import TopBar from "./TopBar";

export default function AppLayout({
children
}: {
children: React.ReactNode;
}) {
return (
    <Box sx={{ minHeight: "100vh", bgcolor: "background.default" }}>
    <TopBar />
    <Container maxWidth="xl" sx={{ mt: 4 }}>
        {children}
    </Container>
    </Box>
);
}
