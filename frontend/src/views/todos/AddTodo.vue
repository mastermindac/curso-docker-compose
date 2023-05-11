<template>
  <div class="form-container">
    <Alert v-bind="alert" @close="alert.show = false" />
    <TodoForm :isLoading="isPostingTodo" @submit="submit" />
  </div>
</template>

<script setup>
import api from "@/api";
import Alert from "@/components/Alert.vue";
import TodoForm from "@/components/forms/TodoForm.vue";
import { useAlert } from "@/composables/alert";
import { httpErrorMessage, humanReadableError } from "@/helpers/errors";
import { ref } from "vue";
import { useRouter } from "vue-router";

const { alert, showAlert } = useAlert();
const isPostingTodo = ref(false);

const router = useRouter();

async function submit(todo) {
  isPostingTodo.value = true;
  try {
    await api.todos.post(todo);
    router.push("/");
  } catch (e) {
    if (e.response?.status == 422) {
      showAlert(humanReadableError(e.response.data.errors));
    } else {
      showAlert(`Failed creating todo: ${httpErrorMessage(e)}`);
    }
  }
  isPostingTodo.value = false;
}
</script>
