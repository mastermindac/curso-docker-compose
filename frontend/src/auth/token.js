import api from "@/api";
import { store } from "@/store";
import axios from "axios";

const {
  VITE_API_PROXY_PATH,
  VITE_API_URL,
  VITE_API_REFRESH_TOKEN_PATH,
} = import.meta.env;

async function refreshToken() {
  const url = VITE_API_PROXY_PATH
    ? VITE_API_REFRESH_TOKEN_PATH
    : VITE_API_URL + VITE_API_REFRESH_TOKEN_PATH;

  const res = await axios.post(url, {}, {
    withCredentials: true
  });

  return processLoginResponse(res);
}

function processLoginResponse({ data: { access_token, user } }) {
  const authorization = `Bearer ${access_token}`;
  api.client.defaults.headers.common["Authorization"] = authorization;
  store.user = { isAuthenticated: true, ...user };

  return authorization;
}

function processLogoutResponse(res) {
  delete api.client.defaults.headers.common["Authorization"];
  store.user = { isAuthenticated: false };
}

export {
  refreshToken,
  processLoginResponse,
  processLogoutResponse,
}
