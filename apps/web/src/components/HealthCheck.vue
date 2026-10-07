<script setup lang="ts">
import { onMounted, ref } from 'vue'

const message = ref('Checking FastAPI...')

async function check() {
  message.value = 'Checking FastAPI...'
  try {
    const response = await fetch('http://127.0.0.1:8000/health', {
      signal: AbortSignal.timeout(5000),
    })
    const data = await response.json()
    if (!response.ok || data.status !== 'ok') throw new Error('Health check failed')
    message.value = 'Vue → FastAPI: Okay'
  } catch {
    message.value = 'FastAPI unavailable: check the server, port, and CORS.'
  }
}

onMounted(check)
</script>
<template>
  <section>
    <p>{{ message }}</p>
    <button @click="check">Check API</button>
  </section>
</template>
