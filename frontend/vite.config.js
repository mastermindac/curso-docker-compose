import { fileURLToPath, URL } from "node:url";

import vue from "@vitejs/plugin-vue";
import { defineConfig, loadEnv } from "vite";

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd());

  return {
    plugins: [vue()],
    resolve: {
      alias: {
        "@": fileURLToPath(new URL("./src", import.meta.url)),
      },
    },
    server: {
      proxy: {
        [env.VITE_API_PROXY_PATH]: {
          target: env.VITE_API_URL,
          rewrite: (path) => {
            const pattern = new RegExp(`^\\${env.VITE_API_PROXY_PATH}`);
            return path.replace(pattern, "");
          },
        },
        [env.VITE_API_REFRESH_TOKEN_PATH]: {
          target: env.VITE_API_URL,
        }
      },
    },
  };
});
