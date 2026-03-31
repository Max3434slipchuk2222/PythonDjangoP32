import './App.css'
import { Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import AddCityPage from "./pages/AddCityPage";
import MainLayout from "./MainLayout";
import EditCityPage from "./pages/EditCityPage";
import DepartmentPage from "./pages/DepartmentPage";



function App() {
    return (
        <Routes>
            <Route path="/" element={<MainLayout/>}>
                <Route index element={<HomePage />} />
                <Route path="add-city" element={<AddCityPage />} />
                <Route path="/edit-city/:id" element={<EditCityPage />} />
                <Route path="/departments" element={<DepartmentPage />}/>
            </Route>
        </Routes>
    )
}

export default App 