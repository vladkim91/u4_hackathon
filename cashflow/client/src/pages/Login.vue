<template>
  <div class="login">
    <form v-on:sumit="handleSubmit">
      <input
        type="username"
        name="username"
        :value="username"
        @input="handleChange"
        placeholder="Username"
      />
      <input
        type="password"
        name="password"
        :value="password"
        @input="handleChange"
        placeholder="Password"
      />
      <button>Log In</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'Login',
  props: {
    username: String,
    password: String
  },
  methods: {
    handleChange(e) {
      this.$emit('handleFormChange', e.target.name, e.target.value);
    },
    handleSubmit(e) {
      e.preventDefault();
      this.$emit('handleSubmit');
    }
  }
};
</script>
