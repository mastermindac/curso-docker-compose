import About from "@/views/About.vue";
import AddTodo from "@/views/AddTodo.vue";
import EditTodo from "@/views/EditTodo.vue";
import Home from "@/views/Home.vue";
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    component: Home,
  },
  {
    path: "/about",
    component: About,
  },
  {
    path: "/todos/create",
    component: AddTodo,
  },
  {
    path: "/todos/:id/edit",
    component: EditTodo,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export { router };
