import { createRouter, createWebHistory } from 'vue-router'
import { HomeView } from '@/views'
import { useAuthStore } from '@/stores'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/dashboard',
      name: 'dashboard',
      component: () => import('../views/DroneListView.vue'), // lazy-loaded when the route is visited.
      meta: {
        requiresAuth: true // Add meta field to indicate protected route
      }
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('../views/SignupView.vue')
    },
    {
      path: '/drones',
      name: 'drones',
      component: () => import('../views/DroneListView.vue')
    },
    {
      path: '/tasks',
      name: 'tasks',
      component: () => import('../views/TaskListView.vue')
    },
    {
      path: '/',
      name: 'home',
      component: HomeView
    }
  ]
})

router.beforeEach(async (to) => {
  // redirect to login page if not logged in and trying to access a restricted page
  const publicPages = ['/', '/signup'];
  const authRequired = !publicPages.includes(to.path);
  const auth = useAuthStore();

  if (authRequired && !auth.token) {
      auth.returnUrl = to.fullPath;
      return '/';
  } else if (!authRequired && auth.token) {
    return '/dashboard';
  }
});

export default router
