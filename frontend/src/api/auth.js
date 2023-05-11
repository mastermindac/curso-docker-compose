import { client } from "./client.js";

export const auth = {
  login(credentials) {
    return client.post("/auth/login", credentials);
  },

  logout() {
    return client.post("/auth/logout");
  },

  register(user) {
    return client.post("/auth/register", user);
  },
}
