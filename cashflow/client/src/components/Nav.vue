<template>
  <nav class="nav">
    <router-link to="/">Home</router-link>
    <router-link to="/resources">Recources</router-link>
    <router-link to="/about">About</router-link>
    <button v-if="userIsLoggedIn()" @click="logout">Logout</button>
  </nav>
</template>

<script>
export default {
  name: 'Nav',
  methods: {
    userIsLoggedIn(){
      return localStorage.getItem('userId') !== null
    },
    logout(){
      localStorage.removeItem('userId')
      this.$router.push('/login')
    }
  }
};
</script>