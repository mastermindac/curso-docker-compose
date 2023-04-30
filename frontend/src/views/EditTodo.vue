<template>
  <Spinner class="spinner" v-if="isLoading" />

  <Alert v-bind="alert" @close="alert.show = false" />

  <TodoForm
    v-if="todo !== null"
    :data="todo"
    :isLoading="isUpdatingTodo"
    title="Edit Todo"
    @submit="submit"
  />
</template>

<script setup>
import api from "@/api";
import Alert from "@/components/Alert.vue";
import Spinner from "@/components/Spinner.vue";
import TodoForm from "@/components/TodoForm.vue";
import { useAlert } from "@/composables/alert";
import { useFetch } from "@/composables/fetch.js";
import { humanReadableError } from "@/helpers/errors.js";
import { ref } from "vue";
import { useRouter } from "vue-router";

const props = defineProps(["id"]);

const { alert, showAlert } = useAlert();

const isUpdatingTodo = ref(false);

const router = useRouter();

const { data: todo, isLoading } = useFetch(api.todos.url(props.id), {
  onError: () => showAlert("Failed loading todo"),
});

async function submit(todo) {
  isUpdatingTodo.value = true;
  try {
    await api.todos.put(props.id, todo);
    router.push("/");
  } catch (e) {
    if (e.response.status == 422) {
      showAlert(humanReadableError(e.response.data.errors));
    } else {
      showAlert("Failed creating todo");
    }
  }
  isUpdatingTodo.value = false;
}
</script>

<style scoped>
.spinner {
  margin: auto;
}
</style>
