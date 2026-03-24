import { useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { Editor } from "@tinymce/tinymce-react";
import { useGetCityByIdQuery, useUpdateCityMutation } from "../../services/cityApi.ts";
import type { ICity } from "../../types/city/ICity.ts";

function EditForm({ city }: { city: ICity }) {
    const navigate = useNavigate();
    const [updateCity] = useUpdateCityMutation();

    const [name, setName] = useState(city.name);
    const [description, setDescription] = useState(city.description ?? "");
    const [showEditor, setShowEditor] = useState(false);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            await updateCity({ id: city.id, name, description }).unwrap();
            navigate(-1);
        } catch (err) {
            console.log(err);
        }
    };

    return (
        <div className="flex justify-center items-center bg-transparent flex-col p-6">
            <h1 className="text-2xl font-bold mb-6 text-center text-gray-800 dark:text-white">
                Редагувати місто
            </h1>
            <form
                onSubmit={handleSubmit}
                className="bg-white dark:bg-slate-900 shadow-lg rounded-xl p-8 w-full max-w-xl border border-gray-200 dark:border-slate-700"
            >
                <div className="mb-5">
                    <label className="block text-sm font-medium text-gray-700 dark:text-slate-300 mb-1">
                        Назва
                    </label>
                    <input
                        type="text"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        className="w-full border border-gray-300 dark:border-slate-600 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-400 focus:border-blue-400 dark:bg-slate-800 dark:text-white transition"
                    />
                </div>

                <div className="mb-5">
                    <label className="block text-sm font-medium text-gray-700 dark:text-slate-300 mb-1">
                        Опис
                    </label>
                    <div
                        onClick={() => setShowEditor(true)}
                        className="w-full border border-gray-300 dark:border-slate-600 rounded-lg px-4 py-2 bg-gray-50 dark:bg-slate-800 cursor-pointer"
                    >
                        {description ? (
                            <div
                                className="prose dark:prose-invert max-w-none"
                                dangerouslySetInnerHTML={{ __html: description }}
                            />
                        ) : (
                            <span className="text-gray-400 dark:text-slate-500">Натисніть, щоб додати опис...</span>
                        )}
                    </div>
                </div>

                <div className="flex gap-3">
                    <button
                        type="submit"
                        className="flex-1 rounded-lg px-6 py-2 text-white bg-gradient-to-r from-cyan-400 via-cyan-500 to-cyan-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-cyan-300 dark:focus:ring-cyan-800 font-medium"
                    >
                        Зберегти
                    </button>
                    <button
                        type="button"
                        onClick={() => navigate(-1)}
                        className="flex-1 rounded-lg px-6 py-2 bg-gray-200 hover:bg-gray-300 dark:bg-slate-700 dark:hover:bg-slate-600 font-medium dark:text-white transition"
                    >
                        Скасувати
                    </button>
                </div>
            </form>

            {showEditor && (
                <div className="fixed inset-0 bg-black/50 dark:bg-black/70 flex items-center justify-center z-50">
                    <div className="bg-white dark:bg-slate-900 rounded-lg shadow-lg w-full max-w-3xl p-6 border border-gray-200 dark:border-slate-700">
                        <Editor
                            apiKey='0xky1zwyw6l6500xb89qg355iwjolt8lpsq5kx8it0rl3c71'
                            value={description}
                            onEditorChange={(content) => setDescription(content)}
                            init={{
                                height: 400,
                                menubar: true,
                                plugins: [
                                    "advlist autolink lists link image charmap print preview anchor",
                                    "searchreplace visualblocks code fullscreen",
                                    "insertdatetime media table paste code",
                                ],
                                toolbar:
                                    "undo redo | formatselect | bold italic backcolor |\
                                    alignleft aligncenter alignright alignjustify | \
                                    bullist numlist outdent indent | removeformat | image",
                                skin: document.documentElement.classList.contains("dark") ? "oxide-dark" : "oxide",
                                content_css: document.documentElement.classList.contains("dark") ? "dark" : "default"
                            }}
                        />
                        <div className="flex justify-end mt-4">
                            <button
                                onClick={() => setShowEditor(false)}
                                className="px-6 py-2 rounded-lg text-white bg-gradient-to-r from-cyan-400 via-cyan-500 to-cyan-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-cyan-300 dark:focus:ring-cyan-800 font-medium"
                            >
                                Зберегти опис
                            </button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}

export default function EditCityPage() {
    const { id } = useParams<{ id: string }>();
    const { data: city, isLoading } = useGetCityByIdQuery(Number(id));

    if (isLoading) return <p className="p-6 text-gray-500">Завантаження...</p>;
    if (!city) return <p className="p-6 text-gray-500">Місто не знайдено</p>;

    return <EditForm city={city} />;
}