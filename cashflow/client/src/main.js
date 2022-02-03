import Vue from 'vue';
import App from './App.vue';
import VueRouter from 'vue-router';
import router from './router';
import './styles/index.css';
import './styles/App.css';

Vue.config.productionTip = false;
Vue.use(VueRouter);

new Vue({
  router,
  render: (h) => h(App)
}).$mount('#app');
