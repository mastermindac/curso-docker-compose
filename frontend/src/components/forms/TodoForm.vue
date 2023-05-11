<template>
  <HtmlForm
    :title="title"
    @submit="(data) => $emit('submit', data)"
    :prepopulate="prepopulate"
    :isLoading="isLoading"
    :fields="[
      { name: 'title', label: 'Todo Title', type: 'text' },
      { name: 'description', label: 'Todo Description', type: 'text' },
      { name: 'date', label: 'Todo Date', type: 'date' },
    ]"
  />
</template>

<script setup>
import HtmlForm from '@/components/forms/HtmlForm.vue';

const props = defineProps({
  title: {
    type: String,
    default: "Add Todo",
  },
  prepopulate: {
    type: Object,
    default: () => ({})
  },
  isLoading: {
    type: Boolean,
    default: false,
  }
});

defineEmits(["submit"]);
</script>
