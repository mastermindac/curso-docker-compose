<template>
  <div class="form-container">
    <Alert v-bind="alert" @close="alert.show = false" />
    <LoginForm @submit="login" :isLoading="isLoggingIn" />
  </div>
</template>

<script setup>
import LoginForm from '@/components/forms/LoginForm.vue';

import api from "@/api";
import { processLoginResponse } from "@/auth";
import Alert from "@/components/Alert.vue";
import { useAlert } from "@/composables/alert";
import { httpErrorMessage, humanReadableError } from '@/helpers/errors';
import { store } from '@/store';
import { ref } from "vue";
import { useRouter } from "vue-router";

const { alert, showAlert } = useAlert();
const isLoggingIn = ref(false);

const router = useRouter();

async function login(credentials) {
  isLoggingIn.value = true;
  try {
    const res = await api.auth.login(credentials);
    processLoginResponse(res);

    let nextRoute = "/todos";
    if (store.nextRoute) {
      nextRoute = store.nextRoute;
      store.nextRoute = null;
    }
    router.push(nextRoute);
  } catch (e) {
    if (e.response?.status == 422) {
      showAlert(humanReadableError(e.response.data.errors));
    } else if (e.response?.status == 401) {
      showAlert("Invalid credentials.");
    } else {
      showAlert(`Could not log in: ${httpErrorMessage(e)}`);
    }
  }
  isLoggingIn.value = false;
}
</script>
