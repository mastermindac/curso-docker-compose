<template>
  <div class="form-container">
    <Alert v-bind="alert" @close="alert.show = false" />
    <LoginForm
      title="Register"
      :includeName="true"
      :isLoading="isRegistering"
      @submit="register"
    />
  </div>
</template>

<script setup>
import api from "@/api";
import { processLoginResponse } from "@/auth";
import Alert from "@/components/Alert.vue";
import LoginForm from '@/components/forms/LoginForm.vue';
import { useAlert } from "@/composables/alert";
import { httpErrorMessage, humanReadableError } from "@/helpers/errors";
import { ref } from "vue";
import { useRouter } from "vue-router";

const { alert, showAlert } = useAlert();
const isRegistering = ref(false);

const router = useRouter();

async function register(data) {
  isRegistering.value = true;
  try {
    const res = await api.auth.register(data);
    processLoginResponse(res);
    router.push("/todos");
  } catch (e) {
    if (e.response.status == 422) {
      showAlert(humanReadableError(e.response.data.errors));
    } else {
      showAlert(`Could not register: ${httpErrorMessage(e)}`);
    }
  }
  isRegistering.value = false;
}
</script>
