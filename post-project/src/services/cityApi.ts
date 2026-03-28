import {createApi} from "@reduxjs/toolkit/query/react";
import {createBaseQuery} from "../utils/createBaseQuery.ts";
import type {ICity} from "../types/city/ICity.ts";
import type {ICityCreate} from "../types/city/ICityCreate.ts";
import {serialize} from "object-to-formdata";
import type {ICityEdit} from "../types/city/ICityEdit.ts";

export const cityApi= createApi({
    reducerPath: 'cityApi',
    baseQuery: createBaseQuery("cities"),
    tagTypes: ['Cities'],
    endpoints: (builder) => ({

        getCities: builder.query<ICity[], void>({
            query: () => {
                return {
                    url: '/',
                    method: 'GET',
                }
            },
            providesTags: ["Cities"]
        }),
        getCityById: builder.query<ICity, number>({
            query: (id) => ({
                url: `${id}/`,
                method: 'GET',
            }),
            providesTags: ["Cities"]
        }),
        deleteCity: builder.mutation<void, number>({
            query: id => ({
                url: `/${id}/`,
                method: "DELETE"
            }),
            invalidatesTags: ["Cities"]
        }),
        updateCity: builder.mutation<void, ICityEdit>({
            query: ({ id, formData }) => ({
                url: `${id}/`,
                method: "PUT",
                body: formData,
                formData: true,
            }),
            invalidatesTags: ["Cities"]
        }),
        createCity: builder.mutation<void, ICityCreate>({
            query: (body) => {
                const formData = serialize(body);
                return {
                    url: "/",
                    method: "POST",
                    body: formData
                }
            },
            invalidatesTags: ["Cities"]
        }),

    })
});

export const {
    useGetCitiesQuery,
    useDeleteCityMutation,
    useCreateCityMutation,
    useUpdateCityMutation,
    useGetCityByIdQuery,
} = cityApi;