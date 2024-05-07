<template>
    <NavbarComponent />
    <div class="container w-full h-full mt-20 flex gap-6 justify-center items-center">
        <div v-for="(task,index) in tasks" :key="index">
            <div class="card card-compact w-64 bg-slate-100 shadow-xl">
                <div class="card-body">
                    <h2 class="card-title">{{ task.title }}</h2>
                    <p>{{ task.desc }}</p>
                    <p>{{ task.status }}</p>
                    <ul v-for="(drone,d_index) in task.drones" :key="d_index">
                        <li>{{ drone.name }}</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
    import { onMounted, computed } from "vue";
    import { NavbarComponent } from '@/components';
    import { useTaskStore } from '@/stores';

    const store = useTaskStore();
    
    const tasks = computed(() => {
        return store.tasks;
    });

    onMounted(() => {
        store.loadTasks()
    });

</script>