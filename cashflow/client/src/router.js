import VueRouter from 'vue-router';

import Home from './pages/Home';
import Recources from './pages/Recources';
import About from './pages/About';

const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/recources', component: Recources, name: 'Recources' },
  { path: '/about', component: About, name: 'About' }
];

export default new VueRouter({
  routes,
  mode: 'history'
});
