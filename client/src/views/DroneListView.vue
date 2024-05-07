<template>
    <NavbarComponent />
    <div class="container w-full h-full mt-20 flex gap-6 justify-center items-center">
        <div v-for="(drone,index) in drones" :key="index">
            <div class="card card-compact w-64 bg-slate-100 shadow-xl">
                <figure><img src="https://images.unsplash.com/photo-1473968512647-3e447244af8f?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Drone" /></figure>
                <div class="card-body">
                    <h2 class="card-title">{{ drone.name }}</h2>
                    <p>{{ drone.desc }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
    import { onMounted, computed } from "vue";
    import { NavbarComponent } from '@/components';
    import { useDroneStore } from '@/stores';

    const store = useDroneStore();

    const drones = computed(() => {
        return store.drones;
    });

    onMounted(() => {
        store.loadDrones()
    });
</script>