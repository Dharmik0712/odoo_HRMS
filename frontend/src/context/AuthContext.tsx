import { createContext, useContext, useState } from "react";

type User = {
role: "EMPLOYEE" | "HR" | "ADMIN";
};

type AuthContextType = {
user: User | null;
login: (user: User) => void;
logout: () => void;
};

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: React.ReactNode }) {
const [user, setUser] = useState<User | null>(() => {
    const stored = localStorage.getItem("user");
    return stored ? JSON.parse(stored) : null;
});

const login = (user: User) => {
    setUser(user);
    localStorage.setItem("user", JSON.stringify(user));
};

const logout = () => {
    setUser(null);
    localStorage.removeItem("user");
    localStorage.removeItem("token");
    window.location.href = "/";
};

return (
    <AuthContext.Provider value={{ user, login, logout }}>
    {children}
    </AuthContext.Provider>
);
}

export function useAuth() {
const context = useContext(AuthContext);
if (!context) {
    throw new Error("useAuth must be used within AuthProvider");
}
return context;
}
