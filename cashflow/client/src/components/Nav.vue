<template>
  <nav class="nav">
    <img src="../assets/logo.png" alt="" class="n-logo">
    <div class="n-container">
      <router-link class="n-button" to="/"><h1 class="n-b-text">Home</h1></router-link>
    <router-link class="n-button" to="/recources"><h1 class="n-b-text">Recources</h1></router-link>
    <router-link class="n-button" to="/about"><h1 class="n-b-text">About</h1></router-link>
    <button v-if="userIsLoggedIn()" @click="logout">Logout</button>
    </div>

  </nav>
</template>

<script>
// import logo from '../assets/logo'
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