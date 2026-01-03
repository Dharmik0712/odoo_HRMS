import EmployeeDashboard from "../dashboard/EmployeeDashboard";
import HRDashboard from "../dashboard/HRDashboard";
import AdminDashboard from "../dashboard/AdminDashboard";
import { useAuth } from "../context/AuthContext";

export default function RoleRouter() {
const { user } = useAuth();

if (!user) return null;

if (user.role === "EMPLOYEE") return <EmployeeDashboard />;
if (user.role === "HR") return <HRDashboard />;
if (user.role === "ADMIN") return <AdminDashboard />;

return null;
}
