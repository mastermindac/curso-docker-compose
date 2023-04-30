import axios from "axios";

export const client = axios.create({
    // Direct communication.
    baseURL: import.meta.env.VITE_API_URL,

    // Proxy.
    // baseURL: "/api",
});
