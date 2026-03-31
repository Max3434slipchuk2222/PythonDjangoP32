import {createApi} from "@reduxjs/toolkit/query/react";
import {createBaseQuery} from "../utils/createBaseQuery.ts";
import type {IDepartment} from "../types/city/IDepartment.ts";

export const departmentApi= createApi({
    reducerPath: 'departmentApi',
    baseQuery: createBaseQuery("departments"),
    tagTypes: ['Departments'],
    endpoints: (builder) => ({

        getDepartment: builder.query<IDepartment[], void>({
            query: () => {
                return {
                    url: '/',
                    method: 'GET',
                }
            },
            providesTags: ["Departments"]
        }),
    })
});

export const {
    useGetDepartmentQuery
} = departmentApi;