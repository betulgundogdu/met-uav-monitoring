<template>
    <div class="navbar bg-slate-100">
      <div class="flex-1">
        <a class="btn btn-ghost text-xl">
          <img src="https://droneqube.com.tr/wp-content/uploads/2023/03/droneqube_logo-250x30.png"/>
        </a>
      </div>
      <div class="flex-none">
        <ul class="menu menu-horizontal px-1">
          <li><RouterLink to="/drones">Drones</RouterLink></li>
          <li><RouterLink to="/tasks">Tasks</RouterLink></li>
          <li class="text-teal-600"><button @click="logout">Logout</button></li>
        </ul>
      </div>
    </div>
  </template>
  
  <script setup>
        import { useAuthStore } from '@/stores'
        const store = useAuthStore();

        function logout() {
            store.logout().then(() => {
                console.log('logout');
            });
        };
  </script>
  
  
  