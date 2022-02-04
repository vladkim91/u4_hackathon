<template>
  <div class="login">
    <form @submit.prevent="handleSubmit">
      <label for="username">Username</label>
      <input id="username" name="username" type="text" v-model="userInfo.username">
      <label for="password">Password</label>
      <input id="password" name="password" type="password" v-model="userInfo.password">
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import { userLogin } from '../services/LoginServices'

export default {
  name: 'Login',
  data: () => ({
    userInfo: {
      username: '',
      password: ''
    }
  }),
  methods: {
    async handleSubmit() {
      const res = await userLogin(this.userInfo)
      if (res !== 'Failed!') {
        this.$router.push('/')
        localStorage.setItem('userId', res)
      }
    }
  }
};
</script>
