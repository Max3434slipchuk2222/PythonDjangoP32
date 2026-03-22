import { useCities } from '../hooks/useCities';

export default function CityList() {
    const { data: cities, isLoading, isError, error } = useCities();

    if (isLoading) return <p>Завантаження міст...</p>;
    if (isError) return <p>Помилка: {(error as Error).message}</p>;

    return (
        <div className="p-6">
            <h2 className="text-center text-2xl font-semibold text-gray-900 mb-6">Міста</h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                {cities?.map((city) => (
                    <div
                        key={city.id}
                        className="bg-white border border-gray-200 rounded-xl p-5 hover:shadow-md transition-shadow cursor-pointer"
                    >
                        <h3 className="text-center text-lg font-medium text-gray-900 mb-2">{city.name}</h3>
                        <p className="text-center text-sm text-gray-500 line-clamp-3">
                            {city.description ?? 'Опис відсутній'}
                        </p>
                    </div>
                ))}
            </div>

            {cities?.length === 0 && (
                <p className="text-gray-400 text-center mt-12">Міст поки немає</p>
            )}
        </div>
    );
}