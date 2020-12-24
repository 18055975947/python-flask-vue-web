<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js + TypeScript App"/>
  </div>
</template>

<script lang="ts">
import { defineComponent, inject } from 'vue'
import HelloWorld from '@/components/HelloWorld.vue' // @ is an alias to /src

declare global {
  interface Window {
    '$': any;
  }
}

export default defineComponent({
  name: 'Home',
  components: {
    HelloWorld
  },
  setup () {
    const axios: any = inject('axios')
    axios.get('http://localhost:5000/api/getRandomNum').then((res: object) => {
      console.log(res)
    }).catch((e: any) => {
      console.log(e)
    })
  }
})
</script>
