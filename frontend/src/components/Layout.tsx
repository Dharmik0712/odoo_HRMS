import { Box } from "@mui/material";
import Navbar from "./Navbar";

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <Box>
      <Navbar />
      <Box sx={{ p: 3 }}>{children}</Box>
    </Box>
  );
}
