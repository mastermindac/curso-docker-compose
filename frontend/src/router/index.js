import { refreshToken } from "@/auth";
import { store } from "@/store";
import Home from "@/views/Home.vue";
import Login from "@/views/auth/Login.vue";
import Logout from "@/views/auth/Logout.vue";
import Register from "@/views/auth/Register.vue";
import Http404 from "@/views/errors/Http404.vue";
import AddTodo from "@/views/todos/AddTodo.vue";
import EditTodo from "@/views/todos/EditTodo.vue";
import { createRouter, createWebHistory } from "vue-router";

const publicRoutes = [
  { path: "/login", component: Login },
  { path: "/register", component: Register },
  { name: "NotFound", path: "/:pathMatch(.*)*", component: Http404 },
]

const privateRoutes = [
  { path: "/", component: Home, alias: ["/todos", "/home"] },
  { path: "/todos/create", component: AddTodo },
  { path: "/todos/:id/edit", component: EditTodo, props: true },
  { path: "/logout", component: Logout },
];

privateRoutes.forEach(route => route.meta = { requiresAuth: true });

const router = createRouter({
  history: createWebHistory(),
  routes: privateRoutes.concat(publicRoutes),
});

router.beforeEach(async (to, from) => {
  if (to.meta.requiresAuth && !store.user.isAuthenticated) {
    try {
      await refreshToken();
    } catch (e) {
      store.nextRoute = to;
      return { path: "/login" }
    }
  }
})

export { router };
