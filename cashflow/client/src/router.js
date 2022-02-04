import VueRouter from 'vue-router';

import Home from './pages/Home';
import Recources from './pages/Recources';
import About from './pages/About';
import Registration from './pages/Registration';

const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/recources', component: Recources, name: 'Recources' },
  { path: '/about', component: About, name: 'About' },
  { path: '/registration', component: Registration, name: 'Registration' }
];

export default new VueRouter({
  routes,
  mode: 'history'
});
