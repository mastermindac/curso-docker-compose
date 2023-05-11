<template>
  <Alert v-bind="alert" @close="alert.show = false" />

  <section>
    <Spinner class="spinner" v-if="isLoading" />
    <div v-else>
      <Todo
        v-if="todos?.length > 0"
        v-for="todo in todos"
        :key="todo.id"
        :todo="todo"
        @remove="removeTodo(todo.id)"
        @edit="$router.push(`/todos/${todo.id}/edit`)"
      />
      <p v-else-if="!error" class="empty-message">
        You don't have any <i>todos</i> yet.
        Try <RouterLink to="/todos/create">adding one</RouterLink>!
      </p>
    </div>
  </section>
</template>

<script setup>
import api from "@/api";
import Alert from "@/components/Alert.vue";
import Spinner from "@/components/Spinner.vue";
import Todo from "@/components/Todo.vue";
import { useAlert } from "@/composables/alert.js";
import { useFetch } from "@/composables/fetch.js";
import { httpErrorMessage } from "@/helpers/errors";

const { alert, showAlert } = useAlert();

const { data: todos, isLoading, error } = useFetch(api.todos.route(), {
  onError: (e) =>  showAlert(`Failed loading todos: ${httpErrorMessage(e)}`),
});

async function removeTodo(id) {
  try {
    await api.todos.delete(id);
    todos.value = todos.value.filter((todo) => todo.id !== id);
  } catch (e) {
    showAlert(`Could not delete todo: ${httpErrorMessage(e)}`);
  }
}
</script>

<style scoped>
.spinner {
  margin: auto;
  margin-top: 30px;
}

.empty-message {
  font-size: large;
}

.empty-message > a {
  color: var(--accent-color);
}
</style>
