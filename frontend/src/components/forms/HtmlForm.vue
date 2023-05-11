<template>
  <div class="form-background">
    <h1>{{ title }}</h1>
    <form class="form">
      <template v-for="field in fields">
        <div class="form-field">
          <label>{{ field.label }}</label>
        </div>
        <input :type="field.type" v-model="data[field.name]" />
      </template>

      <div class="submit">
        <Btn :disabled="isLoading" @click.prevent="$emit('submit', data)">
          <Spinner v-if="isLoading" />
          <span v-else>Submit</span>
        </Btn>
      </div>
    </form>
  </div>
</template>

<script setup>
import Btn from "@/components/Btn.vue";
import Spinner from "@/components/Spinner.vue";
import { reactive } from "vue";

const props = defineProps({
  title: {
    default: "Generic Form",
  },
  fields: {
    type: Array,
    default: () => [
      { label: "Title", type: "text", name: "title" },
      { label: "Description", type: "text", name: "description" },
    ],
  },
  prepopulate: {
    type: Object,
    default: () => ({}),
  },
  isLoading: {
    default: false,
  },
});

const data = reactive({ ...props.prepopulate });

defineEmits(["submit"]);
</script>

<style scoped>
.form-background {
  background-color: var(--navbar-color);
  padding: 20px;
  border-radius: 10px;
}

.form-field {
  margin-top: 20px;
}

.form > input {
  width: 100%;
  height: 30px;
  border: 1px solid var(--accent-color);
}

.submit {
  margin-top: 20px;
  display: flex;
  justify-content: end;
}

.submit button {
  height: 50px;
  width: 80px;
}
</style>
