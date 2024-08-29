import { Navigate } from "react-router-dom"
import { useAuthStore } from "../store/auth";

const PrivateRoute = ({ children }) => {
    const loggedIn = useAuthStore((state) => state.isLoggedIn)()

    return loggedIn ? <>{children}</> : <Navigate to ='/login'></Navigate>
}

export default PrivateRoute