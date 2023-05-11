<template>
  <Spinner class="spinner" v-if="isLoading" />

  <div class="form-container">
    <Alert v-bind="alert" @close="alert.show = false" />

    <TodoForm
      v-if="todo !== null"
      title="Edit Todo"
      @submit="submit"
      :prepopulate="todo"
      :isLoading="isUpdatingTodo"
    />
  </div>
</template>

<script setup>
import api from "@/api";
import Alert from "@/components/Alert.vue";
import TodoForm from "@/components/forms/TodoForm.vue";
import Spinner from "@/components/Spinner.vue";
import { useAlert } from "@/composables/alert";
import { useFetch } from "@/composables/fetch.js";
import { httpErrorMessage, humanReadableError } from "@/helpers/errors.js";
import { ref } from "vue";
import { useRouter } from "vue-router";

const props = defineProps(["id"]);
const { alert, showAlert } = useAlert();
const isUpdatingTodo = ref(false);

const router = useRouter();

const { data: todo, isLoading } = useFetch(api.todos.route(props.id), {
  onError: () => showAlert("Failed loading todo"),
});

async function submit(todo) {
  isUpdatingTodo.value = true;
  try {
    await api.todos.put(props.id, todo);
    router.push("/");
  } catch (e) {
    if (e.response?.status == 422) {
      showAlert(humanReadableError(e.response.data.errors));
    } else {
      showAlert(`Failed updating todo: ${httpErrorMessage(e)}`);
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
