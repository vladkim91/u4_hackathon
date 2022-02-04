<template>
  <form @submit.prevent="handleSubmit">
    <label for="username">Username</label>
    <input id="username" name="username" type="text" v-model="loginInfo.username">
    <label for="password">Password</label>
    <input id="password" name="password" type="text" v-model="loginInfo.password">
    <label for="email">Email</label>
    <input id="email" name="email" type="email" v-model="loginInfo.email">
    <label for="first-name">First Name</label>
    <input id="first-name" name="firstName" type="text" v-model="loginInfo.firstName">
    <label for="last-name">Last Name</label>
    <input id="last-name" name="lastName" type="text" v-model="loginInfo.lastName">
    <button type="submit">Submit</button>
  </form>
</template>

<script>
import { registerUser } from '../services/LoginServices'

export default {
  name: 'Registration',
  data: () => ({
    loginInfo: {
      username: '',
      password: '',
      email: '',
      firstName: '',
      lastName: ''
    }
  }),
  methods: {
    async handleSubmit(){
      const res = await registerUser(this.loginInfo)
      console.log(res)
    }
  }
}
</script>

<style>

</style>