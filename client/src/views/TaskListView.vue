<template>
    <NavbarComponent />
    <div class="overflow-x-auto">
        <table class="table">
            <!-- head -->
            <thead>
            <tr>
                <th>
                <label>
                    <input type="checkbox" class="checkbox" />
                </label>
                </th>
                <th>Name</th>
                <th>Description</th>
                <th>Drones</th>
                <th></th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(task,index) in tasks" :key="index">
                <th>
                <label>
                    <input type="checkbox" class="checkbox" />
                </label>
                </th>
                <td>
                <div class="flex items-center gap-3">
                    <div class="avatar">
                    <div class="mask mask-squircle w-12 h-12">
                        <img src="https://images.unsplash.com/photo-1473968512647-3e447244af8f?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Drone" />              </div>
                    </div>
                    <div>
                    <div class="font-bold">{{  task.title }}</div>
                    <span v-if="task.status" class="text-xs p-4 md:p-2 md:text-md badge badge-ghost badge-sm">{{  task.status }}</span>
                    </div>
                </div>
                </td>
                <td>
                {{  task.desc }}
                <br/>
                </td>
                <td>
                    <ul v-for="(drone,d_index) in task.drones" :key="d_index">
                        <li> <span class="text-xs p-4 md:p-2 m-1 md:text-md badge badge-primary badge-sm"> {{ drone.name }} </span></li>
                    </ul>
                </td>
                <th>
                    <button class="btn badge-accent btn-xs" :disabled="task.status != 'Not executed'">execute</button>
                </th>
                <th>
                    <button class="btn btn-ghost btn-xs">details</button>
                </th>
            </tr>
            </tbody>
            <!-- foot -->
            <tfoot>
            <tr>
                <th></th>
                <th>Name</th>
                <th>Description</th>
                <th>Drones</th>
                <th></th>
            </tr>
            </tfoot>
            
        </table>
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
        store.loadTasks();
    });

</script>