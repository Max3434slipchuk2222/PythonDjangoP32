import { useNavigate } from "react-router-dom";
import { useGetDepartmentQuery } from "../../services/departmentApi.ts";

function DepartmentPage() {
    const navigate = useNavigate();

    const { data: departments, isLoading, error } = useGetDepartmentQuery();

    const deleteDepartmentHandler = async (id: number) => {
        if (window.confirm("Ви впевнені, що хочете видалити цей департамент?")) {
            console.log("Видалення департаменту з ID:", id);
        }
    };

    if (isLoading) {
        return (
            <div className="flex justify-center items-center min-h-screen">
                <span className="text-xl font-semibold dark:text-white">Loading ...</span>
            </div>
        );
    }

    return (
        <div className="p-5">
            <h1 className="text-3xl dark:text-white font-bold mb-6 text-center">Список відділень</h1>

            {error && (
                <p className="text-red-600 text-center mb-4">Помилка завантаження даних</p>
            )}

            <div className="p-10 bg-transparent min-h-screen">
                <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-10">
                    {Array.isArray(departments) && departments.map((dept) => (
                        <div
                            key={dept.id}
                            className="bg-white/80 dark:bg-slate-900/80 rounded-2xl shadow-xl overflow-hidden transform transition duration-500 hover:scale-105 hover:shadow-xl border border-slate-200/50 dark:border-slate-700/50"
                        >
                            <div className="bg-gradient-to-r from-blue-500 to-indigo-600 p-4 text-white">
                                <span className="text-xs uppercase tracking-wider opacity-80">Департамент</span>
                                <h2 className="text-xl font-bold truncate">{dept.name}</h2>
                            </div>

                            <div className="p-6">
                                <div className="mb-4">
                                    <p className="text-gray-600 dark:text-gray-300 text-sm line-clamp-3">
                                        {dept.description}
                                    </p>
                                </div>

                                <div className="space-y-2 border-t border-gray-100 dark:border-slate-700 pt-4">
                                    <div className="flex items-center text-sm text-gray-700 dark:text-gray-400">
                                        <span className="font-bold mr-2"> Місто:</span>
                                        {dept.city_name || "Не вказано"}
                                    </div>
                                    <div className="flex items-center text-sm text-gray-700 dark:text-gray-400">
                                        <span className="font-bold mr-2">Відповідальний:</span>
                                        {`${dept.user_name}`}
                                    </div>
                                </div>
                            </div>

                            <div className="px-6 pb-6 flex gap-3 justify-center">
                                <button
                                    type="button"
                                    onClick={() => deleteDepartmentHandler(dept.id)}
                                    className="flex-1 px-4 py-2 text-sm font-semibold rounded-lg bg-red-600 hover:bg-red-700 cursor-pointer text-white transition-colors shadow-md"
                                >
                                    Delete
                                </button>
                                <button
                                    type="button"
                                    onClick={() => navigate(`/edit-department/${dept.id}`)}
                                    className="flex-1 px-4 py-2 text-sm font-semibold rounded-lg bg-amber-300 hover:bg-amber-400 cursor-pointer text-black transition-colors shadow-md"
                                >
                                    Edit
                                </button>
                            </div>
                        </div>
                    ))}
                </div>

                {Array.isArray(departments) && departments.length === 0 && (
                    <p className="text-center text-gray-500 dark:text-gray-400">Департаментів поки що немає.</p>
                )}
            </div>
        </div>
    );
}

export default DepartmentPage;