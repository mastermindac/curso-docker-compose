import { reactive } from "vue";

export const store = reactive({
  user: {
    isAuthenticated: false,
    id: null,
    name: null,
    email: null,
  }
});
