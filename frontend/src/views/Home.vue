<template>
  <Alert v-bind="alert" @close="alert.show = false" />

  <section>
    <Spinner class="spinner" v-if="isLoading" />
    <div v-else>
      <Todo
        v-for="todo in todos"
        :key="todo.id"
        :todo="todo"
        @remove="removeTodo(todo.id)"
        @edit="$router.push(`/todos/${todo.id}/edit`)"
      />
    </div>
  </section>
</template>

<script setup>
import Alert from "@/components/Alert.vue";
import Spinner from "@/components/Spinner.vue";
import Todo from "@/components/Todo.vue";
import { useAlert } from "@/composables/alert.js";
import { useFetch } from "@/composables/fetch";
import axios from "axios";

const { alert, showAlert } = useAlert();

const { data: todos, isLoading } = useFetch("/api/todos", {
  onError: () => showAlert("Failed loading todos"),
});

async function removeTodo(id) {
  await axios.delete(`/api/todos/${id}`);
  todos.value = todos.value.filter((todo) => todo.id !== id);
}
</script>

<style scoped>
.spinner {
  margin: auto;
  margin-top: 30px;
}
</style>
