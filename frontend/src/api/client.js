import { refreshToken } from "@/auth";
import { router } from "@/router";
import axios from "axios";

const { VITE_API_PROXY_PATH, VITE_API_URL } = import.meta.env;

const client = axios.create({
  baseURL: VITE_API_PROXY_PATH ?? VITE_API_URL,
});

client.interceptors.response.use((res) => res, async (err) => {
  if (err.response.status !== 401) {
    return Promise.reject(err);
  }

  const request = err.config;

  try {
    request.headers["Authorization"] = await refreshToken();
    return client(request);
  } catch (e) {
    router.push("/login");
    return Promise.reject(e);
  }
});

export {
  client,
};
