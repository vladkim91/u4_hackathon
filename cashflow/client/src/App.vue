<template>
  <div id="app">
    <header>
      <Nav />
    </header>
    <main>
      <router-view></router-view>
    </main>
    <Login
      :username="username"
      :password="password"
      @handleFormChange="handleFormChange"
      @handleSubmit="handleSubmit"
    />
  </div>
</template>

<script>
import Nav from './components/Nav.vue';
import Login from './pages/Login.vue';
export default {
  name: 'App',
  components: { Nav, Login },
  data: () => ({
    email: '',
    password: ''
  }),
  methods: {
    handleFormChange(name, value) {
      this[name] = value;
    },
    handleSubmit() {
      alert('form submitted');
      this.email = '';
      this.password = '';
    }
  }
};
</script>
