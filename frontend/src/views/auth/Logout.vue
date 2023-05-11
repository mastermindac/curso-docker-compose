<template>
  <Alert v-bind="alert" @close="alert.show = false" />
  <div class="spinner" v-if="isLoggingOut">
    <Spinner />
    <p>
      Logging Out...
    </p>
  </div>
</template>

<script setup>
import api from "@/api";
import { processLogoutResponse } from "@/auth";
import Alert from '@/components/Alert.vue';
import Spinner from '@/components/Spinner.vue';
import { useAlert } from '@/composables/alert';
import { httpErrorMessage } from "@/helpers/errors";
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const isLoggingOut = ref(true);
const { alert, showAlert } = useAlert();

const router = useRouter();

async function logout() {
  try {
    const res = await api.auth.logout();
    processLogoutResponse(res);
    router.push("/login");
  } catch (e) {
    showAlert(`Can't logout: ${httpErrorMessage(e)}`);
    isLoggingOut.value = false;
  }
}

logout();
</script>

<style scoped>
.spinner {
  font-size: large;
  display: flex;
  align-items: center;
  justify-content: center;
}

.spinner p {
  margin: 0 0 0 1em;
}
</style>
