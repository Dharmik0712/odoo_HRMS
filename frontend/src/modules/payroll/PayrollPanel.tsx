import {
Box,
Typography,
Divider,
Stack
} from "@mui/material";
import { useEffect, useState } from "react";
import { getMyPayroll } from "../../api/payroll.api";

export default function PayrollPanel() {
const [payroll, setPayroll] = useState<any>(null);

useEffect(() => {
    getMyPayroll().then((res) => setPayroll(res.data));
}, []);

if (!payroll) {
    return (
    <Typography color="text.secondary">
        Payroll not assigned yet
    </Typography>
    );
}

const netSalary =
    payroll.basic_salary +
    payroll.hra +
    payroll.allowances -
    payroll.deductions;

return (
    <Box>
    <Typography variant="h6" gutterBottom>
        Salary Details
    </Typography>

    <Stack spacing={1}>
        <SalaryRow label="Basic Salary" value={payroll.basic_salary} />
        <SalaryRow label="HRA" value={payroll.hra} />
        <SalaryRow label="Allowances" value={payroll.allowances} />
        <SalaryRow label="Deductions" value={-payroll.deductions} />
    </Stack>

    <Divider sx={{ my: 2 }} />

    <SalaryRow
        label="Net Salary"
        value={netSalary}
        highlight
    />

    <Typography
        variant="caption"
        color="text.secondary"
        mt={2}
        display="block"
    >
        Effective from: {payroll.effective_from}
    </Typography>
    </Box>
);
}

function SalaryRow({
label,
value,
highlight
}: {
label: string;
value: number;
highlight?: boolean;
}) {
return (
    <Box
    display="flex"
    justifyContent="space-between"
    fontWeight={highlight ? 600 : 400}
    >
    <Typography>{label}</Typography>
    <Typography>
        ₹ {value.toLocaleString("en-IN")}
    </Typography>
    </Box>
);
}
