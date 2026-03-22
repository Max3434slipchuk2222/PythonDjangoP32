import './App.css'
import {Routes, Route, Link, useLocation} from 'react-router-dom';
import CityList from './components/CityList';
import Home from './pages/Home';


const navLinks = [
    { to: '/', label: 'Головна' },
    { to: '/cities', label: 'Міста' },
];

function Navbar() {
    const location = useLocation();
    return (
        <nav className="w-full border-b border-gray-200 bg-white px-6 py-4 flex items-center justify-between">
            <span className="text-xl font-semibold text-gray-900">CityApp</span>
            <ul className="flex gap-6">
                {navLinks.map(link => (
                    <li key={link.to}>
                        <Link
                            to={link.to}
                            className={`text-sm transition-colors ${
                                location.pathname === link.to
                                    ? 'text-blue-600 font-medium'
                                    : 'text-gray-500 hover:text-gray-900'
                            }`}
                        >
                            {link.label}
                        </Link>
                    </li>
                ))}
            </ul>
        </nav>
    );
}
export default function App() {
    return (
        <div className="min-h-screen bg-gray-50">
            <Navbar />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/cities" element={<CityList />} />
            </Routes>
        </div>
    );
}
