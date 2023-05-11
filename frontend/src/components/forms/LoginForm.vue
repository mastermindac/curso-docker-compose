<template>
  <HtmlForm
    :title="title"
    @submit="(data) => $emit('submit', data)"
    :isLoading="isLoading"
    :fields="fields"
  />
</template>

<script setup>
import HtmlForm from '@/components/forms/HtmlForm.vue';

const props = defineProps({
  title: {
    type: String,
    default: "Login",
  },
  isLoading: {
    type: Boolean,
    default: false,
  },
  includeName: {
    type: Boolean,
    default: false,
  }
});

defineEmits(["submit"]);

let fields = [
  { name: 'email', label: 'Email', type: 'text' },
  { name: 'password', label: 'Password', type: 'password' },
]

if (props.includeName) {
  fields = [{ name: "name", label: "Name", type: "text" }, ...fields];
}
</script>
  