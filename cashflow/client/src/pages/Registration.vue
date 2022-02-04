<template>
  <form @submit.prevent="handleSubmit">
    <label for="username">Username</label>
    <input id="username" name="username" type="text" v-bind="username">
    <label for="password">Password</label>
    <input id="password" name="password" type="text" v-bind="password">
    <label for="email">Email</label>
    <input id="email" name="email" type="email" v-bind="email">
    <label for="first-name">First Name</label>
    <input id="first-name" name="firstName" type="text" v-bind="firstName">
    <label for="last-name">Last Name</label>
    <input id="last-name" name="lastName" type="text" v-bind="lastName">
    <button type="submit">Submit</button>
  </form>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Registration',
  data: () => ({
    username: '',
    password: '',
    email: '',
    firstName: '',
    lastName: ''
  }),
  methods: {
    async handleSubmit(){
      
    }
  }
}
</script>

<style>

</style>