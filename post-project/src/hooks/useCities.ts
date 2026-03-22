import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import type {City} from '../types/City';

const api = axios.create({ baseURL: '/api' });

const getCities = async (): Promise<City[]> => {
    const response = await api.get('/cities/');
    console.log('response.data:', response.data);
    const data = response.data;
    return Array.isArray(data) ? data : data.results ?? [];
};

export const useCities = () => {
    return useQuery<City[]>({
        queryKey: ['cities'],
        queryFn: getCities,
    });
};