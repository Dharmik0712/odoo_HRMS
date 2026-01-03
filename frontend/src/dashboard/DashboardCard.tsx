import {
Card,
CardContent,
Typography,
Box
} from "@mui/material";
import { ReactNode } from "react";

export default function DashboardCard({
title,
subtitle,
icon,
active,
onClick
}: {
title: string;
subtitle: string;
icon: ReactNode;
active?: boolean;
onClick: () => void;
}) {
return (
<Card
    onClick={onClick}
    sx={{
    height: 140,
    cursor: "pointer",
    border: active ? "2px solid #2563eb" : "1px solid #e5e7eb",
    backgroundColor: active ? "#eff6ff" : "#fff",
    transition: "all 0.2s ease",
    "&:hover": {
        boxShadow: 6,
        transform: "translateY(-4px)"
    }
    }}
>
    <CardContent>
    <Box display="flex" alignItems="center" gap={1}>
        {icon}
        <Typography fontWeight={600}>{title}</Typography>
    </Box>

    <Typography
        variant="body2"
        color="text.secondary"
        mt={1}
    >
        {subtitle}
    </Typography>
    </CardContent>
</Card>
);
}
