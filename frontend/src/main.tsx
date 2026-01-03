import ReactDOM from "react-dom/client";
import { ThemeProvider, CssBaseline } from "@mui/material";
import theme from "./theme/theme";
import App from "./App";
import { AuthProvider } from "./context/AuthContext";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <ThemeProvider theme={theme}>
    <CssBaseline />
    <AuthProvider>
      <App />
    </AuthProvider>
  </ThemeProvider>
);
