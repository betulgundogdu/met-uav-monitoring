import { getTasks } from "@/services/apiService"
import { defineStore } from 'pinia';

export const useTaskStore = defineStore({
  id: 'tasks',
  state: () => ({
      tasks: null
  }),
  actions: {
    async loadTasks() {
      getTasks()
        .then((response) => {
          if (response.status === 200) {
            this.tasks = response.data;
          }
        })
    },
  }
});