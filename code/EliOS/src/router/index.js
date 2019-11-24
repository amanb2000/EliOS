import Vue from "vue";
import Router from "vue-router";
import firebase from 'firebase';

import Home from "../views/Home.vue";
import Login from '../views/Login.vue';
import SignUp from '../views/SignUp.vue';
import DataEntry from '../views/DataEntry.vue';
import Profile from '../views/Profile.vue';
import Contacts from '../views/Contacts.vue';
import AddContact from '../views/AddContact.vue';
import MonitorBrain from '../views/MonitorBrain.vue';

Vue.use(Router);

const routes = [
  {
    path: "/home",
    name: "home",
    component: Home,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/",
    redirect: "/login"
  },
  {
    path: "*",
    redirect: "/login"
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  }, 
  {
    path: '/data-entry',
    name: 'DataEntry',
    component: DataEntry,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/contacts',
    name: 'Contacts',
    component: Contacts,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/add-contact',
    name: 'AddContact',
    component: AddContact,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/brain',
    name: 'Brain',
    component: MonitorBrain,
    meta: {
      requiresAuth: true
    }
  }
];

const router = new Router({
  routes: routes
});

router.beforeEach((to, from, next) => {
  const currentUser = firebase.auth().currentUser;
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);

  if (requiresAuth && !currentUser) next('login');
  else next();
})

export default router;
