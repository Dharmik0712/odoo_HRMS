import { createTheme } from "@mui/material";

const theme = createTheme({
palette: {
    primary: {
    main: "#2563eb" // modern blue
    },
    background: {
    default: "#f4f6f8"
    }
},
typography: {
    fontFamily: "Inter, Roboto, Arial, sans-serif",
    h5: {
    fontWeight: 600
    }
},
shape: {
    borderRadius: 12
}
});

export default theme;
