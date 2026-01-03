import AppLayout from "./layout/AppLayout";
import RoleRouter from "./routes/RoleRouter";
import { useAuth } from "./context/AuthContext";
import Login from "./auth/Login";

export default function App() {
  const { user } = useAuth();

  if (!user) return <Login />;

  return (
    <AppLayout>
      <RoleRouter />
    </AppLayout>
  );
}
